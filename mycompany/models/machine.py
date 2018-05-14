from odoo import models, fields


class Machine(models.Model):
    _name = "company.machine"

    name = fields.Char()
    picture = fields.Binary()

    tags = fields.Many2many('company.tags')

    approved = fields.Boolean()
    approved_by = fields.Many2one('res.users', 'Approved By', default=lambda self: self.env.uid)

    department_id = fields.Many2one('company.department')
