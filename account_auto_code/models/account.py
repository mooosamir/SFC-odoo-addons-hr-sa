# -*- coding: utf-8 -*-
from odoo import models, fields, api ,_
from odoo.exceptions import UserError

class Autocode(models.Model):
    _inherit = 'account.account'

    do_increment = fields.Boolean(string="",  )
    new_group_id = fields.Many2one('account.group',string='Group',readonly=False,copy=True)
    code = fields.Char(size=64, required=True, index=True)

    # @api.model
    # def create(self, vals_list):
    #     res = super(Autocode, self).create(vals_list)
    #     if res.group_id and res.group_id.code_prefix_start and res.group_id.code_prefix_end:
    #         obj = self.env['account.account'].search([('group_id','=',res.group_id.id)])
    #         list_code = []
    #         for record in obj:
    #             list_code.append(int(record.code))
    #         if list_code:
    #             if max(list_code) != int(res.group_id.code_prefix_end):
    #                 max_number = max(list_code) + 1
    #                 res.sudo().update({'code':str(max_number)})
    #             else:
    #                 raise UserError(_("Auto code cannot increment the code field because the account group reach the prefix end code"))
    #         else:
    #             res.sudo().write({'code': str(res.group_id.code_prefix_start)})
    #     return res

            # line.do_increment = True

    @api.onchange('new_group_id','user_type_id')
    def auto_code(self):
        for line in self:
            lists_invalid_code = []
            for invalid in self.env['account.account'].search([('id', '!=', line._origin.id), ('code', '!=', False)]):
                lists_invalid_code.append(int(invalid.code))

            if line.new_group_id and line.new_group_id.code_prefix_start and line.new_group_id.code_prefix_end and (line.code==False or line.code==''):
                list_code = []
                lists_range_code=[]
                for r in range(int(line.new_group_id.code_prefix_start),int(line.new_group_id.code_prefix_end)+1):
                    lists_range_code.append(r)

                obj = self.env['account.account'].search([('new_group_id','=',line.new_group_id.id),('id','!=',line._origin.id),('code','!=',False),('code','in',lists_range_code)])


                for record in obj:
                    list_code.append(int(record.code))
                if list_code:
                    if max(list_code) != int(line.new_group_id.code_prefix_end) and max(list_code) + 1 not in lists_invalid_code:
                        max_number = max(list_code) + 1
                        line.sudo().write({'code':str(max_number)})
                    else:
                        sub = list(set(lists_range_code) - set(lists_invalid_code))
                        if sub:
                                max_number = min(sub)
                                line.sudo().write({'code': str(max_number)})
                        else:
                            raise UserError(_("Auto code cannot increment the code field because the account group reach the prefix end code"))
                else:
                    sub = list(set(lists_range_code) - set(lists_invalid_code))
                    if sub:
                            max_number = min(sub)
                            line.sudo().write({'code': str(max_number)})
                    else:
                        line.sudo().write({'code': str(line.new_group_id.code_prefix_start)})
            else:
               if line.user_type_id and (line.code==False or line.code==''):
                    obj = self.env['account.account'].search([('user_type_id','=',line.user_type_id.id),('id','!=',line._origin.id),('code','!=',False)],order="create_date DESC")
                    list_code = []
                    for record in obj:
                        list_code.append(int(record.code))
                    if len(list_code) > 0:
                        if max(list_code)+1 in lists_invalid_code:
                            line.sudo().write({'code': str(max(lists_invalid_code)+1)})
                        else:
                            line.sudo().write({'code': str(max(list_code)+1)})
                    else:
                        line.sudo().write({'code':'000000001'})




    # @api.onchange('user_type_id')
    # def auto_code(self):
    #     for line in self:
    #         if line.user_type_id and line.code==False:
    #             obj = self.env['account.account'].search([('user_type_id','=',line.user_type_id.id),('id','!=',line._origin.id),('code','!=',False)],order="create_date DESC")
    #             list_code = []
    #             for record in obj:
    #                 list_code.append(int(record.code))
    #             if len(list_code) > 0:
    #                 line.sudo().write({'code': str(list_code[0]+1)})

