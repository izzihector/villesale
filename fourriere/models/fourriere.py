# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api


class FourriereFourriere(models.Model):
    _name = "fourriere.fourriere"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Fourrière"

    state = fields.Selection([('nouveau', "Nouveau"),
                              ('en_cours', "En cours"),
                              ('depassement', "Dépassement"),
                              ('sortit', "Sortie")],
                             string="État", default="nouveau")
    date_in = fields.Datetime('Date entrée', default=fields.Datetime.today())
    date_out = fields.Datetime('Date sortie')
    name = fields.Char('Numéro', readonly=True)
    ordonnateur_id = fields.Many2one('fourriere.ordonnateur', 'Ordonnateur')
    emplacement_id = fields.Many2one('fourriere.ordonnateur.emplacement', 'Emplacement')
    type_entrant = fields.Many2one('fourriere.entrant', 'Type d\'entrant')
    num_entrant = fields.Char('Numéro d\'entrant')
    num_quitance = fields.Char('Numéro de quitance')
    marque = fields.Many2one('fourriere.marque', 'Marque')
    duree = fields.Float('Durée en jours', compute='_compute_duree_cout')
    excede_duree = fields.Boolean('A éxcédé la durée max', default=False, compute='_compute_duree_cout')
    cout = fields.Float('Coût en Dirham', compute='_compute_duree_cout')
    doc_quitance = fields.Binary('Document de quitance')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('fourriere.fourriere')
        return super(FourriereFourriere, self).create(vals)

    @api.depends('type_entrant', 'date_in')
    def _compute_duree_cout(self):
        for rec in self:
            rec.cout = 0
            rec.duree = 0
            rec.excede_duree = False
            if rec.date_out:
                rec.duree = (rec.date_out - rec.date_in).days
            else:
                rec.duree = (datetime.today() - rec.date_in).days
                # rec.duree = (datetime.today() - rec.date_in).seconds / 60
            if rec.type_entrant:
                rec.cout = rec.duree * rec.type_entrant.cout
            if rec.state == 'en_cours':
                rec.excede_duree = rec.duree > rec.type_entrant.max
                rec.state = "depassement"

    def action_en_cours(self):
        self.write({
            'state': 'en_cours'
        })

    def action_sortit(self):
        return self.env.ref('fourriere.quitance_wizard_action').sudo().read()[0]


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
    max = fields.Float('Durée maximale dans la fourrirère en jours', default=365)
