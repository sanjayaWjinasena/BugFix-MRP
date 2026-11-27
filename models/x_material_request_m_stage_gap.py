# -*- coding: utf-8 -*-
from odoo import models, fields

class XMaterialRequestMStageGap(models.Model):
    _inherit = 'x_material_request_m_stage'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_name = fields.Char(string='Stage Name', required=True)
