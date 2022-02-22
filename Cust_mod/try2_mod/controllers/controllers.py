# -*- coding: utf-8 -*-
# from odoo import http


# class Try2Mod(http.Controller):
#     @http.route('/try2_mod/try2_mod', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/try2_mod/try2_mod/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('try2_mod.listing', {
#             'root': '/try2_mod/try2_mod',
#             'objects': http.request.env['try2_mod.try2_mod'].search([]),
#         })

#     @http.route('/try2_mod/try2_mod/objects/<model("try2_mod.try2_mod"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('try2_mod.object', {
#             'object': obj
#         })
