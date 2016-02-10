# -*- coding: utf-8 -*-
from openerp import models, fields


class OccVagaCarro(models.Model):
    _name = 'occ.vaga.carro'
    _description = 'Detalhes das Vagas de Carros'
    _order = 'name'
    _table = 'occ_vaga_carro'
    _sql_constraints = [('occ.vaga.carro', 'UNIQUE (name)',
                         'Os nomes das vagas devem ser únicos')]
    active = fields.Boolean('Ativo', default=True)
    name = fields.Char(string='Vaga Carro', size=4, required=True)
    bloco_id = fields.Many2one('occ.bloco', 'Bloco', required=True)
    apto_id = fields.Many2one('occ.apto', 'Apartamento',
                              domain="[('bloco_id','=',bloco_id)]")
    tag_ids = fields.Many2many('occ.tag', 'occ_tag_carro_rel',
                               'vaga_carro_ids', 'tag_ids',
                               string='TAGs')
    status = fields.Boolean('Status', default=False)


class OccVagaMoto(models.Model):
    _name = 'occ.vaga.moto'
    _description = 'Detalhes das Vagas de Motos'
    _order = 'name'
    _table = 'occ_vaga_moto'
    _sql_constraints = [('occ.vaga.moto', 'UNIQUE (name)',
                         'Os nomes das vagas devem ser únicos')]
    active = fields.Boolean('Ativo', default=True)
    name = fields.Char(string='Vaga Moto', size=4, required=True)
    bloco_id = fields.Many2one('occ.bloco', 'Bloco', required=True)
    apto_id = fields.Many2one('occ.apto', 'Apartamento',
                              domain="[('bloco_id','=',bloco_id)]")
    tag_ids = fields.Many2many('occ.tag', 'occ_tag_moto_rel',
                               'vaga_moto_ids', 'tag_ids',
                               string='TAGs')
    status = fields.Boolean('Status', default=False)
