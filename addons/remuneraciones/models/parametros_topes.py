# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuParamTopes(models.Model):
    _name = "remu.param.topes"
    _description = "Topes previsionales/cesantía/salud"

    vigente_desde = fields.Date(required=True)
    tope_imponible = fields.Monetary(string="Tope Imponible", currency_field="currency_id")
    tope_salud = fields.Monetary(string="Tope Salud", currency_field="currency_id")
    tope_seguro_cesantia = fields.Monetary(string="Tope Seguro Cesantía", currency_field="currency_id")
    currency_id = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id.id)
