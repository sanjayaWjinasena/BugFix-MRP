# -*- coding: utf-8 -*-
from odoo import fields, models


class MrpWorkcenterProductivity(models.Model):
    _inherit = 'mrp.workcenter.productivity'

    x_studio_employee = fields.Many2one('hr.employee', string='Employee')
