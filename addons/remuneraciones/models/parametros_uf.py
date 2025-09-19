# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuParamUF(models.Model):
    _name = "remu.param.uf"
    _description = "Parámetro UF diaria"

    date = fields.Date(required=True, index=True)
    value = fields.Monetary(string="UF", required=True, currency_field="currency_id")
    currency_id = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id.id)

    _sql_constraints = [
        ("uniq_uf_date", "unique(date)", "La fecha de UF debe ser única."),
    ]
