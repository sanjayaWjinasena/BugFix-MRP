from odoo import fields, models


class XMrpBomGeneralCost(models.Model):
    """Studio custom model mrp_bom_general_cost.
    Direct general cost line for BOM + production order costing.
    Referenced by mrp.bom O2M direct_general_cost and
    mrp.production O2M direct_general_cost."""

    _name = "mrp_bom_general_cost"
    _inherit = ["mail.activity.mixin"]
    _description = "mrp.bom.general.cost"
    _rec_name = "name"
    _order = "sequence asc, id asc"

    active = fields.Boolean(default=True)
    name = fields.Char()
    actual_qty = fields.Float(string="Actual Hour")
    bom_general_cost_ids = fields.Many2one(
        "mrp.bom", string="BOM General Cost", ondelete="set null"
    )
    cost = fields.Float(string="Cost/Hour")
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    operation_id = fields.Many2one("mrp.routing.workcenter", ondelete="cascade")
    planned_qty = fields.Float(string="Planned Hour")
    prod_bom_general_cost_ids = fields.Many2one(
        "mrp.production", string="Prod. BOM General Cost", ondelete="set null"
    )
    prod_bom_line_id = fields.Many2one(
        "mrp.workorder", string="Prod. BOM Line ID", ondelete="cascade"
    )
    sequence = fields.Integer()
    total_actual_cost = fields.Float()
    total_cost = fields.Float()


class XMrpBomGeneralCostGap(models.Model):
    _inherit = "mrp_bom_general_cost"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
