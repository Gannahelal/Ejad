from odoo import models, fields, api
from odoo.exceptions import ValidationError

class OwnProduct(models.Model):
    _name = 'openaacc.ownproduct'


    price = fields.Float('Price')
    quantity = fields.Float('Quantity')
    total_amount = fields.Float('Total Amount', compute='_compute_total_amount', store=True)

    @api.onchange('price', 'quantity')
    def _onchange_price_quantity(self):
        self.total_amount = self.price * self.quantity

    @api.depends('price', 'quantity')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = record.price * record.quantity

    @api.constrains('quantity')
    def _check_quantity(self):
        for record in self:
            if record.quantity < 1:
                raise ValidationError('Quantity must be a positive number.')