# -*- coding: utf-8 -*-
from odoo import fields, models


class XMassProduceSerial(models.Model):
    """Studio wizard model x_mass_produce_serial.
    Parent record for mass-producing serial numbers on a production order.
    Opened as a transient-like popup from mrp.production 'Mass Produce Serial
    Nos' button (server action 1147). Generate/Clear/OK buttons on the primary
    form (view 2600) invoke server actions 1149/1150/1151."""
    _name = 'x_mass_produce_serial'
    _description = 'Mass Produce Serial'
    _rec_name = 'x_name'
    _order = 'x_studio_sequence asc, id asc'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_generated = fields.Boolean(string='Generated')
    x_studio_last_serial_no_id = fields.Many2one('stock.lot', string='Last Used Serial No', ondelete='set null')
    x_studio_mass_produce_serial_ids = fields.One2many(
        'x_mass_produce_serial_', 'x_studio_mass_produce_serial_ids',
        string='Serial No List')
    x_studio_prefix_status = fields.Selection(
        [('New', 'New'), ('Existing', 'Existing')],
        string='Prefix Status')
    x_studio_product_id = fields.Many2one('product.product', string='Product', ondelete='set null')
    x_studio_product_qty = fields.Float(string='Quantity to Create')
    x_studio_production_id = fields.Many2one('mrp.production', string='Production Order', ondelete='cascade')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_sequence_size = fields.Integer(string='Sequence Size')
    x_studio_serial_no_prefix = fields.Char(string='Serial No Prefix')
    x_studio_starting_serial_no = fields.Integer(string='Starting Serial No')
