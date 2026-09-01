# -*- coding: utf-8 -*-
from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_current_user = fields.Many2one('res.users', string='Current User', readonly=True)
    x_studio_direct_general_cost = fields.One2many(
        'x_mrp_bom_general_cost', 'x_studio_prod_bom_general_cost_ids',
        string='Direct General Cost')
    x_studio_direct_material_cost = fields.One2many(
        'x_mrp_bom_material_cos', 'x_studio_prod_bom_material_cost_ids',
        string='Direct Material Cost')
    x_studio_finished_product_location = fields.Many2one('stock.location', string='Finished Product Location')
    x_studio_finished_products_location_updated = fields.Boolean(string='Finished Products Location Updated')
    x_studio_grand_total_actual_cost_1 = fields.Float(string='Grand Total (Actual Cost)', readonly=True)
    x_studio_grand_total_planned_cost = fields.Float(string='Grand Total (Planned Cost)', readonly=True)
    x_studio_mark_as_done_validation = fields.Text(string='Mark as Done Validation')
    x_studio_mass_produced = fields.Boolean(string='Mass Produced')
    x_studio_melt_item = fields.Boolean(string='Melt Item', readonly=True)
    x_studio_one2many_field_Fzcvl = fields.One2many(
        'x_mrp_bom_labour_cost', 'x_studio_prod_bom_labour_cost_ids',
        string='Direct Labour Cost')
    x_studio_one2many_field_vg1OS = fields.One2many(
        'x_mrp_bom_overhead_cos', 'x_studio_prod_bom_overhead_cost_ids',
        string='Direct Overhead Cost')
    x_studio_original_mo = fields.Char(string='Original MO')
    x_studio_ot_applicable = fields.Boolean(string='OT  Applicable', readonly=True, store=False)
    x_studio_pro_bom_total_general_cost = fields.Float(string='Total General Cost', readonly=True)
    x_studio_process_error = fields.Text(string='Process Error')
    x_studio_prod_bom_total_actual_labour_cost = fields.Float(string='Total Actual Labour Cost', readonly=True)
    x_studio_prod_bom_total_actual_labour_cost_ot = fields.Float(string='Total Actual Labour Cost (OT)', readonly=True)
    x_studio_prod_bom_total_actual_labour_cost_without_ot = fields.Float(string='Total Actual Labour Cost (Without OT)', readonly=True)
    x_studio_prod_bom_total_actual_material_cost = fields.Float(string='Total  Actual Material Cost', readonly=True)
    x_studio_prod_bom_total_actual_overhead_cost = fields.Float(string='Total Actual Overhead Cost', readonly=True)
    x_studio_prod_bom_total_labour_cost = fields.Float(string='Total Labour Cost', readonly=True)
    x_studio_prod_bom_total_material_cost = fields.Float(string='Total Material Cost', readonly=True)
    x_studio_prod_bom_total_overhead_cost = fields.Float(string='Total Overhead Cost', readonly=True)
    x_studio_quantity_validation = fields.Boolean(string='Quantity Validation', readonly=True, store=False)
    x_studio_report_type_m_wip = fields.Many2one('x_sales_report_type', string='Report Type (M-WIP)')
    x_studio_serial_cancelled = fields.Boolean(string='Serial Cancelled')
    x_studio_source_validate = fields.Boolean(string='Source Validate', readonly=True, store=False)
    x_studio_super_user = fields.Boolean(string='Super User', readonly=True, store=False)
    x_studio_super_user_melt_items = fields.Boolean(string='Super User (Melt Items)', readonly=True)
    x_studio_temp_location = fields.Boolean(string='Temp Location', readonly=True)
    x_studio_total_actual_general_cost = fields.Float(string='Total Actual General Cost', readonly=True)
    x_studio_tracked_item = fields.Boolean(string='Tracked Item', readonly=True, store=False)
