from odoo import http
from odoo.http import request


class AddonEmployee(http.Controller):
    @http.route(['/employee/employee', '/employee/employee/page/<int:page>'], type="http", auth="user", website=True)
    def employee_list(self, page=0, **kw):
        current_id = request.session.uid
        current_user = http.request.env['hr.employee'].search([('user_id', '=', current_id)], limit=1)
        if current_user.user_has_groups('hr.group_hr_manager'):
            employees = request.env['hr.employee'].search([])
            total = request.env['hr.employee'].search_count([])
        else:
            employees = request.env['hr.employee'].search([('department_id', '=', current_user.department_id.id)])
            total = request.env['hr.employee'].search_count([('department_id', '=', current_user.department_id.id)])
        pager = request.website.pager(
            url='/employee/employee',
            total=total,
            page=page,
            step=10,
        )
        offset = pager['offset']
        employees = employees[offset: offset + 10]
        if len(employees) % 5 == 0:
            rows = len(employees) // 5
        else:
            rows = len(employees) // 5 + 1
        employees_dict = {}
        for i in range(rows):
            employees_dict[i] = {}
            for j in range(5):
                try:
                    employees_dict[i][j] = employees[i * 5 + j]
                except:
                    break
        return request.render('addon_employee.employee_list', {
            'employees': employees,
            'pager': pager,
            'employees_dict': employees_dict,
        })

    @http.route(['/employee/employee/info/<int:id>'], type='http', auth='user', website=True)
    def employee_info(self, id, **kw):
        current_id = request.session.uid
        current_user = http.request.env['hr.employee'].search([('user_id', '=', current_id)], limit=1)
        employee = request.env['hr.employee'].search([('id', '=', id)], limit=1)
        if employee:
            if current_user.user_has_groups('hr.group_hr_manager'):
                    return request.render('addon_employee.employee_info', {'employee': employee})
            else:
                if current_user.id == employee.id:
                    return request.render('addon_employee.employee_info', {'employee': employee})
                else:
                    return request.render('addon_employee.employee_info_alert')

    @http.route(['/employee/employee/info'], type='http', auth='user', website=True)
    def self_info(self, **kw):
        current_id = request.session.uid
        current_user = http.request.env['hr.employee'].search([('user_id', '=', current_id)], limit=1)
        employee = request.env['hr.employee'].search([('id', '=', current_user.id)], limit=1)
        if employee:
            return request.render('addon_employee.employee_info', {'employee': employee})


    # @http.route(['/redirect'], type='json', auth="user", website=True)
    # def select_employee(self, **post):
    #     id = post.get('id')
    #     employee = request.env['hr.employee'].search([('id', '=', id)], limit=1)
    #     print(id)
    #     return request.env['ir.ui.view']._render_template(
    #         'addon_employee.employee_info', {'employee': employee})
