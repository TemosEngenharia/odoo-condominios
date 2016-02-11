# -*- coding: utf-8 -*-
from datetime import datetime
from openerp import models, fields, api


class VirdiAcesso(models.Model):
    _name = 'occ.acesso'
    _table = 'occ_acesso'
    status = fields.Char(u'Situação')
    apto = fields.Char(u'Apartamento')
    placa = fields.Char(u'Placa')
    horario = fields.Char(u'Horario')
    morador = fields.Char(u'Morador')
    sentido = fields.Selection([('in', u'Entrada'), ('out', u'Saída')])


class VirdiTerminais(models.Model):
    _name = 'occ.virdi'
    _rec_name = 'terminal_tipo'
    _description = u'Terminais Virdi'
    _order = 'terminal_status'
    _table = 'occ_virdi'
    active = fields.Boolean('Ativo', default=True)
    terminal_id = fields.Char(u'ID do terminal', size=8, required=True)
    terminal_ip = fields.Char(u'IP do terminal', size=15, require=True)
    terminal_port = fields.Char(u'Porta socket terminal', size=5,
                                readonly=True, require=True)
    terminal_tipo = fields.Selection([('in', u'Entrada'), ('out', u'Saída')],
                                     u"Tipo", default='in', required=True)
    terminal_status = fields.Selection([('open', u'Aberta'),
                                        ('close', u'Fechada')],
                                       u"Estado", default='close',
                                       required=True)

    @api.multi
    def do_open_lock(self):
        self.terminal_status = 'open'
        return True


class ControleAcesso(models.Model):
    _name = 'occ.controle.acesso'
    _rec_name = 'apto_id'
    _description = u'Tabela de Controle de Acesso'
    _table = 'occ_controle_acesso'
    _order = 'horario desc'
    horario = fields.Char(
        u'Horário', default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    sentido = fields.Selection([('in', u'Entrada'), ('out', u'Saída')],
                               u"Sentido")
    morador = fields.Many2one('occ.morador', u'Morador')
    placa = fields.Many2one('occ.veiculo', u'Placa')
    apto_id = fields.Many2one('occ.apto', u'Apartamento')
    status = fields.Char(u'Situação')

    @api.multi
    def abrir_cancela(self):
        sql = """
            UPDATE occ_virdi SET terminal_status = 'open'
                WHERE terminal_tipo = %s;
        """
        self.env.cr.execute(sql, (self.sentido, ))
        self.env.invalidate_all()
        return True


class StatusAcessoManualCancela(models.Model):
    _name = 'occ.status.abertura.manual'
    _description = u'Tabela com os possíveis motivos para entrada sem leitura \
                    do TAG'
    _order = 'name'
    _table = 'occ_status_abertura_manual'
    active = fields.Boolean('Ativo', default=True)
    name = fields.Char(u'Situação', required=True)


class ControleManualCancela(models.Model):
    _name = 'occ.controle.manual.cancela'
    _rec_name = 'placa_manual'
    _description = u'Tabela com os dados para abertura manual da cancela'
    _table = 'occ_controle_manual_cancela'
    _order = 'create_date desc'
    sentido = fields.Selection([('in', u'Entrada'), ('out', u'Saída')],
                               u"Sentido", required=True)
    bloco_id = fields.Many2one('occ.bloco', u'Bloco', required=True)
    apto_id = fields.Many2one('occ.apto', u'Apartamento', required=True,
                              domain="[('bloco_id','=',bloco_id)]")
    placa_manual = fields.Char(u'Placa', size=7, required=True)
    placa_id = fields.Many2one('occ.veiculo', u'Placa')
    morador_id = fields.Many2one('occ.morador', u'Morador')
    status = fields.Many2one('occ.status.abertura.manual', u'Situação',
                             required=True)

    @api.multi
    def write(self, vals):
        sql = """
            UPDATE occ_virdi SET terminal_status = 'open'
                WHERE terminal_tipo = %s;
        """
        self.env.cr.execute(sql, (self.sentido, ))
        self.env.invalidate_all()
        return models.Model.write(self, vals)


class ControleManualVisitante(models.Model):
    _name = 'occ.controle.manual.visitante'
    _rec_name = 'visitante_id'
    _description = u'Tabela com os dados para abertura portão visitante'
    _table = 'occ_controle_manual_visitante'
    _order = 'create_date desc'
    sentido = fields.Selection([('in', u'Entrada'), ('out', u'Saída')],
                               u"Sentido", required=True, default='in')
    bloco_id = fields.Many2one('occ.bloco', u'Bloco', required=True)
    apto_id = fields.Many2one('occ.apto', u'Apartamento', required=True,
                              domain="[('bloco_id','=',bloco_id)]")
    visitante_id = fields.Many2one('occ.visitante', u'Visitante',
                                   required=True)
    morador_id = fields.Many2one('occ.morador', u'Entrada autorizada por',
                                 domain="[('apto_id','=',apto_id)]",
                                 required=True)


class ControleManualPrestServ(models.Model):
    _name = 'occ.controle.manual.funcionario'
    _rec_name = 'funcionario_id'
    _description = u'Tabela com os dados para abertura portão empresas'
    _table = 'occ_controle_manual_funcionario'
    _order = 'create_date desc'
    sentido = fields.Selection([('in', u'Entrada'), ('out', u'Saída')],
                               u"Sentido", required=True, default='in')
    bloco_id = fields.Many2one('occ.bloco', u'Bloco', required=True)
    apto_id = fields.Many2one('occ.apto', u'Apartamento', required=True,
                              domain="[('bloco_id','=',bloco_id)]")
    funcionario_id = fields.Many2one('occ.funcionario',
                                     u'Prestador de Serviço',
                                     required=True)
    morador_id = fields.Many2one('occ.morador', u'Entrada autorizada por',
                                 domain="[('apto_id','=',apto_id)]",
                                 required=True)
