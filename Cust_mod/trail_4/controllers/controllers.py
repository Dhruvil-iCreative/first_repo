# -*- coding: utf-8 -*-
# from odoo import http


# class Trail4(http.Controller):
#     @http.route('/trail_4/trail_4', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trail_4/trail_4/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trail_4.listing', {
#             'root': '/trail_4/trail_4',
#             'objects': http.request.env['trail_4.trail_4'].search([]),
#         })

#     @http.route('/trail_4/trail_4/objects/<model("trail_4.trail_4"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trail_4.object', {
#             'object': obj
#         })
