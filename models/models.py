from odoo import models, fields, api

class Employees(models.Model):
    _name = 'spoints.employees'

    name = fields.Char()
    biography = fields.Html()
    works_ids = fields.One2many('spoints.works', 'employee_id', string="Works")

class Works(models.Model):
    _name = 'spoints.works'
    _inherit = ['mail.thread']

    name = fields.Char()
    employee_id = fields.Many2one('spoints.employees', string="Employee")

