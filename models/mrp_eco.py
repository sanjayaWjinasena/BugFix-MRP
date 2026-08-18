# -*- coding: utf-8 -*-
from odoo import fields, models


class MrpEco(models.Model):
    _inherit = 'mrp.eco'

    x_eco_id_mrp_eco_bom_change_count = fields.Integer(string='Engineering Change count', store=False)
    x_studio_error = fields.Char(string='Error')
    x_studio_item_approved = fields.Boolean(string='Approved Item', readonly=True)
    x_studio_tag_description = fields.Char(string='Tag Description')
