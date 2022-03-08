from odoo import models, fields, api


class department(models.Model):
    _name = 'department.department'

    depart_id = fields.Integer()
    name = fields.Char()
    courses_ids = fields.Many2many(comodel_name="courses.courses", string="Course")
    classes = fields.Integer(string="NO.of Classes")
    floors = fields.Integer(string="No. of Floors")
    description = fields.Text()

