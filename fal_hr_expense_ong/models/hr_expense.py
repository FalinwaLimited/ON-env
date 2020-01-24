from odoo import models, fields, api, _


class HrExpense(models.Model):
    _inherit = 'hr.expense'


    # Fill in amount currency with fal_real_amount if it is zero
    @api.multi
    def _get_account_move_line_values(self):
        res = super(HrExpense, self)._get_account_move_line_values()
        for expense in self:
            company_currency = expense.company_id.currency_id
            different_currency = expense.currency_id != company_currency
            if not different_currency:
                move_line_values = res.get(expense.id)
                real_different_currency = expense.fal_real_currency != company_currency
                for move_line in move_line_values:
                    if not move_line.get('credit'):
                        move_line.update({
                            'amount_currency': expense.fal_real_amount if real_different_currency else 0.0,
                            'currency_id': expense.fal_real_currency.id if real_different_currency else False})
                    else:
                        move_line.update({
                            'amount_currency': -expense.fal_real_amount if real_different_currency else 0.0,
                            'currency_id': expense.fal_real_currency.id if real_different_currency else False})
        return res
