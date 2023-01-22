# -*- coding: utf-8 -*-
# from odoo import http


# class PoApprove(http.Controller):
#     @http.route('/po_approve/po_approve/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/po_approve/po_approve/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('po_approve.listing', {
#             'root': '/po_approve/po_approve',
#             'objects': http.request.env['po_approve.po_approve'].search([]),
#         })

#     @http.route('/po_approve/po_approve/objects/<model("po_approve.po_approve"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('po_approve.object', {
#             'object': obj
#         })
