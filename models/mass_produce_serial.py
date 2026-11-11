from odoo import fields, models


class XMassProduceSerial(models.Model):
    """Studio wizard model mass_produce_serial.
    Parent record for mass-producing serial numbers on a production order.
    Opened as a transient-like popup from mrp.production 'Mass Produce Serial
    Nos' button (server action 1147). Generate/Clear/OK buttons on the primary
    form (view 2600) invoke server actions 1149/1150/1151."""

    _name = "mass_produce_serial"
    _inherit = ["mail.activity.mixin"]
    _description = "Mass Produce Serial"
    _rec_name = "name"
    _order = "sequence asc, id asc"

    active = fields.Boolean(default=True)
    name = fields.Char()
    accounting_company_id = fields.Many2one("res.company", string="Company")
    generated = fields.Boolean()
    last_serial_no_id = fields.Many2one(
        "stock.lot", string="Last Used Serial No", ondelete="set null"
    )
    mass_produce_serial_ids = fields.One2many(
        "mass_produce_serial_",
        "mass_produce_serial_ids",
        string="Serial No List",
    )
    prefix_status = fields.Selection([("New", "New"), ("Existing", "Existing")])
    product_id = fields.Many2one("product.product", ondelete="set null")
    product_qty = fields.Float(string="Quantity to Create")
    production_id = fields.Many2one(
        "mrp.production", string="Production Order", ondelete="set null"
    )
    sequence = fields.Integer()
    sequence_size = fields.Integer()
    serial_no_prefix = fields.Char()
    starting_serial_no = fields.Integer()


class XMassProduceSerialGap(models.Model):
    _inherit = "mass_produce_serial"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
