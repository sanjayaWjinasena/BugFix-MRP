# -*- coding: utf-8 -*-
"""Sentinel declaration for x_material_request_m_stage so cross-references resolve."""
from odoo import fields, models


class XMaterialRequestMStage(models.Model):
    _name = 'x_material_request_m_stage'
    _description = 'X Material Request M Stage'

    x_name = fields.Char(string='Stage Name')
    x_studio_sequence = fields.Integer(string='Sequence')
