# -*- coding: utf-8 -*-

from openerp import models, fields, api
class occbloco(models.Model):
    _name = 'occ.bloco'
    name = fields.Char('Nome do Bloco', required=True)