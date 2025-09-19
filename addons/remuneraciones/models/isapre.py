# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuIsapre(models.Model):
    _name = "remu.isapre"
    _description = "Isapre"
    _rec_name = "name"

    name = fields.Char(required=True)
    code = fields.Char(string="Código", required=True)
    vat = fields.Char(string="RUT")
    precio_plan = fields.Monetary(string="Precio Plan (UF)", currency_field="currency_id")
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id.id)
    active = fields.Boolean(default=True)
