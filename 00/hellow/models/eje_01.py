from odoo import api, fields, models
#Probando 1, subida 
class ejemplo01(models.Model):
    _name = "eje.01"
    name  = fields.Char(string = "name", required = True)
    age = fields.Integer(String = "age")
    color = fields.Char(String = "color")
    is_new = fields.Boolean(String ="is_new")
    type = fields.Selection([
        ("dog","Dog"),
        ("cat","Cat"),
        ("bird","Bird"),
        ("fish","Fish"),
        ("other","Other")],String ="type", default = "small", required = True)
