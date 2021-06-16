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
    type_entrant = fields.Many2one('fourriere.entrant.type', string='Type d\'entrant')
    marque_id = fields.Many2one('fourriere.entrant', 'Marque')
    num_entrant = fields.Char('Numéro d\'entrant')
    num_quitance = fields.Char('Numéro de quitance')
    marque = fields.Many2one('fourriere.entrant', 'Marque')
    duree = fields.Float('Durée en jours', compute='_compute_duree_cout')
    excede_duree = fields.Boolean('A éxcédé la durée max', default=False, compute='_compute_duree_cout')
    cout = fields.Float('Coût en Dirham', compute='_compute_duree_cout')
    doc_quitance = fields.Binary('Document de quitance')
    doc_mef = fields.Binary('Document de mise en fourrière')

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
                rec.duree = (rec.date_out - rec.date_in).days + 1
            else:
                rec.duree = (datetime.today() - rec.date_in).days + 1
                # rec.duree = (datetime.today() - rec.date_in).seconds / 60
            if rec.type_entrant:
                rec.cout = rec.duree * rec.type_entrant.cout
            if rec.state in ('en_cours', 'depassement'):
                rec.excede_duree = rec.duree > rec.type_entrant.max
                if rec.excede_duree:
                    rec.state = "depassement"
                else:
                    rec.state = "en_cours"

    def action_en_cours(self):
        self.write({
            'state': 'en_cours'
        })

    def action_sortit(self):
        return self.env.ref('fourriere.quitance_wizard_action').sudo().read()[0]


class FourriereOrdonnateur(models.Model):
    _name = "fourriere.ordonnateur"

    name = fields.Char('Nom')


class FourriereOrdonnateurEmplacement(models.Model):
    _name = "fourriere.ordonnateur.emplacement"

    name = fields.Char('Nom')


class FourriereEntrant(models.Model):
    _name = "fourriere.entrant"
    _rec_name = "name_ar"

    name = fields.Char('Nom')
    name_ar = fields.Char('Nom en Arabe')
    type_id = fields.Many2one('fourriere.entrant.type', 'Type d\'entrant')


class FourriereEntrantType(models.Model):
    _name = "fourriere.entrant.type"
    _rec_name = "name_ar"

    name = fields.Char('Nom')
    name_ar = fields.Char('Nom en Arabe')
    cout = fields.Float('Coût')
    max = fields.Float('Durée maximale dans la fourrirère en jours', default=365)
