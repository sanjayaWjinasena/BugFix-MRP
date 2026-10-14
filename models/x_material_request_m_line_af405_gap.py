from odoo import fields, models


class XMaterialRequestMLineAf405Gap(models.Model):
    _inherit = 'x_material_request_m_line_af405'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_material_request_m_id = fields.Many2one(comodel_name='x_material_request_m')
    x_name = fields.Char(string='Description', required=True)
