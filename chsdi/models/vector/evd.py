# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, Integer
from geoalchemy2.types import Geometry

from chsdi.models import register, bases
from chsdi.models.vector import Vector

Base = bases['evd']


class BODENEIGNUNG(Base, Vector):
    __tablename__ = 'bodeneignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/bodeneignung-kulurtyp.mako'
    __bodId__ = 'ch.blw.bodeneignung-kulturtyp'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'symb_color'
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))
    farbe = Column('farbe', Integer)
    symb_color = Column('symb_color', Text)

register('ch.blw.bodeneignung-kulturtyp', BODENEIGNUNG)


class emapis_entwaesserung(Base, Vector):
    __tablename__ = 'emapis_entwaesserung'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-entwaesserung'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'geschaeftsnummer'
    id = Column('xtf_id', Text, primary_key=True)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    typ = Column('typ', Text)
    status = Column('status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.blw.emapis-entwaesserung', emapis_entwaesserung)


class emapis_wegebau(Base, Vector):
    __tablename__ = 'emapis_wegebau'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-wegebau'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'geschaeftsnummer'
    id = Column('xtf_id', Text, primary_key=True)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    typ = Column('typ', Text)
    status = Column('status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.blw.emapis-wegebau', emapis_wegebau)


class emapis_seilbahnen(Base, Vector):
    __tablename__ = 'emapis_seilbahnen'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-seilbahnen'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'geschaeftsnummer'
    id = Column('xtf_id', Text, primary_key=True)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    typ = Column('typ', Text)
    status = Column('status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.blw.emapis-seilbahnen', emapis_seilbahnen)


class emapis_wasserversorgung(Base, Vector):
    __tablename__ = 'emapis_wasserversorgung'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-wasserversorgung'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'geschaeftsnummer'
    id = Column('xtf_id', Text, primary_key=True)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    typ = Column('typ', Text)
    status = Column('status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.blw.emapis-wasserversorgung', emapis_wasserversorgung)


class emapis_projektschwerpunkt(Base, Vector):
    __tablename__ = 'emapis_projektschwerpunkt'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-projektschwerpunkt'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'geschaeftsnummer'
    id = Column('xtf_id', Text, primary_key=True)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    typ = Column('typ', Text)
    status = Column('status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.blw.emapis-projektschwerpunkt', emapis_projektschwerpunkt)


class emapis_oekologie(Base, Vector):
    __tablename__ = 'emapis_oekologie'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-oekologie'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'geschaeftsnummer'
    id = Column('xtf_id', Text, primary_key=True)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    typ = Column('typ', Text)
    status = Column('status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.blw.emapis-oekologie', emapis_oekologie)


class emapis_milchleitung(Base, Vector):
    __tablename__ = 'emapis_milchleitung'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-milchleitung'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'geschaeftsnummer'
    id = Column('xtf_id', Text, primary_key=True)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    typ = Column('typ', Text)
    status = Column('status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.blw.emapis-milchleitung', emapis_milchleitung)


class emapis_hochbau(Base, Vector):
    __tablename__ = 'emapis_hochbau'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-hochbau'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'geschaeftsnummer'
    id = Column('xtf_id', Text, primary_key=True)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    typ = Column('typ', Text)
    status = Column('status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.blw.emapis-hochbau', emapis_hochbau)


class emapis_elektrizitaetsversorgung(Base, Vector):
    __tablename__ = 'emapis_elektrizitaetsversorgung'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-elektrizitaetsversorgung'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'geschaeftsnummer'
    id = Column('xtf_id', Text, primary_key=True)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    typ = Column('typ', Text)
    status = Column('status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.blw.emapis-elektrizitaetsversorgung', emapis_elektrizitaetsversorgung)


class emapis_bewaesserung(Base, Vector):
    __tablename__ = 'emapis_bewaesserung'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-bewaesserung'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'geschaeftsnummer'
    id = Column('xtf_id', Text, primary_key=True)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    typ = Column('typ', Text)
    status = Column('status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.blw.emapis-bewaesserung', emapis_bewaesserung)


class emapis_beizugsgebiet(Base, Vector):
    __tablename__ = 'emapis_beizugsgebiet'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-beizugsgebiet'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'geschaeftsnummer'
    id = Column('xtf_id', Text, primary_key=True)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    typ = Column('typ', Text)
    status = Column('status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.blw.emapis-beizugsgebiet', emapis_beizugsgebiet)
