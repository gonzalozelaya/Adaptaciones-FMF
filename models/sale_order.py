# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderOverride(models.Model):
    _inherit = 'sale.order'
    
    buy_note = fields.Char('Nota de compra')

    point_of_sale = fields.Selection(selection=[('6','6'),('7','7')])
    
    def action_confirm(self):
        # Llama al comportamiento estándar de confirmar la orden de venta
        res = super(SaleOrderOverride, self).action_confirm()
        
        # Itera sobre los albaranes relacionados a esta orden
        for picking in self.picking_ids:
            picking.buy_note = self.buy_note  # Copia el valor de buy_note

        return res
        
    def _prepare_invoice(self):
        """
        Sobreescribimos este método para copiar el campo buy_note a la factura.
        """
        invoice_vals = super(SaleOrderOverride, self)._prepare_invoice()
        
        # Copia el valor de buy_note a la factura
        invoice_vals['buy_note'] = self.buy_note
        
        return invoice_vals

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    buy_note = fields.Char('Nota de compra',readonly=True)


class AccountMove(models.Model):
    _inherit = 'account.move'

    buy_note = fields.Char('Nota de compra',readonly=True)

    

    
# class my_module(models.Model):
#     _name = 'my_module.my_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100