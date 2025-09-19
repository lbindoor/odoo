# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuAfp(models.Model):
    _name = "remu.afp"
    _description = "AFP"
    _rec_name = "name"

    name = fields.Char(required=True)
    code = fields.Char(string="Código", required=True)
    vat = fields.Char(string="RUT")
    tasa_trabajador = fields.Float(string="Tasa Trabajador (%)")
    tasa_empleador = fields.Float(string="Tasa Empleador (%)")
    tasa_sis = fields.Float(string="SIS (%)")
    active = fields.Boolean(default=True)
