from odoo import http

class Spoints(http.Controller):

    @http.route('/spoints/spoints/', auth='public')
    def index(self, **kw):
        Employees = http.request.env['spoints.employees']
        return http.request.render('spoints.index', {
        	'employees': Employees.search([])
        })