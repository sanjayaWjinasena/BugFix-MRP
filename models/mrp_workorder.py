# -*- coding: utf-8 -*-
from odoo import fields, models


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    x_studio_original_mo = fields.Char(string='Original MO')
    x_studio_ot_applicable = fields.Boolean(string='OT Applicable')
