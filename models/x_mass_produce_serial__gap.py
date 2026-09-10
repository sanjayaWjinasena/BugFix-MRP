# -*- coding: utf-8 -*-
from odoo import models, fields

class XMassProduceSerialGap(models.Model):
    _inherit = 'x_mass_produce_serial_'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
