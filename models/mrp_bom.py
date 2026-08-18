# -*- coding: utf-8 -*-
from odoo import fields, models


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    x_studio_bom_total_general_cost = fields.Float(string='Total General Cost', readonly=True, store=False)
    x_studio_bom_total_labour_cost = fields.Float(string='Total Labour Cost', readonly=True, store=False)
    x_studio_bom_total_material_cost = fields.Float(string='Total Material Cost', readonly=True)
    x_studio_bom_total_overhead_cost = fields.Float(string='Total Overhead Cost', readonly=True, store=False)
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_direct_general_cost = fields.One2many('x_mrp_bom_general_cost', 'TODO_inverse', string='Direct General Cost')
    x_studio_last_updated_date_cost = fields.Datetime(string='Last Updated Date (Cost)')
    x_studio_one2many_field_4rhw9 = fields.One2many('x_mrp_bom_material_cos', 'TODO_inverse', string='Direct Material Cost')
    x_studio_one2many_field_bOopH = fields.One2many('x_mrp_bom_overhead_cos', 'TODO_inverse', string='Direct Overhead Cost')
    x_studio_one2many_field_jPlQP = fields.One2many('x_mrp_bom_labour_cost', 'TODO_inverse', string='Direct Labour Cost')
    x_studio_product_category = fields.Char(string='Product Category', readonly=True, store=False)
    x_studio_related_field_15j_1iv9vlere = fields.Char(string='New Related Field', readonly=True, store=False)
