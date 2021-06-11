# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api


class FourriereFourriere(models.Model):
    _name = "fourriere.fourriere"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    state = fields.Selection([('nouveau', "Nouveau"), ('en_cours', "En cours"), ('sortit', "Sortit")],
                             string="État")
    date_in = fields.Datetime('Date entrée', default=fields.Datetime.today())
    date_out = fields.Datetime('Date sortie')
    name = fields.Char('Numéro')
    ordonnateur_id = fields.Many2one('fourriere.ordonnateur', 'Ordonnateur')
    emplacement_id = fields.Many2one('fourriere.ordonnateur.emplacement', 'Emplacement')
    type_entrant = fields.Many2one('fourriere.entrant', 'Type d\'entrant')
    num_entrant = fields.Char('Numéro d\'entrant')
    marque = fields.Many2one('fourriere.marque', 'Marque')
    duree = fields.Float('Durée en jours', compute='_compute_duree_cout')
    cout = fields.Float('Coût en Dirham', compute='_compute_duree_cout')

    @api.depends('type_entrant', 'date_in')
    def _compute_duree_cout(self):
        for rec in self:
            rec.cout = 0
            rec.duree = (datetime.today() - rec.date_in).days
            if rec.type_entrant:
                rec.cout = rec.duree * rec.type_entrant.cout

    def action_en_cours(self):
        self.write({
            'state': 'en_cours'
        })

    def action_sortit(self):
        self.write({
            'date_out': datetime.today(),
            'state': 'sortit'
        })


class FourriereOrdonnateur(models.Model):
    _name = "fourriere.ordonnateur"

    name = fields.Char('Nom')


class FourriereMarque(models.Model):
    _name = "fourriere.marque"

    name = fields.Char('Nom')


class FourriereOrdonnateurEmplacement(models.Model):
    _name = "fourriere.ordonnateur.emplacement"

    name = fields.Char('Nom')


class FourriereEntrant(models.Model):
    _name = "fourriere.entrant"

    name = fields.Char('Nom')
    cout = fields.Float('Coût')
