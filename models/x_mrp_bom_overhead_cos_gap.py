# -*- coding: utf-8 -*-
from odoo import models, fields

class XMrpBomOverheadCosGap(models.Model):
    _inherit = 'x_mrp_bom_overhead_cos'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
