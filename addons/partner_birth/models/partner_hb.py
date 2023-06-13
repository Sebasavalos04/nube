# -*- coding: utf-8 -*-
from odoo import models, fields

class partner(models.Model):
    _inherit="res.partner"
    date_of_birth=fields.Date(string="Año de Cumpleanios")
    sex = fields.Selection([
        ('male', 'Masculino'),
        ('female', 'Femenino'),
        ('other', 'Otro')],
        string='Género')