from odoo import models, fields

class Tags(models.Model):
    _name = "company.tags"

    name = fields.Char()