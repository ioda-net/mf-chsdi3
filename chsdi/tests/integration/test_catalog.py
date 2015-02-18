# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestCatalogService(TestsBase):

    def test_catalog_no_params(self):
        resp = self.testapp.get('/rest/services/blw/CatalogServer', status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless('root' in resp.json['results'])
        self.failUnless('children' in resp.json['results']['root'])
        self.failUnless('selectedOpen' in resp.json['results']['root']['children'][0])
        self.failUnless('category' in resp.json['results']['root'])

    def test_catalog_with_callback(self):
        resp = self.testapp.get('/rest/services/blw/CatalogServer', params={'callback': 'cb'}, status=200)
        self.failUnless(resp.content_type == 'application/javascript')

    def test_catalog_existing_map_no_catalog(self):
        self.testapp.get('/rest/services/all/CatalogServer', status=404)

    def test_catalog_wrong_map(self):
        self.testapp.get('/rest/services/foo/CatalogServer', status=400)

    def test_catalog_ordering(self):
        resp = self.testapp.get('/rest/services/inspire/CatalogServer', params={'lang': 'en'}, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless('AGNES' in resp.json['results']['root']['children'][0]['children'][0]['children'][0]['label'])
        self.failUnless('Geoid in CH1903' in resp.json['results']['root']['children'][0]['children'][0]['children'][1]['label'])

    def test_catalog_languages(self):
        for lang in ('de', 'fr', 'it', 'rm', 'en'):
            link = '/rest/services/ech/CatalogServer?lang=' + lang
            resp = self.testapp.get(link)
            self.failUnless(resp.status_int == 200, link)

    def test_all_catalogs(self):

        def existInTree(id, root):
            if (root['id'] == id):
                return True
            if 'children' in root:
                for child in root.get('children'):
                    if (existInTree(id, child)):
                        return True
            return False

        def existInList(node, l):
            found = False
            for entry in l:
                if entry.id == node.get('id'):
                    found = True
                    break

            if not found:
                print node.get('id')
                return False

            if 'children' in node:
                for child in node.get('children'):
                    if not existInList(child, l):
                        return False
            return True

        from chsdi.models.bod import Catalog
        from sqlalchemy.orm import scoped_session, sessionmaker
        DBSession = scoped_session(sessionmaker())
        old_staging = self.testapp.app.registry.settings['geodata_staging']
        # We fix staging for next calls to prod
        self.testapp.app.registry.settings['geodata_staging'] = 'prod'
        try:
            resp = self.testapp.get('/rest/services', status=200)
            for t in resp.json['topics']:
                topic = t.get('id')
                query = DBSession.query(Catalog).filter(Catalog.topic == topic).filter(Catalog.staging == 'prod')
                resp = self.testapp.get('/rest/services/' + topic + '/CatalogServer', status=200)
                entries = query.all()
                # Check if every entry in view_catalog of db is in catalog returned by catalog service
                for catalogEntry in entries:
                    self.failUnless(existInTree(catalogEntry.id, resp.json['results']['root']), catalogEntry.id)

                # Check if every node in the catalog is in view_catalog of db
                self.failUnless(existInList(resp.json['results']['root'], entries))

        finally:
            # reset staging to previous setting
            self.testapp.app.registry.settings['geodata_staging'] = old_staging
            DBSession.close()
