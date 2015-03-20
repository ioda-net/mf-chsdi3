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


class emapis(Base, Vector):
    __tablename__ = 'emapis'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-entwaesserung'
    #__queryable_attributes__ = ['farbe']
    __label__ = 'geschaeftsnummer'
    id = Column('xtf_id', Text, primary_key=True)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    typ = Column('typ', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.blw.emapis-entwaesserung', emapis)
