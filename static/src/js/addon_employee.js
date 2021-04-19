odoo.define('addon_employee.Employee_info', function (require) {
    "use strict";

    const publicWidget = require('web.public.widget');

    // publicWidget.registry.GetEmployeeInfo = publicWidget.Widget.extend({
    //     selector: '.employee',
    //     events: {
    //         click: '_onClick'
    //     },
    //     async _onClick(e) {
    //         e.preventDefault();
    //         await console.log(document.get)
    //     }
    // });

    var table = document.getElementById("table-employees");
    if (table != null) {
        for (var i = 0; i < table.rows.length; i++) {
            for (var j = 0; j < table.rows[i].cells.length; j++)
                table.rows[i].cells[j].onclick = function () {
                    tableText(this);
                };
        }
    }

    function tableText(tableCell) {
        console.log(tableCell);
        var employee_id = tableCell.getElementsByClassName("employee").item(0).id
        console.log(employee_id)
        window.location.href = './employee/info/' + employee_id
    }
});





