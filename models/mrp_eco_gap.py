from odoo import fields, models


class MrpEcoGap(models.Model):
    _inherit = 'mrp.eco'

    x_eco_id_mrp_eco_bom_change_count = fields.Integer(string='Engineering Change count')
