from odoo import models, fields, api


class appointments(models.Model):
    _name = 'appointment.appointment'

    date = fields.Datetime(string="Date&Time")
    prof_name = fields.Many2one('professor.professor', string="With")
    student_id = fields.Many2one('student.student', string="Students")