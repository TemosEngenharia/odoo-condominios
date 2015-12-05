# -*- coding: utf-8 -*-
from openerp import models, fields


class OccBloco(models.Model):
    _name = 'occ.bloco'
    _description = 'Detalhes dos Blocos'
    _order = 'name'
    _table = 'occ_bloco'
    _sql_constraints = [('occ.bloco', 'UNIQUE (name)',
                         'Os nomes dos blocos devem ser únicos')]
    name = fields.Char('Bloco', size=4, required=True)
    apto_ids = fields.One2many('occ.apto', 'bloco_id',
                               'Apartamentos neste bloco')
    morador_ids = fields.One2many('occ.morador', 'bloco_id',
                                  'Moradores neste bloco')
    vaga_ids = fields.One2many('occ.vaga', 'bloco_id', 'Vagas neste bloco')


class OccVaga(models.Model):
    _name = 'occ.vaga'
    _description = 'Detalhes das Vagas'
    _order = 'name'
    _table = 'occ_vaga'
    _sql_constraints = [('occ.vagas', 'UNIQUE (name)',
                         'Os nomes das vagas devem ser únicos')]
    name = fields.Char(string='Vaga', size=4, required=True)
    tipo = fields.Selection([('carro', 'Vaga Carro'), ('moto', 'Vaga Moto')],
                            "Tipo", default='carro', required=True)
    bloco_id = fields.Many2one('occ.bloco', 'Bloco',
                               ondelete="cascade", required=True)
    apto_id = fields.Many2one('occ.apto', 'Apartamento')
    tag_ids = fields.Many2many('occ.tag', 'TAG')


class OccApto(models.Model):
    _name = 'occ.apto'
    _description = 'Detalhes dos Apartamentos'
    _order = 'name'
    _table = 'occ_apto'
    _sql_constraints = [('occ.apto', 'UNIQUE (name,bloco_id)',
                         'Os nomes dos apartamentos devem ser '
                         'únicos dentro de cada bloco')]
    name = fields.Char('Apartamento', size=4, required=True)
    morador_ids = fields.One2many('occ.morador', 'apto_id',
                                  'Moradores neste Apartamento')
    bloco_id = fields.Many2one('occ.bloco', 'Bloco',
                               ondelete="cascade", required=True)
    vaga_id = fields.Many2one('occ.vaga', string='Vaga', required=True,
                              domain="[('bloco_id','=',bloco_id)]")


class OccVeiculo(models.Model):
    _name = 'occ.veiculo'
    _description = 'Detalhes das Veiculos'
    _order = 'name'
    _table = 'occ_veiculos'
    _sql_constraints = [('occ.veiculo', 'UNIQUE (name)',
                         'Placa já cadastrada')]
    _sql_constraints = [('occ.veiculo', 'UNIQUE (name,tag_id)',
                         'Um veículo deve ter somente uma TAG ativa por vez')]
    active = fields.Boolean('Ativo', default=True)
    name = fields.Char(string='Placa', size=8, required=True)
    tipo = fields.Selection([('carro', 'Carro'), ('moto', 'Moto')], "Tipo",
                            default='carro', required=True)
    morador_id = fields.Many2one('occ.morador', 'Morador', ondelete="cascade",
                                 required=True)
    tag_id = fields.Many2one('occ.tag', 'TAG', ondelete="cascade",
                             required=True)


class OccTAG(models.Model):
    _name = 'occ.tag'
    _description = 'Detalhes das TAGs'
    _order = 'name'
    _table = 'occ_tag'
    _sql_constraints = [('occ.tag', 'UNIQUE (name)',
                         'As TAGs devem ser únicas')]

    active = fields.Boolean('Ativo', default=True)
    name = fields.Char(string='TAG', size=46, required=True)
    tipo = fields.Selection([('carro', 'TAG Carro'), ('moto', 'TAG Moto')],
                            "Tipo", default='carro', required=True)
    veiculo_ids = fields.Many2one('occ.veiculo', 'Placa', ondelete="cascade")
    vaga_ids = fields.Many2many('occ.tag', 'occ_tag_rel', 'tag_id', 'vaga_id',
                                string='TAGs', ondelete="cascade")
