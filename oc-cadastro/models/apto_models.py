# -*- coding: utf-8 -*-

from openerp import models, fields, api
class OccApto(models.Model):
    _name = 'occ.apto'
    _order = 'name'
    _rec_name = 'name'
    _table = 'occ_apto'
    name = fields.Char('Apartamento', size=40, translate=True, required=True)
    bloco_id = fields.Many2one('occ.bloco', 'Bloco', required=True)
    pessoas = fields.One2many('occ.pessoas', 'apto_id', 'Moradores neste apartamento')