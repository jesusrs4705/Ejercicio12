from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    notes = fields.Text(string='Notes')

    def _action_confirm(self):
        res = super()._action_confirm()
        for order in self:
            order.picking_ids.write({'notes': order.notes})
        return res