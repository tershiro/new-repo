# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "app_test"
app_title = "test-app"
app_publisher = "stericano"
app_description = "test-app by stericano"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "tershiro@windowslive.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/app_test/css/app_test.css"
# app_include_js = "/assets/app_test/js/app_test.js"

# include js, css files in header of web template
# web_include_css = "/assets/app_test/css/app_test.css"
# web_include_js = "/assets/app_test/js/app_test.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "app_test.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "app_test.install.before_install"
# after_install = "app_test.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "app_test.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"app_test.tasks.all"
# 	],
# 	"daily": [
# 		"app_test.tasks.daily"
# 	],
# 	"hourly": [
# 		"app_test.tasks.hourly"
# 	],
# 	"weekly": [
# 		"app_test.tasks.weekly"
# 	]
# 	"monthly": [
# 		"app_test.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "app_test.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "app_test.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "app_test.task.get_dashboard_data"
# }

