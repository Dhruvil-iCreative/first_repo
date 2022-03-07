# -*- coding: utf-8 -*-

from odoo import models, fields, api


class school(models.Model):
    _name = 'school.school'
    _description = 'school.school'
    school_id = fields.Integer(string="ID")
    name = fields.Char()
    departments_id_1 = fields.Many2many("department.department", string="Department")
    courses_id_1 = fields.Many2many(string="Course", compute="compute_courses_of_dept")
    # student_id=fields.One2many("student.student","school_id_1",string="Students")

    def compute_courses_of_dept(self):
        for rec in self:
            courses = self.env["department.department"].search([("courses_id", "=", )])
            self.courses_id_1 = courses
