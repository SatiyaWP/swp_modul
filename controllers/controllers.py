# -*- coding: utf-8 -*-
from odoo import http

# class SwpModul(http.Controller):
#     @http.route('/swp_modul/swp_modul/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/swp_modul/swp_modul/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('swp_modul.listing', {
#             'root': '/swp_modul/swp_modul',
#             'objects': http.request.env['swp_modul.swp_modul'].search([]),
#         })

#     @http.route('/swp_modul/swp_modul/objects/<model("swp_modul.swp_modul"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('swp_modul.object', {
#             'object': obj
#         })