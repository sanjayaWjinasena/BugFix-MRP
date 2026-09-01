# -*- coding: utf-8 -*-
from odoo import fields, models


class XMrpBomMaterialCos(models.Model):
    """Studio custom model x_mrp_bom_material_cos (24-char truncated 'cost').
    Direct material cost line for BOM + production order costing.
    Referenced by mrp.bom O2M x_studio_one2many_field_4rhw9 and
    mrp.production O2M x_studio_direct_material_cost."""
    _name = 'x_mrp_bom_material_cos'
    _description = 'mrp.bom.material.cost'
    _rec_name = 'x_name'
    _order = 'x_studio_sequence asc, id asc'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_actual_qty = fields.Float(string='Actual Qty')
    x_studio_bom_line_id = fields.Many2one('mrp.bom.line', string='BOM Line', ondelete='set null')
    x_studio_bom_material_cost_ids = fields.Many2one('mrp.bom', string='BOM Material Cost', ondelete='cascade')
    x_studio_cost = fields.Float(string='Cost/Unit')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_line_id = fields.Many2one('mrp.bom.line', string='BOM Line ID', ondelete='set null')
    x_studio_operation_id = fields.Many2one('mrp.routing.workcenter', string='Operation', ondelete='set null')
    x_studio_planned_qty = fields.Float(string='Planned Qty')
    x_studio_prod_bom_line_id = fields.Many2one('stock.move', string='Prod. BOM Line ID', ondelete='set null')
    x_studio_prod_bom_material_cost_ids = fields.Many2one('mrp.production', string='Prod. BOM Material Cost', ondelete='cascade')
    x_studio_product_id = fields.Many2one('product.product', string='Product', ondelete='set null')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_total_actual_cost = fields.Float(string='Total Actual Cost')
    x_studio_total_cost = fields.Float(string='Total Cost')
    x_studio_uom_id = fields.Many2one('uom.uom', string='UOM', ondelete='set null')
