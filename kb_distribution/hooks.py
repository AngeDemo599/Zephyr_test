# hooks.py for kb_distribution

app_name = "kb_distribution"
app_title = "KB Distribution"
app_publisher = "Your Company"
app_description = "KB Distribution App"
app_email = "your@email.com"
app_license = "MIT"

# Comprehensive fixtures configuration
fixtures = [
    # Export ALL doctypes
    {
        "dt": "DocType",
        "filters": [["name", "like", "%"]]
    },
    # Export all Custom HTML Block content
    {
        "dt": "Custom HTML Block",
        "filters": [["name", "like", "%"]]
    },
    # Export all Custom Fields
    {
        "dt": "Custom Field",
        "filters": [["name", "like", "%"]]
    },
    # Export all Client Scripts
    {
        "dt": "Client Script",
        "filters": [["name", "like", "%"]]
    },
    # Export all Server Scripts
    {
        "dt": "Server Script",
        "filters": [["name", "like", "%"]]
    },
    # Export all Print Formats
    {
        "dt": "Print Format",
        "filters": [["name", "like", "%"]]
    },
    # Export all Reports
    {
        "dt": "Report",
        "filters": [["name", "like", "%"]]
    },
    # Export all Workspaces
    {
        "dt": "Workspace",
        "filters": [["name", "like", "%"]]
    },
    # Export all Custom Roles
    {
        "dt": "Role",
        "filters": [["name", "like", "%"]]
    },
    # Export all Workflows
    {
        "dt": "Workflow",
        "filters": [["name", "like", "%"]]
    },
    # Export all Email Templates
    {
        "dt": "Email Template",
        "filters": [["name", "like", "%"]]
    },
    # Export all Property Setters
    {
        "dt": "Property Setter",
        "filters": [["name", "like", "%"]]
    },
    # Export all Notification settings
    {
        "dt": "Notification",
        "filters": [["name", "like", "%"]]
    },
    # Export all Letter Heads
    {
        "dt": "Letter Head",
        "filters": [["name", "like", "%"]]
    },
    # Export all Web Page content
    {
        "dt": "Web Page",
        "filters": [["name", "like", "%"]]
    },
    # Export all Web Forms
    {
        "dt": "Web Form",
        "filters": [["name", "like", "%"]]
    }
]

# Define doctype JavaScript files explicitly
doctype_js = {
    "Custom HTML Block": "public/js/custom_html_block.js",
    # Add other doctypes here with their JS files
}

# Register all modules
modules = {
    "KB Distribution": {
        "doctype": ["*"]
    }
}

# Include all custom apps JavaScript
app_include_js = [
    "custom_app.bundle.js"
]

# Include all CSS
app_include_css = [
    "custom_app.bundle.css"
]
