odoo.define('juvana_theme.theme', function (require) {
    'use strict';

    // Replace favicon with Juvana logo
    var link = document.querySelector("link[rel*='icon']") || document.createElement('link');
    link.type = 'image/x-icon';
    link.rel = 'shortcut icon';
    link.href = '/juvana_theme/static/img/favicon.ico';
    document.getElementsByTagName('head')[0].appendChild(link);

    // Add custom class to body for theme-specific styles
    document.body.classList.add('juvana_theme');
});
