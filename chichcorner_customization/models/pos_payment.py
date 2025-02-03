from odoo import fields, models

class PosPayment(models.Model):
    _inherit = 'pos.payment'

    stan = fields.Char(
        string='STAN Number',
        related='pos_order_id.stan',
        readonly=True,
        help='System Trace Audit Number from the associated POS order.'
    )
    identite_number = fields.Char(
        string='CIN',
        related='pos_order_id.identite_number',
        readonly=True,
        help='System Trace Audit Number from the associated POS order.'
    )
    cheque_number = fields.Char(
        string='Check number',
        related='pos_order_id.cheque_number',
        readonly=True,
        help='System Trace Audit Number from the associated POS order.'
    )
    banque = fields.Selection(
        string='Banque',
        related='pos_order_id.banque',
        readonly=True,
        help='System Trace Audit Number from the associated POS order.'
    )

