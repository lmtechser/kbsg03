# -*- coding: utf-8 -*-

from odoo import models, fields, api

class k_modulo2(models.Model):
      _inherit = 'res.partner'
        
      codigo = fields.Char('codigo')  
      start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now()) 
#     _name = 'k_modulo2.k_modulo2'
#     _description = 'k_modulo2.k_modulo2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
