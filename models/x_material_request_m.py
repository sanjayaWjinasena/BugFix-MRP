# -*- coding: utf-8 -*-
from odoo import fields, models


class XMaterialRequestM(models.Model):
    """Studio-ported custom model x_material_request_m."""
    _name = 'x_material_request_m'
    _description = 'Material Request M'

    x_active = fields.Boolean(string='Active')
    x_color = fields.Integer(string='Color')
    x_material_request_m_line_ids_af086 = fields.One2many('x_material_request_m_line_af405', 'TODO_inverse', string='New Lines')
    x_name = fields.Char(string='Description', required=True)
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_date = fields.Date(string='Date')
    x_studio_date_start = fields.Datetime(string='Start Date')
    x_studio_date_stop = fields.Datetime(string='End Date')
    x_studio_image = fields.Binary(string='Image')
    x_studio_kanban_state = fields.Selection([], string='Kanban State')
    x_studio_notes = fields.Html(string='Notes')
    x_studio_partner_email = fields.Char(string='Email')
    x_studio_partner_id = fields.Many2one('res.partner', string='Contact')
    x_studio_partner_phone = fields.Char(string='Phone')
    x_studio_priority = fields.Boolean(string='High Priority')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_stage_id = fields.Many2one('x_material_request_m_stage', string='Stage', required=True)
    x_studio_tag_ids = fields.Many2many('x_material_request_m_tag', 'x_material_request_m_x_studio_tag_ids_rel', 'x_id', 'x_material_request_m_tag_id', string='Tags')
    x_studio_user_id = fields.Many2one('res.users', string='Responsible')
    x_studio_value = fields.Monetary(string='Value')
