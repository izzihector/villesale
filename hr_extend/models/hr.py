# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    french_name = fields.Char('Nom en Français')

    def name_get(self):
        result = []
        for record in self:
            record_name = record.name
            if record.french_name:
                record_name += ' - ' + record.french_name
            result.append((record.id, record_name))
        return result

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if args is None:
            args = []
        domain = ['|', ('french_name', operator, name), ('name', operator, name)]
        return self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)


class HrDepartment(models.Model):
    _inherit = "hr.department"

    french_name = fields.Char('Nom en Français')

    def name_get(self):
        result = []
        for record in self:
            record_name = record.name
            if record.french_name:
                record_name += ' - ' + record.french_name
            result.append((record.id, record_name))
        return result

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if args is None:
            args = []
        domain = ['|', ('french_name', operator, name), ('name', operator, name)]
        return self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)


class HrJob(models.Model):
    _inherit = "hr.job"

    french_name = fields.Char('Nom en Français')

    def name_get(self):
        result = []
        for record in self:
            record_name = record.name
            if record.french_name:
                record_name += ' - ' + record.french_name
            result.append((record.id, record_name))
        return result

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if args is None:
            args = []
        domain = ['|', ('french_name', operator, name), ('name', operator, name)]
        return self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)
