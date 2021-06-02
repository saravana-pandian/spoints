from odoo import http

class Spoints(http.Controller):

    @http.route('/spoints/spoints/', auth='public')
    def index(self, **kw):
        return http.request.render('spoints.index', {
            'employees': ["Employee 1", "Employee 2", "Employee 3"],
        })