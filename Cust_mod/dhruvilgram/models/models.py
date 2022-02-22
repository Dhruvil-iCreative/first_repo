# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dhruvilgram(models.Model):
    _name = 'dhruvilgram.dhruvilgram'
    _description = 'dhruvilgram.dhruvilgram'

    name = fields.Char()
    age = fields.Integer()
    your_age = fields.Float(compute="_age_pc", store=True)
    description = fields.Text()
    city=fields.Selection([("ahm","Ahmedabad"),("raj","Rajkot"),("sur","Surat")])
    email=fields.Char()
    gender=fields.Selection([("m","Male"),("f","Female")])
    mobile=fields.Char()
    image=fields.Binary()

    @api.depends('age')
    def _age_pc(self):
        for record in self:
            record.your_age = float(record.age) 
