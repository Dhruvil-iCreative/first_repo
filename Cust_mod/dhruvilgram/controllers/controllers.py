# -*- coding: utf-8 -*-
# from odoo import http


# class Dhruvilgram(http.Controller):
#     @http.route('/dhruvilgram/dhruvilgram', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dhruvilgram/dhruvilgram/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dhruvilgram.listing', {
#             'root': '/dhruvilgram/dhruvilgram',
#             'objects': http.request.env['dhruvilgram.dhruvilgram'].search([]),
#         })

#     @http.route('/dhruvilgram/dhruvilgram/objects/<model("dhruvilgram.dhruvilgram"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dhruvilgram.object', {
#             'object': obj
#         })
