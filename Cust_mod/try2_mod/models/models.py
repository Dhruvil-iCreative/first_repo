# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class try2_mod(models.Model):
#     _name = 'try2_mod.try2_mod'
#     _description = 'try2_mod.try2_mod'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
