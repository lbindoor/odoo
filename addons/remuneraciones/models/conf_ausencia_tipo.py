# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuConfAusenciaTipo(models.Model):
    _name = "remu.conf.ausencia.tipo"
    _description = "Tipo de Ausencia"

    name = fields.Char(required=True)
    code = fields.Char(string="Código", required=True)
    requiere_justificacion = fields.Boolean(default=False)
    descuenta_remuneracion = fields.Boolean(default=False)
    activo = fields.Boolean(default=True)
