# -*- coding: utf-8 -*-

from odoo import models, fields, api


class trail_4(models.Model):
    _name = 'trail_4.trail_4'
    _description = 'trail_4.trail_4'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    dhruvil = fields.Integer()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
