from odoo import models, fields


class Department(models.Model):
    _name = "company.department"

    name = fields.Char()
    no_of_machines = fields.Integer()
    machine_ids = fields.One2many('company.machine', 'department_id')
