# -*- coding: utf-8 -*-
from odoo import fields, models


class MrpEco(models.Model):
    _inherit = 'mrp.eco'

    x_studio_item_approved = fields.Boolean(string='Approved Item')
    x_studio_error = fields.Char(string='Error', copy=True)
    x_studio_tag_description = fields.Char(string='Tag Description', copy=True)
