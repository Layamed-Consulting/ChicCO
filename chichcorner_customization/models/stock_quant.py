from odoo import models, fields, api,_
from odoo.exceptions import UserError

class StockQuant(models.Model):
    _inherit = "stock.quant"

    def action_print_label(self):
        label_layout = self.env['product.label.layout'].create({
            'print_format': '2x7xprice',  # default format
            'custom_quantity': 1,  # default quantity
            'product_ids': [(6, 0, self.mapped('product_id').ids)],
            'pricelist_id': self.env['product.pricelist.item'].search([
                ('product_id', 'in', self.mapped('product_id').ids)
            ], limit=1).pricelist_id.id,
        })

        xml_id, data = label_layout._prepare_report_data()
        if not xml_id:
            raise UserError(_('Unable to find report template'))

        report_action = self.env.ref(xml_id).report_action(None, data=data, config=False)
        report_action.update({'close_on_report_download': True})
        return report_action


