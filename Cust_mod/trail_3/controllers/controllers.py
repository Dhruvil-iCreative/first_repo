# -*- coding: utf-8 -*-
# from odoo import http


# class Trail3(http.Controller):
#     @http.route('/trail_3/trail_3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trail_3/trail_3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trail_3.listing', {
#             'root': '/trail_3/trail_3',
#             'objects': http.request.env['trail_3.trail_3'].search([]),
#         })

#     @http.route('/trail_3/trail_3/objects/<model("trail_3.trail_3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trail_3.object', {
#             'object': obj
#         })
