# -*- coding: utf-8 -*-
from odoo import fields, models


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    x_studio_bom_total_general_cost = fields.Float(string='Total General Cost', readonly=True, store=False)
    x_studio_bom_total_labour_cost = fields.Float(string='Total Labour Cost', readonly=True, store=False)
    x_studio_bom_total_material_cost = fields.Float(string='Total Material Cost', readonly=True)
    x_studio_bom_total_overhead_cost = fields.Float(string='Total Overhead Cost', readonly=True, store=False)
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    # TODO: x_studio_direct_general_cost = fields.One2many(...) -- Studio inverse name unknown; port from Clear-DB manually.
    x_studio_last_updated_date_cost = fields.Datetime(string='Last Updated Date (Cost)')
    # TODO: x_studio_one2many_field_4rhw9 = fields.One2many(...) -- Studio inverse name unknown; port from Clear-DB manually.
    # TODO: x_studio_one2many_field_bOopH = fields.One2many(...) -- Studio inverse name unknown; port from Clear-DB manually.
    # TODO: x_studio_one2many_field_jPlQP = fields.One2many(...) -- Studio inverse name unknown; port from Clear-DB manually.
    x_studio_product_category = fields.Char(string='Product Category', readonly=True, store=False)
    x_studio_related_field_15j_1iv9vlere = fields.Char(string='New Related Field', readonly=True, store=False)
