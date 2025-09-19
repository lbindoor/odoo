# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuParamTablaImpuestos(models.Model):
    _name = "remu.param.tabla.impuestos"
    _description = "Tabla de Impuesto Único (tramos)"

    tramo = fields.Integer(string="Tramo", required=True)
    desde = fields.Float(string="Desde (UTM)", required=True)
    hasta = fields.Float(string="Hasta (UTM)", required=True)
    tasa = fields.Float(string="Tasa (%)", required=True)
    rebaja = fields.Float(string="Rebaja (UTM)", required=True)
    vigente_desde = fields.Date(string="Vigente desde", required=True)
