# -*- coding: utf-8 -*-
from odoo import fields, models


class XMrpBomLabourCost(models.Model):
    """Studio custom model x_mrp_bom_labour_cost.
    Direct labour cost line for BOM + production order costing.
    Includes OT (overtime) breakdown fields.
    Referenced by mrp.bom O2M x_studio_one2many_field_jPlQP and
    mrp.production O2M x_studio_one2many_field_Fzcvl."""
    _name = 'x_mrp_bom_labour_cost'
    _description = 'mrp.bom.labour.cost'
    _rec_name = 'x_name'
    _order = 'x_studio_sequence asc, id asc'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Name')
    x_studio_actual_qty = fields.Float(string='Actual Hour')
    x_studio_bom_labour_cost_ids = fields.Many2one('mrp.bom', string='BOM Labour Cost', ondelete='cascade')
    x_studio_cost = fields.Float(string='Cost/Hour')
    x_studio_cost_ot = fields.Float(string='Cost/Hour(OT)')
    x_studio_cost_without_ot = fields.Float(string='Cost/Hour(Labour Cost)')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_operation_id = fields.Many2one('mrp.routing.workcenter', string='Operation', ondelete='set null')
    x_studio_planned_qty = fields.Float(string='Planned Hour')
    x_studio_prod_bom_labour_cost_ids = fields.Many2one('mrp.production', string='Prod. BOM Labour Cost', ondelete='cascade')
    x_studio_prod_bom_line_id = fields.Many2one('mrp.workorder', string='Prod. BOM Line ID', ondelete='set null')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_total_actual_cost = fields.Float(string='Total Actual Cost')
    x_studio_total_actual_cost_ot = fields.Float(string='Total Actual Cost (OT)')
    x_studio_total_actual_cost_without_ot = fields.Float(string='Total Actual Cost (Labour Cost)')
    x_studio_total_cost = fields.Float(string='Total Cost')
