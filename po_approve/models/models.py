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
        for rec in self:
            rec.write({'state': 'purchase'})

    def second_approve(self):
        for rec in self:
            rec.write({'state': 'second_approve'})