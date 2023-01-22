# -*- coding: utf-8 -*-

from odoo import models, fields, api


class po_approve(models.Model):
    _inherit = 'purchase.order'
    state = fields.Selection([
        ('draft', 'RFQ'),
        ('sent', 'RFQ Sent'),
        ('to approve', 'To Approve'),
        ('first_approve', 'First Approved'),
        ('second_approve', 'Second Approved'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)

    def first_approve(self):
        for rec in self:
            rec.write({'state': 'first_approve'})

    def button_confirm(self):
        for order in self:
            if order.state not in ['draft', 'sent', 'second_approve']:
                continue
            order._add_supplier_to_product()
            # Deal with double validation process
            if order._approval_allowed():
                order.button_approve()
            else:
                order.write({'state': 'to approve'})
            if order.partner_id not in order.message_partner_ids:
                order.message_subscribe([order.partner_id.id])
        self._purchase_request_line_check()
        self._purchase_request_confirm_message()
        return True
    def second_approve(self):
        for rec in self:
            rec.write({'state': 'second_approve'})