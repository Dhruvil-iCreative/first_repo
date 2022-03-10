from odoo import models, fields, api


class ContactImprove(models.Model):
    _inherit = ["res.partner"]

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s - %s' % (rec.name, rec.phone)))
            print(result)
        return result

    @api.model
    def name_search(self, name, operator='ilike'):
        domain = []
        if name:
            domain = ['|', '|', ('name', operator, name), ('email', operator, name)]
        return domain
