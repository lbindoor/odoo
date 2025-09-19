# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuParamIngresoMinimo(models.Model):
    _name = "remu.param.ingreso.minimo"
    _description = "Ingreso Mínimo Vigente"

    date_from = fields.Date(string="Vigente desde", required=True)
    amount = fields.Monetary(string="Monto", required=True, currency_field="currency_id")
    currency_id = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id.id)
