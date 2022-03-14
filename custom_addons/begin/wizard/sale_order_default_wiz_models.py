from odoo import models, fields, api


class SaleOrderDefaultWiz(models.TransientModel):
    _name = "default.wiz"
    _inherit = 'sale.order'

    customer = fields.Char()
    cus_email = fields.Char()
    sale_person = fields.Char()
    sale_person_contact = fields.Char()
    payment_terms = fields.Char()

    @api.model
    def default_get(self, vals):
        res = super(SaleOrderDefaultWiz, self).default_get(vals)
        if res.get('is_mostafeed', False):
            vals = [(0, 0, {'outcome_amount': 900, 'type': asha}),
                    (0, 0, {'outcome_amount': 150, 'type': kesaa}),
                    (0, 0, {'outcome_amount': 140, 'type': water})]
            res.update({'outcomes': vals})