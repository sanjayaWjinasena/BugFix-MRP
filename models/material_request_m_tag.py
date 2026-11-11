"""Sentinel declaration for material_request_m_tag so cross-references resolve."""

from odoo import fields, models


class XMaterialRequestMTag(models.Model):
    _name = "material_request_m_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Material Request M Tags"

    color = fields.Integer(string="Color")
    name = fields.Char(string="Name")


class XMaterialRequestMTagGap(models.Model):
    _inherit = "material_request_m_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    color = fields.Integer(string="Color")
    name = fields.Char(string="Name", required=True)
