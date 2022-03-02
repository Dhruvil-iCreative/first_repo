from odoo import models, fields, api


class professor(models.Model):
    _name = 'professor.professor'

    name=fields.Char(string="Professor Name")
    age=fields.Integer()
    specialization_course_id=fields.Many2one('courses.courses',string="Specialization")
    experience=fields.Integer()
    online=fields.Boolean('Teaches Online??')

