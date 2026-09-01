# -*- coding: utf-8 -*-
"""x_material_request_m_line_af405 - line rows for x_material_request_m.

Studio-created custom model. Very small (3 fields, 0 rows on Clear-DB).
Referenced only by the primary form view for x_material_request_m
(Clear-DB view 8745) which BugFix-MRP has not ported yet. Porting the
model unblocks:
  * Uncommenting the x_material_request_m_line_ids_af086 One2many on
    x_material_request_m (was TODO on-disk pending inverse discovery).
  * Future port of view 8745.
"""
from odoo import fields, models


class XMaterialRequestMLineAf405(models.Model):
    _name = 'x_material_request_m_line_af405'
    _description = 'material_request_m_line'
    _order = 'x_studio_sequence asc, id asc'
    _rec_name = 'x_name'

    x_name = fields.Char(string='Description')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_material_request_m_id = fields.Many2one(
        'x_material_request_m',
        string='X Material Request M',
        ondelete='set null',
    )
