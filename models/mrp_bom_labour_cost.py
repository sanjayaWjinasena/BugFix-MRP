from odoo import fields, models


class XMrpBomLabourCost(models.Model):
    """Studio custom model mrp_bom_labour_cost.
    Direct labour cost line for BOM + production order costing.
    Includes OT (overtime) breakdown fields.
    Referenced by mrp.bom O2M one2many_field_jPlQP and
    mrp.production O2M one2many_field_Fzcvl."""

    _name = "mrp_bom_labour_cost"
    _inherit = ["mail.activity.mixin"]
    _description = "mrp.bom.labour.cost"
    _rec_name = "name"
    _order = "sequence asc, id asc"

    active = fields.Boolean(default=True)
    name = fields.Char()
    actual_qty = fields.Float(string="Actual Hour")
    bom_labour_cost_ids = fields.Many2one(
        "mrp.bom", string="BOM Labour Cost", ondelete="set null"
    )
    cost = fields.Float(string="Cost/Hour")
    cost_ot = fields.Float(string="Cost/Hour(OT)")
    cost_without_ot = fields.Float(string="Cost/Hour(Labour Cost)")
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    operation_id = fields.Many2one("mrp.routing.workcenter", ondelete="cascade")
    planned_qty = fields.Float(string="Planned Hour")
    prod_bom_labour_cost_ids = fields.Many2one(
        "mrp.production", string="Prod. BOM Labour Cost", ondelete="set null"
    )
    prod_bom_line_id = fields.Many2one(
        "mrp.workorder", string="Prod. BOM Line ID", ondelete="cascade"
    )
    sequence = fields.Integer()
    total_actual_cost = fields.Float()
    total_actual_cost_ot = fields.Float(string="Total Actual Cost (OT)")
    total_actual_cost_without_ot = fields.Float(
        string="Total Actual Cost (Labour Cost)"
    )
    total_cost = fields.Float()


class XMrpBomLabourCostGap(models.Model):
    _inherit = "mrp_bom_labour_cost"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
