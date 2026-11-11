"""Sentinel declaration for material_request_m_stage so cross-references resolve."""

from odoo import fields, models


class XMaterialRequestMStage(models.Model):
    _name = "material_request_m_stage"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Material Request M Stages"

    name = fields.Char(string="Stage Name")
    sequence = fields.Integer(string="Sequence")


class XMaterialRequestMStageGap(models.Model):
    _inherit = "material_request_m_stage"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Stage Name", required=True)
