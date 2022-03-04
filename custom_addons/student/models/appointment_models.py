from odoo import models, fields, api


class appointments(models.Model):
    _name = 'appointment.appointment'

    date = fields.Datetime(string="Date&Time")
    prof_name = fields.Many2one('professor.professor', string="With")
    student_id = fields.Many2one('student.student', string="Students")
    emergency = fields.Selection([('y',"Yes"),('n',"NO")])
    emergency_1 = fields.Char(string="Is it emergency??", readonly=True)


    @api.onchange('emergency')
    def yes_no(self):
        for rec in self:
            if(rec.emergency):
                rec.emergency_1 = rec.emergency