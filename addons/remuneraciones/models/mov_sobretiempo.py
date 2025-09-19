# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuMovSobretiempo(models.Model):
    _name = "remu.mov.sobretiempo"
    _description = "Movimientos de Sobretiempo"
    _order = "date desc"

    employee_id = fields.Many2one("hr.employee", required=True, string="Empleado")
    tipo_id = fields.Many2one("remu.conf.sobretiempo.tipo", required=True, string="Tipo")
    date = fields.Date(required=True)
    hours = fields.Float(string="Horas", required=True)
    factor = fields.Float(string="Factor (%)", related="tipo_id.factor", store=True)
    notes = fields.Text()
    approved = fields.Boolean(string="Aprobado", default=False)
