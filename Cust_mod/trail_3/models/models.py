# -*- coding: utf-8 -*-

from odoo import models, fields, api


class trail_3(models.Model):
    _name = 'trail_3.trail_3'
    _description = 'trail_3.trail_3'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    city = fields.Selection([("ahm", 'Ahmedabad'), ("raj", 'Rajkot'), ("sur", 'Surat')])

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
