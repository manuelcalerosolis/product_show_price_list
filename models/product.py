# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp

import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pricelist_pub = fields.Float('First pricelist', compute='_compute_price_list', store=False,
                               digits=dp.get_precision('Product Price'))
    pricelist_t12 = fields.Float('Second pricelist', compute='_compute_price_list', store=False,
                               digits=dp.get_precision('Product Price'))
    pricelist_t10 = fields.Float('Third pricelist', compute='_compute_price_list', store=False,
                               digits=dp.get_precision('Product Price'))
    pricelist_t06 = fields.Float('Fourth pricelist', compute='_compute_price_list', store=False,
                               digits=dp.get_precision('Product Price'))
    pricelist_t04 = fields.Float('Fifth pricelist', compute='_compute_price_list', store=False,
                               digits=dp.get_precision('Product Price'))
    pricelist_t01 = fields.Float('Sixth pricelist', compute='_compute_price_list', store=False,
                               digits=dp.get_precision('Product Price'))
    pricelist_t03 = fields.Float('Seventh pricelist', compute='_compute_price_list', store=False,
                               digits=dp.get_precision('Product Price'))

    def _compute_price_list(self):

        for product in self:
            _logger.info(product.item_ids)

            product.pricelist_pub = 0
            product.pricelist_t12 = 0
            product.pricelist_t10 = 0
            product.pricelist_t06 = 0
            product.pricelist_t04 = 0
            product.pricelist_t01 = 0
            product.pricelist_t03 = 0

            for product_item_id in product.item_ids:

                _logger.info("*"*80)
                _logger.info("product_item_id.pricelist_id.id")
                _logger.info(product_item_id.pricelist_id.id)

                if product_item_id.pricelist_id.name == 'Tarifa pública':
                    product.pricelist_pub = product_item_id.fixed_price

                if product_item_id.pricelist_id.name == 'T-12: TARIFA ALMACEN':
                    product.pricelist_t12 = product_item_id.fixed_price

                if product_item_id.pricelist_id.name == 'T-10: TARIFA HUELVA':
                    product.pricelist_t10 = product_item_id.fixed_price

                if product_item_id.pricelist_id.name == 'T-06: TARIFA PROFESIONALES':
                    product.pricelist_t06 = product_item_id.fixed_price

                if product_item_id.pricelist_id.name == 'T-04: TARIFA PETIT&ASTUTO':
                    product.pricelist_t04 = product_item_id.fixed_price

                if product_item_id.pricelist_id.name == 'T-01: TARIFA TIENDA':
                    product.pricelist_t01 = product_item_id.fixed_price

                if product_item_id.pricelist_id.name == 'T-03: TARIFA MARIO FIALHO':
                    product.pricelist_t03 = product_item_id.fixed_price





