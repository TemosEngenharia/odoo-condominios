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
    vaga_carro_ids = fields.One2many('occ.vaga.carro', 'bloco_id',
                                     'Vagas para Carros neste bloco')
    vaga_moto_ids = fields.One2many('occ.vaga.moto', 'bloco_id',
                                    'Vagas para Motos neste bloco')


class OccVagaCarro(models.Model):
    _name = 'occ.vaga.carro'
    _description = 'Detalhes das Vagas de Carros'
    _order = 'name'
    _table = 'occ_vaga_carro'
    _sql_constraints = [('occ.vaga.carro', 'UNIQUE (name)',
                         'Os nomes das vagas devem ser únicos')]
    name = fields.Char(string='Vaga Carro', size=4, required=True)
    bloco_id = fields.Many2one('occ.bloco', 'Bloco', required=True)
    apto_id = fields.Many2one('occ.apto', 'Apartamento',
                              domain="[('bloco_id','=',bloco_id)]")
    tag_ids = fields.Many2many('occ.tag', 'occ_tag_carro_rel',
                               'vaga_carro_ids', 'tag_ids',
                               string='TAGs')
    status = fields.Boolean('Status', default=True)
"""    veiculo_ids = fields.Many2many('occ.tag', 'occ_tag_carro_rel',
                                   'vaga_carro_ids', 'tag_ids',
                                   string='TAGs')"""


class OccVagaMoto(models.Model):
    _name = 'occ.vaga.moto'
    _description = 'Detalhes das Vagas de Motos'
    _order = 'name'
    _table = 'occ_vaga_moto'
    _sql_constraints = [('occ.vaga.moto', 'UNIQUE (name)',
                         'Os nomes das vagas devem ser únicos')]
    name = fields.Char(string='Vaga Moto', size=4, required=True)
    bloco_id = fields.Many2one('occ.bloco', 'Bloco', required=True)
    apto_id = fields.Many2one('occ.apto', 'Apartamento',
                              domain="[('bloco_id','=',bloco_id)]")
    tag_ids = fields.Many2many('occ.tag', 'occ_tag_moto_rel',
                               'vaga_moto_ids', 'tag_ids',
                               string='TAGs')
    status = fields.Boolean('Status', default=True)
"""    veiculo_ids = fields.Many2many('occ.tag', 'occ_tag_moto_rel',
                                   'vaga_moto_ids', 'tag_ids',
                                   string='TAGs')"""


class OccApto(models.Model):
    _name = 'occ.apto'
    _description = 'Detalhes dos Apartamentos'
    _order = 'name'
    _table = 'occ_apto'
    _sql_constraints = [('occ.apto', 'UNIQUE (name)',
                         'Os nomes dos apartamentos devem ser únicos')]
    name = fields.Char('Apartamento', size=4, required=True)
    numero = fields.Char('Número', size=4, required=True)
    morador_ids = fields.One2many('occ.morador', 'apto_id',
                                  'Moradores neste Apartamento')
    bloco_id = fields.Many2one('occ.bloco', 'Bloco',
                               ondelete="cascade", required=True)
    vaga_carro_id = fields.Many2one('occ.vaga.carro', 'Vaga Carro',
                                    domain="[('bloco_id','=',bloco_id)]")
    vaga_moto_id = fields.Many2one('occ.vaga.moto', 'Vaga Moto',
                                   domain="[('bloco_id','=',bloco_id)]")


class OccTAG(models.Model):
    _name = 'occ.tag'
    _description = 'Detalhes das TAGs'
    _order = 'name'
    _table = 'occ_tag'
    _sql_constraints = [('occ.tag', 'UNIQUE (name)',
                         'As TAGs devem ser únicas')]

    active = fields.Boolean('Ativo', default=True)
    name = fields.Char(string='TAG', size=6, required=True)
    tipo = fields.Selection([('carro', 'TAG Carro'), ('moto', 'TAG Moto')],
                            "Tipo", default='carro', required=True)
    veiculo_ids = fields.One2many('occ.veiculo', 'tag_id', 'Veículo')
    vaga_carro_ids = fields.Many2many('occ.vaga.carro', 'occ_tag_carro_rel',
                                      'tag_ids', 'vaga_carro_ids',
                                      string='Vagas Carro')
    vaga_moto_ids = fields.Many2many('occ.vaga.moto', 'occ_tag_moto_rel',
                                     'tag_ids', 'vaga_moto_ids',
                                     string='Vagas Moto')


class OccVeiculo(models.Model):
    _name = 'occ.veiculo'
    _description = 'Detalhes das Veiculos'
    _order = 'name'
    _table = 'occ_veiculos'
    _sql_constraints = [('occ.veiculo', 'UNIQUE (name)',
                         'Placa já cadastrada')]
    _sql_constraints = [('occ.veiculo', 'UNIQUE (name,tag_id)',
                         'Um veículo deve ter somente uma TAG ativa por vez')]
    _sql_constraints = [('occ.veiculo', 'UNIQUE (tag_id)',
                         'Tag já cadastrado')]
    active = fields.Boolean('Ativo', default=True)
    name = fields.Char(string='Placa', size=8, required=True)
    tipo = fields.Selection([('carro', 'Carro'), ('moto', 'Moto')], "Tipo",
                            default='carro', required=True)
    morador_id = fields.Many2one('occ.morador', 'Morador', ondelete="cascade",
                                 required=True)
    tag_id = fields.Many2one('occ.tag', 'TAG', required=True,
                             domain="[('tipo','=',tipo)]")
    status = fields.Boolean('Status', default=False)
"""
    vaga_carro_ids = fields.Many2many('occ.vaga.carro', 'occ_tag_carro_rel',
                                      'tag_ids', 'tag_id',
                                      string='Vagas', readonly=True,
                                      domain="[('tipo','=',tipo), \
                                      ('tag_id','=',tag_ids]")
    vaga_moto_ids = fields.Many2many('occ.vaga.moto', 'occ_tag_moto_rel',
                                     'tag_ids', 'tag_id',
                                     string='Vagas', readonly=True,
                                     domain="[('tipo','=',tipo), \
                                     ('tag_id','=',tag_ids]")
"""
