# -*- coding: utf-8 -*-
from odoo import fields, models


class XMrpBomOverheadCos(models.Model):
    """Studio custom model x_mrp_bom_overhead_cos (24-char truncated 'cost').
    Direct overhead cost line for BOM + production order costing.
    Referenced by mrp.bom O2M x_studio_one2many_field_bOopH and
    mrp.production O2M x_studio_one2many_field_vg1OS."""
    _name = 'x_mrp_bom_overhead_cos'
    _description = 'mrp.bom.overhead.cost'
    _rec_name = 'x_name'
    _order = 'x_studio_sequence asc, id asc'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_actual_qty = fields.Float(string='Actual Hour')
    x_studio_bom_overhead_cost_ids = fields.Many2one('mrp.bom', string='BOM Overhead Cost', ondelete='cascade')
    x_studio_cost = fields.Float(string='Cost/Hour')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_operation_id = fields.Many2one('mrp.routing.workcenter', string='Operation', ondelete='set null')
    x_studio_planned_qty = fields.Float(string='Planned Hour')
    x_studio_prod_bom_line_id = fields.Many2one('mrp.workorder', string='Prod. BOM Line ID', ondelete='set null')
    x_studio_prod_bom_overhead_cost_ids = fields.Many2one('mrp.production', string='Prod. BOM Overhead Cost', ondelete='cascade')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_total_actual_cost = fields.Float(string='Total Actual Cost')
    x_studio_total_cost = fields.Float(string='Total Cost')
