from odoo import fields, models


class MrpWorkcenter(models.Model):
    _inherit = "mrp.workcenter"

    employee = fields.Many2one("hr.employee")
    employees = fields.Many2many(
        "hr.employee",
        "mrp_workcenter_x_studio_employees_rel",
        "mrp_id",
        "hr_employee_id",
    )
    general_cost_hour = fields.Float(
        string="Equipment Actual Cost per Hour", readonly=True, store=False
    )
    labour_cost_hour = fields.Float(
        string="Labour Cost per Hour", readonly=True, store=False
    )
    labour_idle_cost_per_hour = fields.Float(readonly=True, store=False)
    many2many_field_j1rG7 = fields.Many2many(
        "res.users",
        "mrp_workcenter_x_studio_many2many_field_j1rG7_rel",
        "mrp_id",
        "res_users_id",
        string="Users",
    )
    ot_cost_per_hour = fields.Float(
        string="OT Cost per Hour", readonly=True, store=False
    )
    overhead_cost_hour = fields.Float(string="Overhead Cost per Hour")
