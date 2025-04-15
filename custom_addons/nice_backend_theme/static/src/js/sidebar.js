odoo.define('nice_backend_theme.sidebar', function (require) {
    'use strict';

    var core = require('web.core');
    var session = require('web.session');
    var Widget = require('web.Widget');

    var SidebarMenu = Widget.extend({
        template: 'nice_backend_theme.sidebar',
        events: {
            'click .toggle-sidebar-btn': '_onToggleSidebar',
            'click .nav-link': '_onNavClick',
        },

        init: function () {
            this._super.apply(this, arguments);
            this.isSidebarToggled = false;
        },

        start: function () {
            this._super.apply(this, arguments);
            this._initSidebar();
            return this;
        },

        _initSidebar: function () {
            // Initialize sidebar state
            if (localStorage.getItem('sidebarState') === 'toggled') {
                this._toggleSidebar();
            }

            // Handle responsive behavior
            $(window).on('resize', _.debounce(function () {
                if (window.innerWidth < 1200) {
                    document.body.classList.add('toggle-sidebar');
                } else {
                    document.body.classList.remove('toggle-sidebar');
                }
            }, 200));
        },

        _onToggleSidebar: function (ev) {
            ev.preventDefault();
            this._toggleSidebar();
        },

        _toggleSidebar: function () {
            document.body.classList.toggle('toggle-sidebar');
            this.isSidebarToggled = !this.isSidebarToggled;
            localStorage.setItem('sidebarState', this.isSidebarToggled ? 'toggled' : '');
        },

        _onNavClick: function (ev) {
            var $target = $(ev.currentTarget);
            
            // Handle collapsible menus
            if ($target.hasClass('collapsed')) {
                $('.nav-link').not($target).addClass('collapsed');
                $('.nav-content').not($target.next()).removeClass('show');
            }

            // Close sidebar on mobile when clicking a menu item
            if (window.innerWidth < 1200) {
                document.body.classList.add('toggle-sidebar');
            }
        },
    });

    // Register sidebar widget
    core.action_registry.add('nice_backend_theme.sidebar', SidebarMenu);

    return {
        SidebarMenu: SidebarMenu,
    };
});
