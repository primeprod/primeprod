from odoo import fields, models


class InheritCrm(models.Model):
    _inherit = "crm.lead"

    # def _get_default_myCheck1(self):
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    #     self.myCheck1 = True

    no_of_employee = fields.Integer(string="No. Of Employees")
    no_of_users = fields.Integer(string="Approx. no. of Logins")
    brief_label = fields.Text(string="Brief Description")
    callback = fields.Char(string="Request for a call back")
    # attachment = fields.Many2one(string="Attach Documents")
    product_interested_in = fields.Char(string="Products interested in")
    product_interested_in_mm = fields.Many2many('crm.new',string="Products interested in")

class NewLabel(models.Model):
    _name = "crm.new"

    name = fields.Char(string="Name")
    # hrms = fields.Many2many(string="HRMS")
    # cms = fields.Many2many(string="CMS")


# new module created for enquiry form
# new module created for enquiry form
# new module created for enquiry form
# new module created for enquiry form