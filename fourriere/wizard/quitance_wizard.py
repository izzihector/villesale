# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api


class FourriereFourriere(models.TransientModel):
    _name = "quitance.wizard"

    num_quitance = fields.Char('Numéro de quitance')
    date_quitance = fields.Date('Date quitance')
    doc_quitance = fields.Binary('Document de quitance')

    def act_validate(self):
        if self._context.get('active_id', False):
            fourriere_id = self.env['fourriere.fourriere'].browse(self._context['active_id'])
            fourriere_id.write({
                'date_out': self.date_quitance,
                'num_quitance': self.num_quitance,
                'doc_quitance': self.doc_quitance,
                'state': 'sortit'
            })
