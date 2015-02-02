# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, Integer
from geoalchemy2.types import Geometry
from sqlalchemy.types import Numeric
from chsdi.models import *
from chsdi.models.vector import Vector

Base = bases['vbs']


class Kulturgueter(Base, Vector):
    __tablename__ = 'kgs'
    __table_args__ = ({'schema': 'babs', 'autoload': False})
    __template__ = 'templates/htmlpopup/kgs.mako'
    __queryable_attributes__ = ['zkob']
    __bodId__ = 'ch.babs.kulturgueter'
    __extended_info__ = True
    __label__ = 'zkob'
    id = Column('kgs_nr', Integer, primary_key=True)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))
    zkob = Column('zkob', Text)
    x = Column('x', Numeric)
    y = Column('y', Numeric)
    kategorie = Column('kategorie', Text)
    gemeinde = Column('gemeinde', Text)
    gemeinde_ehemalig = Column('gemeinde_ehemalig', Text)
    objektart = Column('objektart', Text)
    hausnr = Column('hausnr', Text)
    adresse = Column('adresse', Text)
    kurztexte = Column('kurztexte', Text)
    kt_kz = Column('kt_kz', Text)
    pdf_list = Column('pdf_list', Text)
    link_uri = Column('link_uri', Text)
    link_title = Column('link_title', Text)
    link_2_uri = Column('link_2_uri', Text)
    link_2_title = Column('link_2_title', Text)
    link_3_uri = Column('link_3_uri', Text)
    link_3_title = Column('link_3_title', Text)

register('ch.babs.kulturgueter', Kulturgueter)


class TERRITORIALREGIONEN(Base, Vector):
    __tablename__ = 'territorialregionen'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/territorialregionen.mako'
    __bodId__ = 'ch.vbs.territorialregionen'
    __label__ = 'name'
    id = Column('terreg_nr', Integer, primary_key=True)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=3, srid=21781))
    name = Column('name', Text)

register('ch.vbs.territorialregionen', TERRITORIALREGIONEN)


class sim_facilities_a(Base, Vector):
    __tablename__ = 'sim_fac_anhoerung'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/sim_facilities.mako'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_anhorung'
    id = Column('stabil_id', Text, primary_key=True)
    facility = Column('facility', Text)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    objname_de = Column('objname_de', Text)
    objname_fr = Column('objname_fr', Text)
    objname_it = Column('objname_it', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.vbs.sachplan-infrastruktur-militaer_anhorung', sim_facilities_a)


class sim_facilities_k(Base, Vector):
    __tablename__ = 'sim_fac_kraft'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/sim_facilities.mako'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_kraft'
    id = Column('stabil_id', Integer, primary_key=True)
    facility = Column('facility', Text)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    objname_de = Column('objname_de', Text)
    objname_fr = Column('objname_fr', Text)
    objname_it = Column('objname_it', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.vbs.sachplan-infrastruktur-militaer_kraft', sim_facilities_k)


class sim_planning_k(Base, Vector):
    __tablename__ = 'sim_pl_kraft'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/sim_planning.mako'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_kraft'
    id = Column('stabil_id', Text, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    bgdi_created = Column('bgdi_created', Text)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.vbs.sachplan-infrastruktur-militaer_kraft', sim_planning_k)


class sim_planning_a(Base, Vector):
    __tablename__ = 'sim_pl_anhoerung'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/sim_planning.mako'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_anhorung'
    id = Column('stabil_id', Text, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    bgdi_created = Column('bgdi_created', Text)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.vbs.sachplan-infrastruktur-militaer_anhorung', sim_planning_a)


class sim_planning_raster_a(Base, Vector):
    __tablename__ = 'sim_pl_r_anhoerung'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/sim_planning.mako'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_anhorung'
    id = Column('stabil_id', Text, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    bgdi_created = Column('bgdi_created', Text)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.vbs.sachplan-infrastruktur-militaer_anhorung', sim_planning_raster_a)


class sim_planning_raster_k(Base, Vector):
    __tablename__ = 'sim_pl_r_kraft'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/sim_planning.mako'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_kraft'
    id = Column('stabil_id', Integer, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    bgdi_created = Column('bgdi_created', Text)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.vbs.sachplan-infrastruktur-militaer_kraft', sim_planning_raster_k)
