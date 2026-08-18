# -*- coding: utf-8 -*-
"""Sentinel declaration for x_material_request_m_tag so cross-references resolve."""
from odoo import fields, models


class XMaterialRequestMTag(models.Model):
    _name = 'x_material_request_m_tag'
    _description = 'X Material Request M Tag'

    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Name')
