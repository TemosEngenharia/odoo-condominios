# -*- coding: utf-8 -*-

from openerp import models, fields, api
class OccBloco(models.Model):
    _name = 'occ.bloco'
    _order = 'name'
    _rec_name = 'name'
    _table = 'occ_bloco'
    name = fields.Char('Bloco', required=True)
    apto = fields.One2many('occ.apto', 'bloco_id', 'Apartamentos neste bloco')
