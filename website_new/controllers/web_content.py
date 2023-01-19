import base64

from odoo import http
from odoo.http import request
import base64
import os


class Enquiry(http.Controller):

    @http.route('/enquiry_webform_new', type="http", auth="public", website="True")
    def enquiry_webform(self, **kw):
        # products_list = request.env['crm.new'].search([])
        # values = {}
        # values.update({
        #     'product_interested_in' : products_list
        # })


        return http.request.render('website_new.new_enquiry_form', {})

    @http.route('/create/enquiryform', type="http", auth="public", website="True")
    def create_enquiryform(self, **kw):
        print(kw,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')



        # c = kw.get('attachment')
        # os.path()
        # x = open(c, 'rb')
        # d = x.read()
        # b = kw[''].encode('utf-8')
        # print(base64.b64encode(b).decode(),d,c,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        crm_obj = request.env['crm.lead'].sudo().create(kw)
        print(crm_obj,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return request.render("website_new.enquiry_thanks", {})


