from odoo import fields, models


class XMrpBomOverheadCos(models.Model):
    """Studio custom model mrp_bom_overhead_cos (24-char truncated 'cost').
    Direct overhead cost line for BOM + production order costing.
    Referenced by mrp.bom O2M one2many_field_bOopH and
    mrp.production O2M one2many_field_vg1OS."""

    _name = "mrp_bom_overhead_cos"
    _inherit = ["mail.activity.mixin"]
    _description = "mrp.bom.overhead.cost"
    _rec_name = "name"
    _order = "sequence asc, id asc"

    active = fields.Boolean(default=True)
    name = fields.Char()
    actual_qty = fields.Float(string="Actual Hour")
    bom_overhead_cost_ids = fields.Many2one(
        "mrp.bom", string="BOM Overhead Cost", ondelete="set null"
    )
    cost = fields.Float(string="Cost/Hour")
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    operation_id = fields.Many2one("mrp.routing.workcenter", ondelete="cascade")
    planned_qty = fields.Float(string="Planned Hour")
    prod_bom_line_id = fields.Many2one(
        "mrp.workorder", string="Prod. BOM Line ID", ondelete="cascade"
    )
    prod_bom_overhead_cost_ids = fields.Many2one(
        "mrp.production", string="Prod. BOM Overhead Cost", ondelete="set null"
    )
    sequence = fields.Integer()
    total_actual_cost = fields.Float()
    total_cost = fields.Float()


class XMrpBomOverheadCosGap(models.Model):
    _inherit = "mrp_bom_overhead_cos"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
