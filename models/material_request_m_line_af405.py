"""material_request_m_line_af405 - line rows for material_request_m.

Studio-created custom model. Very small (3 fields, 0 rows on Clear-DB).
Referenced only by the primary form view for material_request_m
(Clear-DB view 8745) which BugFix-MRP has not ported yet. Porting the
model unblocks:
  * Uncommenting the material_request_m_line_ids_af086 One2many on
    material_request_m (was TODO on-disk pending inverse discovery).
  * Future port of view 8745.
"""

from odoo import fields, models


class XMaterialRequestMLineAf405(models.Model):
    _name = "material_request_m_line_af405"
    _description = "material_request_m_line"
    _order = "sequence asc, id asc"
    _rec_name = "name"

    name = fields.Char(string="Description")
    sequence = fields.Integer()
    material_request_m_id = fields.Many2one(
        "material_request_m",
        ondelete="set null",
    )


class XMaterialRequestMLineAf405Gap(models.Model):
    _inherit = "material_request_m_line_af405"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    material_request_m_id = fields.Many2one(comodel_name="material_request_m")
    name = fields.Char(string="Description", required=True)
