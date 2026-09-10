# -*- coding: utf-8 -*-
from odoo import models, fields

class XMaterialRequestMGap(models.Model):
    _inherit = 'x_material_request_m'

    x_active = fields.Boolean(string='Active')
    x_color = fields.Integer(string='Color')
    x_material_request_m_line_ids_af086 = fields.One2many(comodel_name='x_material_request_m_line_af405', inverse_name='x_material_request_m_id', string='New Lines')
    x_name = fields.Char(string='Description', required=True)
