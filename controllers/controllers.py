# -*- coding: utf-8 -*-
# from odoo import http


# class Rifa(http.Controller):
#     @http.route('/rifa/rifa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rifa/rifa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rifa.listing', {
#             'root': '/rifa/rifa',
#             'objects': http.request.env['rifa.rifa'].search([]),
#         })

#     @http.route('/rifa/rifa/objects/<model("rifa.rifa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rifa.object', {
#             'object': obj
#         })
