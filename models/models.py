from odoo import models, fields, api

class Employees(models.Model):
    _name = 'spoints.employees'

    name = fields.Char()