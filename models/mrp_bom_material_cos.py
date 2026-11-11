from odoo import fields, models


class XMrpBomMaterialCos(models.Model):
    """Studio custom model mrp_bom_material_cos (24-char truncated 'cost').
    Direct material cost line for BOM + production order costing.
    Referenced by mrp.bom O2M one2many_field_4rhw9 and
    mrp.production O2M direct_material_cost."""

    _name = "mrp_bom_material_cos"
    _inherit = ["mail.activity.mixin"]
    _description = "mrp.bom.material.cost"
    _rec_name = "name"
    _order = "sequence asc, id asc"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    actual_qty = fields.Float(string="Actual Qty")
    bom_line_id = fields.Many2one(
        "mrp.bom.line", string="BOM Line", ondelete="set null"
    )
    bom_material_cost_ids = fields.Many2one(
        "mrp.bom", string="BOM Material Cost", ondelete="set null"
    )
    cost = fields.Float(string="Cost/Unit")
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    line_id = fields.Many2one(
        "mrp.bom.line", string="BOM Line ID", ondelete="cascade"
    )
    operation_id = fields.Many2one(
        "mrp.routing.workcenter", string="Operation", ondelete="set null"
    )
    planned_qty = fields.Float(string="Planned Qty")
    prod_bom_line_id = fields.Many2one(
        "stock.move", string="Prod. BOM Line ID", ondelete="cascade"
    )
    prod_bom_material_cost_ids = fields.Many2one(
        "mrp.production", string="Prod. BOM Material Cost", ondelete="set null"
    )
    product_id = fields.Many2one(
        "product.product", string="Product", ondelete="set null"
    )
    sequence = fields.Integer(string="Sequence")
    total_actual_cost = fields.Float(string="Total Actual Cost")
    total_cost = fields.Float(string="Total Cost")
    uom_id = fields.Many2one("uom.uom", string="UOM", ondelete="set null")


class XMrpBomMaterialCosGap(models.Model):
    _inherit = "mrp_bom_material_cos"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
