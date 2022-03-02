# -*- coding: utf-8 -*-

from odoo import models, fields, api


class school(models.Model):
    _name = 'school.school'
    _description = 'school.school'
    school_id=fields.Integer(string="ID")
    name = fields.Char()
    departments_id_1=fields.Many2many("department.department",string="Department")
    courses_id_1=fields.Many2many(string="Course",related="departments_id_1.courses_id")
