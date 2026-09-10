# -*- coding: utf-8 -*-
from odoo import models, fields

class XMaterialRequestMLineAf405Gap(models.Model):
    _inherit = 'x_material_request_m_line_af405'

    x_material_request_m_id = fields.Many2one(comodel_name='x_material_request_m', string='X Material Request M')
    x_name = fields.Char(string='Description', required=True)
