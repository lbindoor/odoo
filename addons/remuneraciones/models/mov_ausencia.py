# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuMovAusencia(models.Model):
    _name = "remu.mov.ausencia"
    _description = "Movimientos de Ausencias"
    _order = "date_from desc"

    employee_id = fields.Many2one("hr.employee", required=True, string="Empleado")
    tipo_id = fields.Many2one("remu.conf.ausencia.tipo", required=True, string="Tipo")
    date_from = fields.Datetime(required=True)
    date_to = fields.Datetime(required=True)
    justificante = fields.Binary(string="Adjunto justificante")
    justificante_filename = fields.Char()
    notes = fields.Text()
    state = fields.Selection(
        [("draft", "Borrador"), ("approved", "Aprobado"), ("rejected", "Rechazado")],
        default="draft"
    )
