# -*- coding: utf-8 -*-

from odoo import models, fields, api


class student(models.Model):
    _name = 'student.student'
    _description = 'student.student'
    _rec_name="fname"


    fname = fields.Char()
    lname = fields.Char()
    image = fields.Binary()
    mobile = fields.Char()
    email = fields.Char()
    gender = fields.Selection([('m', "Male"), ("f", "Female"), ("o", "Other")])
    city = fields.Selection([("a", "Ahmedabad"), ("b", "Baroda"), ("r", "Rajkot"), ("s", "Surat")])
    school_id_1=fields.Many2one(comodel_name="school.school",string="School")
    departmentss=fields.Many2many(string="Department",related="school_id_1.departments_id_1")
    coursess=fields.Many2many(string="Courses",related="departmentss.courses_id")
