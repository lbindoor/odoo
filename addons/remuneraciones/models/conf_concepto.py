# -*- coding: utf-8 -*-
from odoo import models, fields

class RemuConfConcepto(models.Model):
    _name = "remu.conf.concepto"
    _description = "Conceptos de Haberes y Descuentos"

    # Encabezado
    code = fields.Char(string="Código", required=True)
    name = fields.Char(string="Descripción", required=True)
    nature = fields.Selection([("haber", "Haber"), ("descuento", "Descuento")],
                              string="Tipo de Concepto", required=True, default="haber")

    # Clasificación (izquierda)
    imponible = fields.Boolean(string="Imponible", default=True)
    tributa = fields.Boolean(string="Tributable", default=True)
    adicional_horas_extras = fields.Boolean(string="Adicional Horas Extras")
    reliquida_imp_unico = fields.Boolean(string="Reliquida Imp. Único")
    horas_extras = fields.Boolean(string="Horas Extras")
    adicional_sueldo_base = fields.Boolean(string="Adicional Sueldo Base")
    adicional_valor_dia_hora = fields.Boolean(string="Adicional Valor Día/Hora")
    renta_exenta = fields.Boolean(string="Renta Exenta")
    haber_variable_semana_corrida = fields.Boolean(string="Haber Variable Semana Corrida")
    cuota_reliquidacion_mes = fields.Boolean(string="Cuota de Reliquidación del Mes")

    # Características (derecha)
    class_type = fields.Selection([("variable", "Variable"), ("fijo", "Fijo")],
                                  string="Clase", required=True, default="variable")
    currency_type = fields.Selection([("CLP", "Pesos"), ("UF", "UF"), ("UTM", "UTM")],
                                     string="Tipo Moneda", required=True, default="CLP")
    amount_pesos = fields.Monetary(string="Monto en Pesos", currency_field="currency_id",
                                   help="Monto fijo en CLP si corresponde")
    dia_cambio = fields.Integer(string="Día Cambio", help="Día del mes en que cambia el valor si corresponde")
    campo_resultado = fields.Selection([("none","--------"), ("monto","Monto"),
                                        ("porcentaje","Porcentaje"), ("factor","Factor")],
                                       string="Campo Resultado", default="none")
    amount_other = fields.Float(string="Monto en Otra Moneda", help="Monto en UF/UTM según Tipo Moneda")
    porcentaje = fields.Float(string="Porcentaje")
    factor = fields.Float(string="Factor")
    currency_id = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id.id)

    # LRE y opciones
    lre_classification = fields.Selection([
        ("2113","Bonos u otras remun. variables mensuales o superiores a un mes (2113)"),
        ("1101","Sueldo Base (1101)"),
        ("2101","Gratificación (2101)"),
        ("3101","Descuento AFP/Salud (3101)"),
        ("9999","Otro (9999)"),
    ], string="Clasificación LRE", default="2113")
    exportable_lre = fields.Boolean(string="Exportable al Libro de Remuneracion Configurable", default=True)
    no_calcula_gratificacion = fields.Boolean(string="No incluir para calculo de gratificación")
    proporcional_dias = fields.Boolean(string="Proporcional a los días Trabajados")
    no_provision_anios_servicio = fields.Boolean(string="No incluir para cálculo de Provisión Años de Servicio")

    activo = fields.Boolean(string="Activo", default=True)
