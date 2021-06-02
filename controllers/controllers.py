from odoo import http

class Spoints(http.Controller):

    @http.route('/spoints/spoints/', auth='public', website=True)
    def index(self, **kw):
        Employees = http.request.env['spoints.employees']
        return http.request.render('spoints.index', {
        	'employees': Employees.search([])
        })
    @http.route('/spoints/<model("spoints.employees"):employee>/', auth='public', website=True)
    def employee(self, employee):
    	return http.request.render('spoints.biography', {
    		'person': employee
    	})