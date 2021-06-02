# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    project_type = fields.Selection([('juridique', 'Gestion des affaires juridiques et contentieux'),
                                     ('patrimoine', 'Gestion du Patrimoine')], string="Type du Projet")


class ProjectTask(models.Model):
    _inherit = 'project.task'

    remarque = fields.Char('Remarque')
    etape_juridique_id = fields.Many2one('etape.juridique', stirng='Etape Juridique')
    tribunal_id = fields.Many2one('tribunal', stirng='Etape Juridique')
    resume = fields.Char('Résumé')
    num_dossier = fields.Char('Numéro de dossier')
    date_jugement = fields.Char('Date et jugement')
    avocat_id = fields.Many2one('res.partner', stirng='Avocat')
    defendeur = fields.Many2one('res.partner', stirng='Defendeur')
    demandeur = fields.Many2one('res.partner', stirng='Demandeur')
    annee = fields.Char('Année')
    id_affaire = fields.Char('ID Affaire')
    department_id = fields.Many2one('hr.department', 'Arrondissment')


class EtapeJuridique(models.Model):
    _name = 'etape.juridique'

    name = fields.Char('Nom')


class Tribunal(models.Model):
    _name = 'tribunal'

    name = fields.Char('Nom')
