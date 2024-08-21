app_name = "custom_apps"
app_title = "Custom Apps"
app_publisher = "Monil Kamboj"
app_description = "Custom Apps"
app_email = "abc@example.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/custom_apps/css/custom_apps.css"
# app_include_js = "/assets/custom_apps/js/custom_apps.js"

# include js, css files in header of web template
# web_include_css = "/assets/custom_apps/css/custom_apps.css"
# web_include_js = "/assets/custom_apps/js/custom_apps.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "custom_apps/public/scss/website"

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
# app_include_icons = "custom_apps/public/icons.svg"

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
# 	"methods": "custom_apps.utils.jinja_methods",
# 	"filters": "custom_apps.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "custom_apps.install.before_install"
# after_install = "custom_apps.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "custom_apps.uninstall.before_uninstall"
# after_uninstall = "custom_apps.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "custom_apps.utils.before_app_install"
# after_app_install = "custom_apps.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "custom_apps.utils.before_app_uninstall"
# after_app_uninstall = "custom_apps.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "custom_apps.notifications.get_notification_config"

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
# 		"custom_apps.tasks.all"
# 	],
# 	"daily": [
# 		"custom_apps.tasks.daily"
# 	],
# 	"hourly": [
# 		"custom_apps.tasks.hourly"
# 	],
# 	"weekly": [
# 		"custom_apps.tasks.weekly"
# 	],
# 	"monthly": [
# 		"custom_apps.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "custom_apps.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "custom_apps.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "custom_apps.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["custom_apps.utils.before_request"]
# after_request = ["custom_apps.utils.after_request"]

# Job Events
# ----------
# before_job = ["custom_apps.utils.before_job"]
# after_job = ["custom_apps.utils.after_job"]

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
# 	"custom_apps.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
        {
        'doctype':'State',
        "filters":{
            'name':['in',(
                "Andaman and Nicobar Islands",
                "Andhra Pradesh",
                "Arunachal Pradesh",
                "Assam",
                "Bihar",
                "Chandigarh",
                "Chhattisgarh",
                "Dadra and Nagar Haveli and Daman and Diu",
                "Delhi",
                "Goa",
                "Gujarat",
                "Haryana",
                "Himachal Pradesh",
                "Jammu and Kashmir",
                "Jharkhand",
                "Karnataka",
                "Kerala",
                "Ladakh",
                "Lakshadweep",
                "Madhya Pradesh",
                "Maharashtra",
                "Manipur",
                "Meghalaya",
                "Mizoram",
                "Nagaland",
                "Odisha",
                "Puducherry",
                "Punjab",
                "Rajasthan",
                "Sikkim",
                "Tamil Nadu",
                "Telangana",
                "Tripura",
                "Uttarakhand",
                "Uttar Pradesh",
                "West Bengal",
            )]
        }
    },
    {
        'doctype':'District',
        "filters":{
            'name':['in',(
                "Ambala",
                "Bhiwani", 
                "Faridabad", "Fatehabad", 
                "Gurgaon (Gurugram)", 
                "Hisar", 
                "Jhajjar", "Jind", 
                "Kaithal", "Karnal", "Kurukshetra", 
                "Mahendragarh (Narnaul)", "Mewat", "Palwal", "Panchkula", "Panipat", "Rewari", "Rohtak", "Sirsa", "Sonipat", "Yamunanagar", "Anantapur", "Chittoor", "East Godavari", "Guntur", "Krishna", "Kurnool", "Nellore", "Prakasam", "Srikakulam", "Visakhapatnam", "Vizianagaram", "West Godavari", "YSR Kadapa", "Adilabad", "Hyderabad", "Karimnagar", "Khammam", "Mahabubnagar", "Medak", "Nalgonda", "Nizamabad", "Chandigarh", "Warangal", "Jayashankar Bhupalpally", "Mulugu", "Peddapalli", "Rajanna Sircilla", "Tawang", "West Kameng", "East Kameng", "Papum Pare", "Lower Subansiri", "Upper Subansiri", "West Siang", "East Siang", "Siang", "Changlang", "Tirap", "Longding", "Anjaw", "Lohit", "Namsai", "Kamle", "Kurung Kumey", "Kra Daadi", "Leparada", "Lower Dibang Valley", "Upper Dibang Valley", "Dibang Valley", "Upper Siang", "Pakke-Kessang", "Shi-Yomi", "Baksa", "Barpeta", "Bongaigaon", "Cachar", "Charaideo", "Chirang", "Darrang", "Dhemaji", "Dhubri", "Dibrugarh", "Goalpara", "Golaghat", "Hailakandi", "Hojai", "Jorhat", "Kamrup", "Kamrup Metropolitan", "Karbi Anglong", "Karimganj", "Kokrajhar", "Lakhimpur", "Majuli", "Morigaon", "Nagaon", "Nalbari", "Sivasagar", "Sonitpur", "South Salmara-Mankachar", "Tinsukia", "Udalguri", "West Karbi Anglong", "Biswanath", "Araria", "Arwal", "Aurangabad", "Banka", "Begusarai", "Bhagalpur", "Bhojpur", "Buxar", "Darbhanga", "East Champaran", "Gaya", "Gopalganj", "Jamui", "Jehanabad", "Kaimur", "Katihar", "Kishanganj", "Lakhisarai", "Madhepura", "Madhubani", "Munger", "Muzaffarpur", "Nalanda", "Nawada", "Purnia", "Rohtas", "Saharsa", "Samastipur", "Saran", "Sheikhpura", "Sheohar", "Sitamarhi", "Siwan", "Supaul", "Vaishali", "West Champaran", "Balod", "Baloda Bazar", "Balrampur", "Bastar", "Bilaspur", "Dhamtari", "Durg", "Janjgir-Champa", "Jashpur", "Korba", "Koriya", "Mahasamund", "Raigarh", "Raipur", "Rajnandgaon", "Sukma", "Surajpur", "Surguja", "North Goa", "South Goa", "Ahmedabad", "Amreli", "Anand", "Banaskantha", "Bharuch", "Bhavnagar", "Dahod", "Dang", "Gandhinagar", "Jamnagar", "Junagadh", "Kutch", "Mahisagar", "Mehsana", "Narmada", "Navsari", "Panchmahal", "Patan", "Porbandar", "Rajkot", "Surat", "Tapi", "Vadodara", "Valsad", "Bilaspur", "Chamba", "Hamirpur", "Kangra", "Kinnaur", "Mandi", "Shimla", "Sirmaur", "Solan", "Una", "Bokaro", "Chatra", "Deoghar", "Dumka", "East Singhbhum", "Garhwa", "Giridih", "Godda", "Gumla", "Hazaribagh", "Jamtara", "Khunti", "Koderma", "Latehar", "Lohardaga", "Pakur", "Palamu", "Ramgarh", "Ranchi", "Sahibganj", "Seraikela-Kharsawan", "Simdega", "West Singhbhum", "Bagalkot", "Ballari", "Belagavi", "Bengaluru Rural", "Bengaluru Urban", "Bidar", "Chamarajanagar", "Chikkaballapur", "Chikkamagaluru", "Chitradurga", "Dakshina Kannada", "Davangere", "Dharwad", "Gadag", "Gulbarga", "Hassan", "Haveri", "Kodagu", "Kolar", "Koppal", "Mandya", "Mysuru", "Raichur", "Ramanagara", "Shivamogga", "Tumakuru", "Udupi", "Uttara Kannada", "Yadgir", "Alappuzha", "Ernakulam", "Idukki", "Kannur", "Kasaragod", "Kottayam", "Kollam", "Kozhikode", "Malappuram", "Palakkad", "Pathanamthitta", "Thrissur", "Wayanad", "Agar Malwa", "Alirajpur", "Anuppur", "Ashoknagar", "Balaghat", "Barwani", "Betul", "Bhind", "Bhopal", "Burhanpur", "Chhindwara", "Damoh", "Datia", "Dewas", "Dhar", "Dindori", "East Nimar", "Guna", "Gwalior", "Harda", "Hoshangabad", "Jabalpur", "Jagdalpur", "Jhabua", "Katni", "Khandwa", "Khargone", "Mandla", "Mandsaur", "Morena", "Narsinghpur", "Neemuch", "Panna", "Raisen", "Rajgarh", "Ratlam", "Rewa", "Satna", "Sehore", "Shahdol", "Shajapur", "Sheopur", "Shivpuri", "Sidhi", "Singrauli", "Tikamgarh", "Ujjain", "Umaria", "Vidisha", "Ahmednagar", "Akola", "Amravati", "Aurangabad", "Beed", "Bhandara", "Buldhana", "Chandrapur", "Dhule", "Gadchiroli", "Gondia", "Hingoli", "Jalgaon", "Jalna", "Kolhapur", "Latur", "Mumbai City", "Mumbai Suburban", "Nagpur", "Nanded", "Nashik", "Osmanabad", "Palghar", "Parbhani", "Pune", "Raigad", "Ratnagiri", "Sangli", "Satara", "Sindhudurg", "Solapur", "Thane", "Wardha", "Washim", "Yavatmal", "Bishnupur", "Churachandpur", "Imphal East", "Imphal West", "Jiribam", "Kakching", "Kamjong", "Kangpokpi", "Noney", "Pherzawl", "Senapati", "Tamenglong", "Tengnoupal", "Thoubal", "Ukhrul", "East Garo Hills", "East Jaintia Hills", "East Khasi Hills", "North Garo Hills", "Ri-Bhoi", "South Garo Hills", "South West Garo Hills", "South West Khasi Hills", "West Garo Hills", "West Jaintia Hills", "West Khasi Hills", "Aizawl", "Champhai", "Kolasib", "Lawngtlai", "Mamit", "Serchhip", "Lunglei", "Dimapur", "Kohima", "Mokokchung", "Mon", "Peren", "Tuensang", "Wokha", "Zunheboto", "Angul", "Balangir", "Balasore", "Bargarh", "Bhadrak", "Boudh", "Cuttack", "Deogarh", "Dhenkanal", "Gajapati", "Ganjam", "Jagatsinghpur", "Jajpur", "Jharsuguda", "Kalahandi", "Kandhamal", "Kendrapara", "Kendujhar", "Khurda", "Koraput", "Malkangiri", "Mayurbhanj", "Nabarangpur", "Nayagarh", "Nuapada", "Puri", "Rayagada", "Sambalpur", "Sonepur", "Sundargarh", "Amritsar", "Barnala", "Bathinda", "Faridkot", "Fatehgarh Sahib", "Ferozepur", "Gurdaspur", "Hoshiarpur", "Jalandhar", "Kapurthala", "Mansa", "Moga", "Mohali", "Muktsar", "Nawanshahr", "Patiala", "Rupnagar", "Sangrur", "Sri Muktsar Sahib", "Tarn Taran", "Ajmer", "Alwar", "Banswara", "Baran", "Barmer", "Bharatpur", "Bhilwara", "Bikaner", "Bundi", "Chittorgarh", "Churu", "Dausa", "Dhaulpur", "Jaipur", "Jaisalmer", "Jalore", "Jhalawar", "Jhunjhunu", "Jodhpur", "Karauli", "Kota", "Nagaur", "Pali", "Rajsamand", "Sawai Madhopur", "Sikar", "Sirohi", "Tonk", "Udaipur", "East Sikkim", "North Sikkim", "South Sikkim", "West Sikkim", "Chennai", "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul", "Erode", "Kanchipuram", "Kanyakumari", "Karur", "Krishnagiri", "Madurai", "Nagapattinam", "Namakkal", "Perambalur", "Pudukkottai", "Ramanathapuram", "Salem", "Sivaganga", "Thanjavur", "Theni", "Tiruchirappalli", "Tirunelveli", "Tirupur", "Tiruvallur", "Tiruvannamalai", "Vellore", "Viluppuram", "Virudhunagar", "Adilabad", "Bhadradri Kothagudem", "Hyderabad", "Jagtial", "Jangaon", "Jayashankar Bhupalpally", "Jogulamba Gadwal", "Kamareddy", "Karimnagar", "Khammam", "Mahabubabad", "Mahabubnagar", "Mancherial", "Medak", "Medchal-Malkajgiri", "Nagarkurnool", "Nalgonda", "Nirmal", "Nizamabad", "Peddapalli", "Rajanna Sircilla", "Rangareddy", "Siddipet", "Warangal Rural", "Warangal Urban", "Wanaparthy", "Yadadri Bhuvanagiri", "Dhalai", "Gomati", "Khowai", "North Tripura", "Sepahijala", "South Tripura", "Unakoti", "West Tripura", "Agra", "Aligarh", "Ambedkar Nagar", "Amethi", "Amroha", "Auraiya", "Azamgarh", "Bahraich", "Ballia", "Balrampur", "Banda", "Barabanki", "Bareilly", "Basti", "Bijnor", "Budaun", "Bulandshahr", "Chandauli", "Chitrakoot", "Deoria", "Etah", "Etawah", "Farrukhabad", "Fatehpur", "Firozabad", "Gautam Buddh Nagar", "Ghaziabad", "Ghazipur", "Gorakhpur", "Hamirpur", "Hapur", "Hardoi", "Hathras", "Jalaun", "Jalpaiguri", "Jaunpur", "Jhansi", "Kannauj", "Kanpur Dehat", "Kanpur Nagar", "Kheri", "Lucknow", "Mau", "Meerut", "Mirzapur", "Moradabad", "Muzaffarnagar", "Pilibhit", "Pratapgarh", "Raebareli", "Rampur", "Saharanpur", "Sant Kabir Nagar", "Sant Ravidas Nagar", "Shahjahanpur", "Shamli", "Shravasti", "Siddharthnagar", "Sitapur", "Sultanpur", "Unnao", "Varanasi", "Almora", "Bageshwar", "Chamoli", "Champawat", "Dehradun", "Haridwar", "Nainital", "Pauri Garhwal", "Pithoragarh", "Rudraprayag", "Tehri Garhwal", "Udham Singh Nagar", "Uttarkashi", "Alipurduar", "Bankura", "Bardhaman", "Birbhum", "Dakshin Dinajpur", "Darjeeling", "Hooghly", "Howrah", "Jalpaiguri", "Jhargram", "Jitpur", "Kolkata", "Malda", "Murshidabad", "Nadia", "North 24 Parganas", "Purba Medinipur", "Purulia", "South 24 Parganas", "Uttar Dinajpur", "North and Middle Andaman", "South Andaman", "Nicobar", "Dadra", "Nagar Haveli", "Central Delhi", "East Delhi", "New Delhi", "North Delhi", "North East Delhi", "North West Delhi", "South Delhi", "South East Delhi", "South West Delhi", "Shahdara", "West Delhi", "Jammu", "Samba", "Kathua", "Udhampur", "Reasi", "Doda", "Ramban", "Anantnag", "Kishtwar", "Poonch", "Rajouri", "Ramban", "Srinagar", "Ganderbal", "Budgam", "Pulwama", "Kulgam", "Anantnag", "Baramulla", "Bandipora", "Shopian", "Leh", "Kargil", "Kavaratti", "Agatti", "Amini", "Androth", "Kalapeni", "Suheli", "Minicoy", "Puducherry", "Karaikal", "Mahe", "Yanam"

            )]
        }
    }
]

