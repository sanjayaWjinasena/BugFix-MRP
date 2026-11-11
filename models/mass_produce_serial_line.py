from odoo import fields, models


class XMassProduceSerialLine(models.Model):
    """Studio wizard model mass_produce_serial_ (Studio truncated name
    with trailing underscore -- was 'x_mass_produce_serial_line' but hit
    the 24-char model-name limit). Line records for the parent
    mass_produce_serial wizard."""

    _name = "mass_produce_serial_"
    _inherit = ["mail.activity.mixin"]
    _description = "Mass Produce Serial Line"
    _rec_name = "name"
    _order = "sequence asc, id asc"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    lot_serial_id = fields.Many2one(
        "stock.lot", string="Lot/Serial Number", ondelete="set null"
    )
    lotserial_number = fields.Char(string="Lot/Serial Number")
    mass_produce_serial_ids = fields.Many2one(
        "mass_produce_serial", string="Mass Produce Serial", ondelete="cascade"
    )
    product_id = fields.Many2one(
        "product.product", string="Product", ondelete="set null"
    )
    product_qty = fields.Float(string="Quantity")
    product_uom_id = fields.Many2one(
        "uom.uom", string="Unit of Measure", ondelete="set null"
    )
    production_id = fields.Many2one(
        "mrp.production", string="Production Order", ondelete="set null"
    )
    production_order = fields.Char(string="Production Order")
    sequence = fields.Integer(string="Sequence")
    sequence_size = fields.Integer(string="Sequence Size")
    serial_no_prefix = fields.Char(string="Serial No Prefix")
    starting_no = fields.Char(string="Starting No")
    starting_serial_no = fields.Integer(string="Starting Serial No")
