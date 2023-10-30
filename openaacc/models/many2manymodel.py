from odoo import models, fields
class Project(models.Model):
    _name = 'openaacc.project'
    _description = 'Project'

    name = fields.Char(string='Name')
    employee_ids = fields.Many2many('openaacc.employee', string='Employees')
class Employee(models.Model):
    _name = 'openaacc.employee'
    _description = 'Employee'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    project_ids = fields.Many2many('openaacc.project', string='Projects')