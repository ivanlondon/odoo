odoo.define('nice_backend_theme.theme', function (require) {
    'use strict';

    var core = require('web.core');
    var session = require('web.session');
    var Widget = require('web.Widget');
    var SystrayMenu = require('web.SystrayMenu');
    var config = require('web.config');

    var ThemeCustomizer = Widget.extend({
        template: 'nice_backend_theme.theme_customizer',
        events: {
            'click .theme-toggle': '_onThemeToggle',
            'click .sidebar-toggle': '_onSidebarToggle'
        },

        init: function () {
            this._super.apply(this, arguments);
            this.isSidebarCollapsed = false;
            this.isDarkMode = localStorage.getItem('theme') === 'dark';
            this._applyTheme();
        },

        start: function () {
            this._super.apply(this, arguments);
            this._initTheme();
            return this;
        },

        _initTheme: function () {
            // Add theme class to body
            $('body').addClass('nice_theme');
            
            // Initialize responsive behavior
            this._handleResponsive();
            $(window).on('resize', _.debounce(this._handleResponsive.bind(this), 200));
        },

        _handleResponsive: function () {
            if (window.innerWidth < 992) {
                this.isSidebarCollapsed = true;
                $('body').addClass('sidebar-collapsed');
            } else if (this.isSidebarCollapsed) {
                this.isSidebarCollapsed = false;
                $('body').removeClass('sidebar-collapsed');
            }
        },

        _onThemeToggle: function (ev) {
            ev.preventDefault();
            this.isDarkMode = !this.isDarkMode;
            this._applyTheme();
        },

        _onSidebarToggle: function (ev) {
            ev.preventDefault();
            this.isSidebarCollapsed = !this.isSidebarCollapsed;
            $('body').toggleClass('sidebar-collapsed');
        },

        _applyTheme: function () {
            if (this.isDarkMode) {
                $('body').addClass('dark-mode');
                localStorage.setItem('theme', 'dark');
            } else {
                $('body').removeClass('dark-mode');
                localStorage.setItem('theme', 'light');
            }
        }
    });

    // Add theme customizer to systray menu
    SystrayMenu.Items.push(ThemeCustomizer);

    return {
        ThemeCustomizer: ThemeCustomizer
    };
});
