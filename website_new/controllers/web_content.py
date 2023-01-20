import base64

from odoo import http
from odoo.http import request
import base64
import os


class Enquiry(http.Controller):

    @http.route('/enquiry_webform_new', type="http", auth="public", website="True")
    def enquiry_webform(self, **kw):
        products_list = request.env['crm.new'].search([])
        values = {}
        values.update({
            'product_interested_in' : products_list
        })


        return http.request.render('website_new.new_enquiry_form', values)

    @http.route('/create/enquiryform', type="http", auth="public", website="True")
    def create_enquiryform(self, **kw):



        # c = kw.get('attachment')
        # os.path()
        # x = open(c, 'rb')
        # d = x.read()
        # b = kw[''].encode('utf-8')
        # print(base64.b64encode(b).decode(),d,c,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        # kw['type'] = 'lead'
        product_interested_in = request.httprequest.form.getlist('product_interested_in')
        # print(product_interested_in,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        crm_val = {
            'partner_name': kw['partner_name'],
            'name':  kw['name'],
            'street': kw['street'],
            'email_from': kw['email_from'],
            'phone':kw['phone'],
            'no_of_employee': kw['no_of_employee'],
            'no_of_users': kw['no_of_users'],
            'description': kw['description'],
            'callback': kw['callback'],
            'type':'lead',
            'product_interested_in_mm' : product_interested_in
        }
        crm_obj = request.env['crm.lead'].sudo().create(crm_val)
        # print(crm_val,crm_obj,'crm_obj!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return request.render("website_new.enquiry_thanks", {})

        # print(crm_val,crm_obj,'crm_obj!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        # print(crm_val,crm_obj,'crm_obj!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        # print(crm_val,crm_obj,'crm_obj!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


