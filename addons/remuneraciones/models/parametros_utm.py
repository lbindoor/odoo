# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuParamUTM(models.Model):
    _name = "remu.param.utm"
    _description = "Parámetro UTM mensual"

    year = fields.Integer(required=True)
    month = fields.Selection([(str(i), str(i)) for i in range(1,13)], string="Mes", required=True)
    value = fields.Monetary(string="UTM", required=True, currency_field="currency_id")
    currency_id = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id.id)

    _sql_constraints = [
        ("uniq_utm_period", "unique(year, month)", "El período (año/mes) de UTM debe ser único."),
    ]
