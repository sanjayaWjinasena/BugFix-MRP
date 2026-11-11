from odoo import fields, models


class MrpWorkorder(models.Model):
    _inherit = "mrp.workorder"

    original_mo = fields.Char(string="Original MO")
    ot_applicable = fields.Boolean(string="OT Applicable")
