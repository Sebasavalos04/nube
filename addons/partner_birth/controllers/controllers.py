# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerBirth(http.Controller):
#     @http.route('/partner_birth/partner_birth', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_birth/partner_birth/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_birth.listing', {
#             'root': '/partner_birth/partner_birth',
#             'objects': http.request.env['partner_birth.partner_birth'].search([]),
#         })

#     @http.route('/partner_birth/partner_birth/objects/<model("partner_birth.partner_birth"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_birth.object', {
#             'object': obj
#         })
