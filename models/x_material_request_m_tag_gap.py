# -*- coding: utf-8 -*-
from odoo import models, fields

class XMaterialRequestMTagGap(models.Model):
    _inherit = 'x_material_request_m_tag'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Name', required=True)
