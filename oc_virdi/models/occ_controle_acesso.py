# -*- coding: utf-8 -*-
from openerp import models, fields, api


class VirdiTerminais(models.Model):
    _name = 'occ.virdi'
    _description = 'Equipamentos Virdi'
    _order = 'terminal_id'
    _table = 'occ_virdi'
    terminal_id = fields.Char('ID do terminal', size=8, required=True)
    terminal_ip = fields.Char('IP do terminal', size=15, require=True)
    terminal_port = fields.Char('Porta socket terminal', size=5,
                                readonly=True, require=True)
    terminal_tipo = fields.Selection([('in', 'Entrada'), ('out', 'Saída')],
                                     "Tipo", default='in', required=True)
    terminal_status = fields.Selection([('open', 'Aberta'),
                                        ('close', 'Fechada')],
                                       "Estado", default='close',
                                       required=True)

    @api.multi
    def do_open_lock(self):
        self.terminal_status = 'open'
        return True


class ControleAcesso(models.Model):
    _name = 'occ.controle.acesso'
    _description = 'Tabela de Controle de Acesso'
    _table = 'occ_controle_acesso'
    horario = fields.Char('Horário')
    sentido = fields.Selection([('in', 'Entrada'), ('out', 'Saída')],
                               "Sentido", default='in')
    morador = fields.Many2one('occ.morador', 'Morador')
    placa = fields.Many2one('occ.veiculo', 'Placa')
    status = fields.Char('Situação')

    def abrir_cancela_entrada(a, b, c, d, e):  # @NoSelf
        import psycopg2.extensions
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
        with psycopg2.connect(database="reserva", user="cezar") as conn_pg:
            with conn_pg.cursor() as conn_pgs:
                conn_pgs.execute("update occ_virdi SET terminal_status = 'open' \
                                 where terminal_tipo = 'in';")
        return True

    def abrir_cancela_saida(a, b, c, d, e):  # @NoSelf
        import psycopg2.extensions
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
        with psycopg2.connect(database="reserva", user="cezar") as conn_pg:
            with conn_pg.cursor() as conn_pgs:
                conn_pgs.execute("update occ_virdi SET terminal_status = 'open' \
                                 where terminal_tipo = 'out';")
        return True
