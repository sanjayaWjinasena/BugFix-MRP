from odoo import fields, models


class MrpEco(models.Model):
    _inherit = "mrp.eco"

    item_approved = fields.Boolean(string="Approved Item")
    error = fields.Char(string="Error", copy=True)
    tag_description = fields.Char(string="Tag Description", copy=True)


class MrpEcoGap(models.Model):
    _inherit = "mrp.eco"

    eco_id_mrp_eco_bom_change_count = fields.Integer(
        string="Engineering Change count"
    )
