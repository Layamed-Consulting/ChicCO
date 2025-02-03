# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import AccessError, UserError, ValidationError
import datetime


class ProductProduct(models.Model):
    _inherit = 'product.product'

    collection = fields.Char('Collection', index=True, copy=False)
    style = fields.Char('Style', index=True, copy=False)
    hs_code = fields.Char('HS Code', index=True, copy=False)
    composition = fields.Char('Composition', index=True, copy=False)
    origine_id = fields.Many2one('res.country', 'Origine', index=True, copy=False)
    chic_lot_ids = fields.One2many('chic.lot', 'product_id', string="Lot de fabrication")


class ChicLot(models.Model):
    _name = 'chic.lot'
    _description = 'Lots de fabrication'
    

    date_arrivage = fields.Datetime('Date arrivage', required=True)
    name = fields.Char('N° de lot', required=True, index=True)
    date_peremption = fields.Datetime('Date péremption', required=True, index=True)
    product_id = fields.Many2one('product.product', index=True)