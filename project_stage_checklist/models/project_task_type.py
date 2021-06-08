# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    checklist_ids = fields.One2many('project.stage.checklist', 'task_type_id', string="Checklist")


class ProjectTask(models.Model):
    _inherit = "project.task"

    checklist_ids = fields.One2many('project.stage.checklist', 'task_id', string="Checklist")

    # @api.onchange('stage_id')
    # def _update_checklist(self):
    #     for line in self.checklist_ids:
    #         if not line.attachment_ids:
    #             raise ValidationError('Veuillez renseigner les pièces jointes '
    #                                   'au niveau de la checklist avant de procéder à la prochaine étape')
    #     res_lines = []
    #     for line in self.stage_id.checklist_ids:
    #         res_lines.append((0, 0, {
    #             'name': line.name
    #         }))
    #     print('onchange executed', res_lines)
    #     self.checklist_ids = res_lines

    def write(self, vals):
        if vals.get('stage_id', False):
            cl_lines = []
            next_stage = self.env['project.task.type'].browse(vals['stage_id'])
            if next_stage.sequence > self.stage_id.sequence:
                for line in self.checklist_ids:
                    if line.required and not line.attachment_ids:
                        raise ValidationError('Veuillez renseigner la pièces jointe requise pour la rubrique %s '
                                              'au niveau de la checklist avant de procéder à la prochaine étape' % line.name)

                for line in next_stage.checklist_ids:
                    existing_line = self.checklist_ids.filtered(lambda x: x.sequence == next_stage.sequence)
                    if not existing_line:
                        cl_lines.append((0, 0, {
                            'name': line.name,
                            'required': line.required,
                            'sequence': next_stage.sequence
                        }))
                vals['checklist_ids'] = cl_lines
        return super(ProjectTask, self).write(vals)


class ProjectStageTask(models.Model):
    _name = 'project.stage.checklist'

    name = fields.Char('Description')
    attachment_ids = fields.Many2many('ir.attachment', string="Pièces jointes")
    task_type_id = fields.Many2one('project.task.type', 'Étape')
    task_id = fields.Many2one('project.task', 'Tâche')
    required = fields.Boolean('Obligatoire', default=False)
    sequence = fields.Integer(string='Sequence')
