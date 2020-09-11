# -*- coding: utf-8 -*-
from odoo import http


class KModulo(http.Controller):
     @http.route('/k_modulo/k_modulo/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/k_modulo/k_modulo/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('k_modulo.listing', {
             'root': '/k_modulo/k_modulo',
             'objects': http.request.env['k_modulo.k_modulo'].search([]),
         })

     @http.route('/k_modulo/k_modulo/objects/<model("k_modulo.k_modulo"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('k_modulo.object', {
             'object': obj
         })
