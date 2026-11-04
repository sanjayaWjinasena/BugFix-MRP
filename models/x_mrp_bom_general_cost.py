from odoo import fields, models


class XMrpBomGeneralCost(models.Model):
    """Studio custom model x_mrp_bom_general_cost.
    Direct general cost line for BOM + production order costing.
    Referenced by mrp.bom O2M x_studio_direct_general_cost and
    mrp.production O2M x_studio_direct_general_cost."""

    _name = "x_mrp_bom_general_cost"
    _inherit = ["mail.activity.mixin"]
    _description = "mrp.bom.general.cost"
    _rec_name = "name"
    _order = "sequence asc, id asc"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    x_studio_actual_qty = fields.Float(string="Actual Hour")
    x_studio_bom_general_cost_ids = fields.Many2one(
        "mrp.bom", string="BOM General Cost", ondelete="set null"
    )
    x_studio_cost = fields.Float(string="Cost/Hour")
    x_studio_currency_id = fields.Many2one("res.currency", string="Currency")
    x_studio_operation_id = fields.Many2one(
        "mrp.routing.workcenter", string="Operation", ondelete="cascade"
    )
    x_studio_planned_qty = fields.Float(string="Planned Hour")
    x_studio_prod_bom_general_cost_ids = fields.Many2one(
        "mrp.production", string="Prod. BOM General Cost", ondelete="set null"
    )
    x_studio_prod_bom_line_id = fields.Many2one(
        "mrp.workorder", string="Prod. BOM Line ID", ondelete="cascade"
    )
    sequence = fields.Integer(string="Sequence")
    x_studio_total_actual_cost = fields.Float(string="Total Actual Cost")
    x_studio_total_cost = fields.Float(string="Total Cost")


class XMrpBomGeneralCostGap(models.Model):
    _inherit = "x_mrp_bom_general_cost"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
