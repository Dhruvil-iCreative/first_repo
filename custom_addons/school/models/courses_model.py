from odoo import models, fields, api


class courses(models.Model):
    _name = 'courses.courses'

    course_id = fields.Integer()
    name = fields.Char()
    duration = fields.Integer()
    description = fields.Text()
    fees = fields.Integer()

    # @api.depends('duration')
    # def _value_pc(self):
    #     for record in self:
    #         record.duration_1 = int(record.duration)+"months"
