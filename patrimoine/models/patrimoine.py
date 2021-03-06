# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PatrimoinePatrimoine(models.Model):
    _name = "patrimoine.patrimoine"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "num_id"

    num_id = fields.Char('ID')
    doc_source = fields.Char('Document Source')
    arrondissment = fields.Many2one('hr.department', 'Arrondissement')
    type_bien = fields.Char('Type du bien')
    consistance = fields.Char('Consistance')
    superficie = fields.Char('Superficie')
    superficie_num = fields.Float('Superficie numérique')
    source = fields.Char('Source')
    destination = fields.Char('Destination')
    adresse = fields.Char('Adresse')
    prix_acquisition = fields.Char('Prix acquisition')
    prix_acquisition_num = fields.Float('Prix acquisition numérique')
    titre_date = fields.Char('Titre et date')
    reference = fields.Char('Reference')
    reference_vente = fields.Char('Reference vente')
    prix_vente = fields.Char('prix vente')
    date_contrat = fields.Char('Date contrat')
    nom_exploitant = fields.Char('Nom exploitant')
    duree_exploitation = fields.Char('Duree exploitation')
    frequence_loyer = fields.Char('Frequence Loyer')
    prix_loyer = fields.Char('Prix Loyer')
    prix_loyer_annuel = fields.Float('Prix Loyer annuel numérique')
    remarque = fields.Char('Remarques')
    type_foncier = fields.Char('Type de foncier')
    type_location = fields.Char('Type de location')
    etage = fields.Char('Étage')
    type_2 = fields.Char('Type 2')
    numero = fields.Char('Numéro')
    bis = fields.Char('Bis')
    etat_actuel = fields.Char('État actuel')
    utilisation = fields.Char('Utilisation')
    loyer_id = fields.Many2one('patrimoine.loyer', string="Détails sur le loyer")
    parent_id = fields.Many2one('patrimoine.patrimoine', string="Patrimoine Parent")
    patri_latitude = fields.Float(string='Geo Latitude', digits=(16, 5))
    patri_longitude = fields.Float(string='Geo Longitude', digits=(16, 5))


class PatrimoineLoyer(models.Model):
    _name = "patrimoine.loyer"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    state = fields.Selection([('libre', "Libre"), ('occupe', "Occupé")], string="État du loyer")
    name = fields.Char('ID')
    rc = fields.Char('RC')
    patente = fields.Char('Patente')
    personnephysiqueoumorale = fields.Char('Personne physique ou morale')
    nom_societe = fields.Char('Nom Societe')
    nom_locataire = fields.Char('Nom locataire')
    designation_locataire = fields.Char('Designation locataire')
    cin_locataire = fields.Char('Cin locataire')
    adresse_locataire = fields.Char('Adresse locataire')
    tel = fields.Char('Tél')
    etat_administratif = fields.Char('Etat administratif')
    nom_exploitant = fields.Char('Nom exploitant')
    designation_exploitant = fields.Char('Designation exploitant')
    cin_exploitant = fields.Char('CIN exploitant')
    adresse_exploitant = fields.Char('Adresse exploitant')
    tel_exploitant = fields.Char('Tél exploitant')
    nature_exploitant = fields.Char('Nature exploitant')
    activite_exploitant = fields.Char('Activité exploitant')
    type_contrat = fields.Char('Type de contrat')
    disponible = fields.Boolean('Disponible')
    date_contrat = fields.Char('Date contrat')
    duree_location = fields.Char('Durée de location')
    prix_loyer_num = fields.Float('Prix loyer numérique')
    prix_loyer = fields.Char('Prix loyer')
    periodicite = fields.Char('Periodicité')
    etat_taxes = fields.Char('État des taxes')
    duree_mois = fields.Char('Durée en mois')
    source = fields.Char('Source')
    date = fields.Char('Date')
    numero = fields.Char('Numéro')
