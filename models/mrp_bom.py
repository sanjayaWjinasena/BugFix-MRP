from odoo import fields, models


class MrpBom(models.Model):
    _inherit = "mrp.bom"

    bom_total_general_cost = fields.Float(
        string="Total General Cost", readonly=True, store=False
    )
    bom_total_labour_cost = fields.Float(
        string="Total Labour Cost", readonly=True, store=False
    )
    bom_total_material_cost = fields.Float(string="Total Material Cost", readonly=True)
    bom_total_overhead_cost = fields.Float(
        string="Total Overhead Cost", readonly=True, store=False
    )
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    direct_general_cost = fields.One2many(
        "mrp_bom_general_cost",
        "bom_general_cost_ids",
    )
    last_updated_date_cost = fields.Datetime(string="Last Updated Date (Cost)")
    one2many_field_4rhw9 = fields.One2many(
        "mrp_bom_material_cos",
        "bom_material_cost_ids",
        string="Direct Material Cost",
    )
    one2many_field_bOopH = fields.One2many(
        "mrp_bom_overhead_cos",
        "bom_overhead_cost_ids",
        string="Direct Overhead Cost",
    )
    one2many_field_jPlQP = fields.One2many(
        "mrp_bom_labour_cost",
        "bom_labour_cost_ids",
        string="Direct Labour Cost",
    )
    product_category = fields.Char(readonly=True, store=False)
    related_field_15j_1iv9vlere = fields.Char(
        string="New Related Field", readonly=True, store=False
    )
