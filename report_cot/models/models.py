# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReportCot(models.Model):
	_inherit = "sale.order"

	cargo_envio = fields.Char(string="Cargo por envio")
	instalacion = fields.Char(string="Instalacion")
	tiempo_entrega = fields.Char(string="Tiempo de entrega")
	forma_pago = fields.Char(string="Forma de pago")
	#------------------------------------------------------#
	pago_importacion = fields.Char(string="En los productos de importacion y fabricacion el pago sera")
	tiempo_entrega = fields.Char(string="Tiempo de entrega")
	nota_venta = fields.Char(string="Nota", default="Precios sujetos a cambio sin previo aviso")