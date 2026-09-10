# -*- coding: utf-8 -*-
from odoo import models, fields

class MrpEcoGap(models.Model):
    _inherit = 'mrp.eco'

    x_eco_id_mrp_eco_bom_change_count = fields.Integer(string='Engineering Change count')
