# -*- coding: utf-8 -*-
from odoo import models, fields, api


class BugAdvanced(models.Model):
    _inherit = 'bm.bug'
    need_time = fields.Integer('所需时间(小时)')
    name = fields.Char(help='简要描述发现的bug')
    stage_id = fields.Many2one('bm.bug.stage', '阶段')
    tag_ids = fields.Many2many('bm.bug.tag', string='标示')