# -*- coding: utf-8 -*-
from odoo import http

# class ReportCot(http.Controller):
#     @http.route('/report_cot/report_cot/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_cot/report_cot/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_cot.listing', {
#             'root': '/report_cot/report_cot',
#             'objects': http.request.env['report_cot.report_cot'].search([]),
#         })

#     @http.route('/report_cot/report_cot/objects/<model("report_cot.report_cot"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_cot.object', {
#             'object': obj
#         })