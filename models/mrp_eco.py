# -*- coding: utf-8 -*-
from odoo import fields, models


class MrpEco(models.Model):
    _inherit = 'mrp.eco'

    x_studio_item_approved = fields.Boolean(string='Approved Item')
