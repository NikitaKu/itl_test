# -*- coding: utf-8 -*-

import logging
from openerp import models
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_show_partners(self, cr, uid, ids, context=None):
        this = self.browse(cr, uid, ids, context=context)[0]
        return {
            'name': _('Same Customers'),
            'view_type': 'form',
            'view_mode': 'kanban,tree,form',
            'res_model': 'res.partner',
            'type': 'ir.actions.act_window',
            'context': {'search_default_customer': 1},
            'domain': [('customer', '=', True), ('city', '=', this.partner_id.city)],
        }

