# -*- coding: utf-8 -*-
# from odoo import http


# class KModulo2(http.Controller):
#     @http.route('/k_modulo2/k_modulo2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/k_modulo2/k_modulo2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('k_modulo2.listing', {
#             'root': '/k_modulo2/k_modulo2',
#             'objects': http.request.env['k_modulo2.k_modulo2'].search([]),
#         })

#     @http.route('/k_modulo2/k_modulo2/objects/<model("k_modulo2.k_modulo2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('k_modulo2.object', {
#             'object': obj
#         })
