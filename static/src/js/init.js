odoo.define('addon_employee.Addon_employee', function (required) {
    "use strict";
    function initCss(e) {
        var style_css = document.createElement("link");

        style_css.setAttribute("rel", "stylesheet"),
        style_css.setAttribute("type", "text/css"),
        style_css.onload = e,
        style_css.setAttribute("href", "/addon_employee/static/src/css/addon_employee.css"),
        document.head.appendChild(style_css);
    }
    function initJs(e) {
        var js_src = document.createElement("script");

        js_src.setAttribute("type", "text/javascript"),
        js_src.onload = e,
        js_src.setAttribute("src", "/addon_employee/static/src/js/addon_employee.js"),
        document.head.appendChild(js_src);
    }
    initCss()
    initJs()
});

