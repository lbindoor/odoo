# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuMovHaberDescuento(models.Model):
    _name = "remu.mov.haber.descuento"
    _description = "Movimientos de Haberes y Descuentos"
    _order = "date desc"

    employee_id = fields.Many2one("hr.employee", required=True, string="Empleado")
    concepto_id = fields.Many2one("remu.conf.concepto", required=True, string="Concepto")
    date = fields.Date(required=True)
    amount = fields.Monetary(required=True, currency_field="currency_id")
    currency_id = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id.id)
    notes = fields.Text()
    state = fields.Selection(
        [("draft", "Borrador"), ("approved", "Aprobado"), ("cancel", "Anulado")],
        default="draft"
    )
