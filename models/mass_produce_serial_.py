from odoo import fields, models


class XMassProduceSerialGap(models.Model):
    _inherit = "mass_produce_serial_"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
