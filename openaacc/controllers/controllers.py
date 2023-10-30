# -*- coding: utf-8 -*-
# from odoo import http


# class Openaacc(http.Controller):
#     @http.route('/openaacc/openaacc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openaacc/openaacc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('openaacc.listing', {
#             'root': '/openaacc/openaacc',
#             'objects': http.request.env['openaacc.openaacc'].search([]),
#         })

#     @http.route('/openaacc/openaacc/objects/<model("openaacc.openaacc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openaacc.object', {
#             'object': obj
#         })
