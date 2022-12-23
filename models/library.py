from odoo import models, fields, api


class Library(models.Model):
    _name = "uadb.library"
    _description = "Gestion BU"

    date_pub = fields.Date("Date")
    num_isbn = fields.Char("CodeIsbn")
    auteur = fields.Many2many("res.partner")