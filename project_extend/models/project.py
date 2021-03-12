# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    project_type = fields.Selection([('juridique', 'Gestion des affaires juridiques et contentieux'),
                                     ('patrimoine', 'Gestion du Patrimoine')], string="Type du Projet")
