# -*- coding: utf-8 -*-

from openerp import models, fields, api
class OccPessoas(models.Model):
    _name = 'occ.pessoas'
    _order = 'name'
    _rec_name = 'name'
    _table = 'occ_pessoas'
    name = fields.Char('Nome', size=40, translate=True, required=True, help="Entrar com o nome completo do morador")
    active = fields.Boolean('Ativo', default=True)
    image = fields.Binary('Foto', translate=True, help="Digitalizar a foto do morador")
    rg = fields.Char('Identidade', size=15, required=True, help="Entrar com o número do RG")
    cpf = fields.Char('CPF', size=15, require=True, help="Entrar somente com os números do CPF")
    telefone = fields.Char('Telefone', size=10, translate=True, help="Inserir o telefone do apartamento")
    celular = fields.Char('Celular', size=11, placeholder="11942454999", translate=True, help="Inserir o número do celular com o DDD")
    email = fields.Char('email', placeholder="cezar.santanna@gmail.com")
    bloco_id = fields.Many2one('occ.bloco', 'Bloco')
    apto_id = fields.Many2one('occ.apto', 'Apartamento')