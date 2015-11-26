# -*- coding: utf-8 -*-
from openerp import http

# class Oc-cadastro(http.Controller):
#     @http.route('/oc-cadastro/oc-cadastro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oc-cadastro/oc-cadastro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oc-cadastro.listing', {
#             'root': '/oc-cadastro/oc-cadastro',
#             'objects': http.request.env['oc-cadastro.oc-cadastro'].search([]),
#         })

#     @http.route('/oc-cadastro/oc-cadastro/objects/<model("oc-cadastro.oc-cadastro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oc-cadastro.object', {
#             'object': obj
#         })