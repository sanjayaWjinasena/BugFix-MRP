# -*- coding: utf-8 -*-
from odoo import fields, models


class XMassProduceSerialLine(models.Model):
    """Studio wizard model x_mass_produce_serial_ (Studio truncated name
    with trailing underscore -- was 'x_mass_produce_serial_line' but hit
    the 24-char model-name limit). Line records for the parent
    x_mass_produce_serial wizard."""
    _name = 'x_mass_produce_serial_'
    _description = 'Mass Produce Serial Line'
    _rec_name = 'x_name'
    _order = 'x_studio_sequence asc, id asc'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_lot_serial_id = fields.Many2one('stock.lot', string='Lot/Serial Number', ondelete='set null')
    x_studio_lotserial_number = fields.Char(string='Lot/Serial Number')
    x_studio_mass_produce_serial_ids = fields.Many2one(
        'x_mass_produce_serial', string='Mass Produce Serial',
        ondelete='cascade')
    x_studio_product_id = fields.Many2one('product.product', string='Product', ondelete='set null')
    x_studio_product_qty = fields.Float(string='Quantity')
    x_studio_product_uom_id = fields.Many2one('uom.uom', string='Unit of Measure', ondelete='set null')
    x_studio_production_id = fields.Many2one('mrp.production', string='Production Order', ondelete='set null')
    x_studio_production_order = fields.Char(string='Production Order')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_sequence_size = fields.Integer(string='Sequence Size')
    x_studio_serial_no_prefix = fields.Char(string='Serial No Prefix')
    x_studio_starting_no = fields.Char(string='Starting No')
    x_studio_starting_serial_no = fields.Integer(string='Starting Serial No')
