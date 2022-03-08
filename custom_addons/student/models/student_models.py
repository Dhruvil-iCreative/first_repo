# -*- coding: utf-8 -*-

from odoo import models, fields, api


class student(models.Model):
    _name = 'student.student'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'student.student'
    _rec_name="fname"


    fname = fields.Char()
    lname = fields.Char()
    image = fields.Binary()
    mobile = fields.Char()
    email = fields.Char()
    gender = fields.Selection([('m', "Male"), ("f", "Female"), ("o", "Other")])
    city = fields.Selection([("a", "Ahmedabad"), ("b", "Baroda"), ("r", "Rajkot"), ("s", "Surat")])
    school_id = fields.Many2one(comodel_name="school.school",string="School")
    departments_ids = fields.Many2many(string="Department",related="school_id.departments_ids")
    courses_ids = fields.Many2many(string="Courses",related="departments_ids.courses_ids")
    appointment_id = fields.One2many('appointment.appointment','student_id',string="Appointment")
    task_ids = fields.Many2many("tasks.tasks",string="Task Checklist")
    checklist_progress = fields.Float(compute="tasks_progress",string="Progress",store=True,default=0.0)
    tod = fields.Datetime(comodel_name='Date current action', default=lambda self: fields.Datetime.now(), string="Apply On")

    @api.depends('task_ids')
    def tasks_progress(self):
        '''return the value of the progress done after clicking the checkboxes'''
        for rec in self:
            total_len = self.env['tasks.tasks'].search_count([])
            check_list_len = len(rec.task_ids)
            if total_len != 0:
                rec.checklist_progress = (check_list_len*100)/total_len
