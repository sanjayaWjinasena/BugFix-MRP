# -*- coding: utf-8 -*-
from odoo import models, fields

class XMrpBomGeneralCostGap(models.Model):
    _inherit = 'x_mrp_bom_general_cost'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
