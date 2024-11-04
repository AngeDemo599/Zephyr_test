app_name = "kb_distribution"
app_title = "Kb Distribution"
app_publisher = "KB DEVELOPPEMENT"
app_description = "Application de distribution conçu par l\'équipe KB"
app_email = "webdev@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "kb_distribution",
# 		"logo": "/assets/kb_distribution/logo.png",
# 		"title": "Kb Distribution",
# 		"route": "/kb_distribution",
# 		"has_permission": "kb_distribution.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/kb_distribution/css/kb_distribution.css"
# app_include_js = "/assets/kb_distribution/js/kb_distribution.js"

# include js, css files in header of web template
# web_include_css = "/assets/kb_distribution/css/kb_distribution.css"
# web_include_js = "/assets/kb_distribution/js/kb_distribution.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "kb_distribution/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "kb_distribution/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "kb_distribution.utils.jinja_methods",
# 	"filters": "kb_distribution.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "kb_distribution.install.before_install"
# after_install = "kb_distribution.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "kb_distribution.uninstall.before_uninstall"
# after_uninstall = "kb_distribution.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "kb_distribution.utils.before_app_install"
# after_app_install = "kb_distribution.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "kb_distribution.utils.before_app_uninstall"
# after_app_uninstall = "kb_distribution.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "kb_distribution.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"kb_distribution.tasks.all"
# 	],
# 	"daily": [
# 		"kb_distribution.tasks.daily"
# 	],
# 	"hourly": [
# 		"kb_distribution.tasks.hourly"
# 	],
# 	"weekly": [
# 		"kb_distribution.tasks.weekly"
# 	],
# 	"monthly": [
# 		"kb_distribution.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "kb_distribution.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "kb_distribution.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "kb_distribution.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["kb_distribution.utils.before_request"]
# after_request = ["kb_distribution.utils.after_request"]

# Job Events
# ----------
# before_job = ["kb_distribution.utils.before_job"]
# after_job = ["kb_distribution.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"kb_distribution.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# my_customizations/my_customizations/hooks.py


# Fixtures - this will export all your customizations
fixtures = [
    # Custom DocTypes
    "DocType",
    
    # Print Formats
    {
        "doctype": "Print Format",
        "filters": [
            ["standard", "=", "No"]
        ]
    },
    
    # Custom Fields
    {
        "doctype": "Custom Field"
    },
    
    # Client Scripts
    {
        "doctype": "Client Script"
    },
    
    # Server Scripts
    {
        "doctype": "Server Script"
    },
    
    # Workspaces
    {
        "doctype": "Workspace"
    },
    
    # Custom DocPerm
    {
        "doctype": "Custom DocPerm"
    },
    
    # Property Setter
    {
        "doctype": "Property Setter"
    },
    
    # Report
    {
        "doctype": "Report",
        "filters": [
            ["is_standard", "=", "No"]
        ]
    },
    
    # Notification
    {
        "doctype": "Notification"
    },
    
    # Workflow
    "Workflow",
    "Workflow State",
    "Workflow Action"
]

# Include js/css files
app_include_js = [
    "/assets/my_customizations/js/my_customizations.js"
]

app_include_css = [
    "/assets/my_customizations/css/my_customizations.css"
]
