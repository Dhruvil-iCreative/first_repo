from odoo import models, fields, api


class RentalTypeWiz(models.TransientModel):
    _name = "rental.type.wiz"
    # _inherit = "rental.type"
    _description = 'rental.type.wiz'

    name = fields.Char(required=True)
    code = fields.Integer()
    description = fields.Text()

    @api.model
    def create(self, vals):
        # rtn = super(RentalType, self).create(vals)
        rtn = self.env['rental.type'].create(vals)
        return rtn
