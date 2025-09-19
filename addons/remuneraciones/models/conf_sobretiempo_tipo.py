# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuConfSobretiempoTipo(models.Model):
    _name = "remu.conf.sobretiempo.tipo"
    _description = "Tipos de Sobretiempo"

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    factor = fields.Float(string="Factor (%)", help="Porcentaje sobre valor hora, p.ej. 50, 100")
    requiere_aprobacion = fields.Boolean(default=True)
    activo = fields.Boolean(default=True)
