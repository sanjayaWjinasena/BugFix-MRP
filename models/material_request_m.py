from odoo import fields, models


class XMaterialRequestM(models.Model):
    """Studio-ported custom model material_request_m."""

    _name = "material_request_m"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Material Request M"

    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    material_request_m_line_ids_af086 = fields.One2many(
        "material_request_m_line_af405",
        "material_request_m_id",
        string="New Lines",
    )
    name = fields.Char(string="Description", required=True)
    accounting_company_id = fields.Many2one("res.company", string="Company")
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    date = fields.Date(string="Date")
    date_start = fields.Datetime(string="Start Date")
    date_stop = fields.Datetime(string="End Date")
    image = fields.Binary(string="Image")
    kanban_state = fields.Selection(
        [("normal", "In Progress"), ("done", "Ready"), ("blocked", "Blocked")],
        string="Kanban State",
    )
    notes = fields.Html(string="Notes")
    partner_email = fields.Char(string="Email")
    partner_id = fields.Many2one("res.partner", string="Contact")
    partner_phone = fields.Char(string="Phone")
    custom_reports_priority = fields.Boolean(string="High Priority")
    sequence = fields.Integer(string="Sequence")
    stage_id = fields.Many2one(
        "material_request_m_stage", string="Stage", required=True
    )
    tag_ids = fields.Many2many(
        "material_request_m_tag",
        "x_material_request_m_x_studio_tag_ids_rel",
        "x_id",
        "x_material_request_m_tag_id",
        string="Tags",
    )
    user_id = fields.Many2one("res.users", string="Responsible")
    value = fields.Float(string="Value")  # was Monetary (no currency_field)


class XMaterialRequestMGap(models.Model):
    _inherit = "material_request_m"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    material_request_m_line_ids_af086 = fields.One2many(
        comodel_name="material_request_m_line_af405",
        inverse_name="material_request_m_id",
        string="New Lines",
    )
    name = fields.Char(string="Description", required=True)
