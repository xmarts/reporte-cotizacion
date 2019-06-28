# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReportCot(models.Model):
	_inherit = "sale.order"
	#nuevo
	proyecto = fields.Char(string="Proyecto")
	observaciones =fields.Text(string="Observaciones")
	#
	cargo_envio = fields.Char(string="Cargo por envio")
	instalacion = fields.Char(string="Instalacion")
	tiempo_entrega = fields.Char(string="Tiempo de entrega")
	forma_pago = fields.Char(string="Forma de pago")
	#------------------------------------------------------#
	pago_importacion = fields.Char(string="En los productos de importacion y fabricacion el pago sera")
	tiempo_entrega = fields.Char(string="Tiempo de entrega")
	nota_venta = fields.Char(string="Nota", default="Precios sujetos a cambio sin previo aviso")


class ReportCot(models.Model):
	_inherit = "sale.order.line"

	tiempo_entrega = fields.Char(string="Tiempo de entrega")
	price_product_cantidad = fields.Monetary(compute='_compute_product_cantidad', string='Subtotal', readonly=True, store=True)

	@api.depends('price_unit', 'product_uom_qty')
	def _compute_product_cantidad(self):
		for line in self:
			line.price_product_cantidad = line.product_uom_qty * line.price_unit