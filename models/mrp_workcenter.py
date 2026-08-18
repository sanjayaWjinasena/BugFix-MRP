# -*- coding: utf-8 -*-
from odoo import fields, models


class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    x_studio_employee = fields.Many2one('hr.employee', string='Employee')
    x_studio_employees = fields.Many2many('hr.employee', 'mrp_workcenter_x_studio_employees_rel', 'mrp_id', 'hr_employee_id', string='Employees')
    x_studio_general_cost_hour = fields.Float(string='Equipment Actual Cost per Hour', readonly=True, store=False)
    x_studio_labour_cost_hour = fields.Float(string='Labour Cost per Hour', readonly=True, store=False)
    x_studio_labour_idle_cost_per_hour = fields.Float(string='Labour Idle Cost Per Hour', readonly=True, store=False)
    x_studio_many2many_field_j1rG7 = fields.Many2many('res.users', 'mrp_workcenter_x_studio_many2many_field_j1rG7_rel', 'mrp_id', 'res_users_id', string='Users')
    x_studio_ot_cost_per_hour = fields.Float(string='OT Cost per Hour', readonly=True, store=False)
    x_studio_overhead_cost_hour = fields.Float(string='Overhead Cost per Hour')
