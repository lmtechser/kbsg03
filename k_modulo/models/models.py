# -*- coding: utf-8 -*-

from odoo import models, fields, api


class k_modulo(models.Model):
     _name = 'k_modulo.k_modulo'
     _description = 'k_modulo.k_modulo'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

     @api.depends('value')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100
