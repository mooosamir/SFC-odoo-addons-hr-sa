from odoo import models, fields, api,_
from odoo.exceptions import ValidationError,UserError
from odoo.tools.misc import formatLang, get_lang

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    state = fields.Selection([
        ('draft', 'RFQ'),
        ('sent', 'RFQ Sent'),
        ('to approve', 'To Approve'),
        ('submit', 'Submited'),
        ('first_approve', 'First Approved'),
        ('second_approve', 'Second Approved'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)

    def submit(self):
        for rec in self:
            rec.write({'state':'submit'})
    def first_approve(self):
        for rec in self:
            rec.write({'state':'first_approve'})
    def second_approve(self):
        for rec in self:
            rec.write({'state':'second_approve'})

