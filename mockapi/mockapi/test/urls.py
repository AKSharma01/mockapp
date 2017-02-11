from flask import Flask, request, render_template, url_for
from views import *

app = Flask(__name__)
app.secret_key = "mockapi.dev"

urls = [
    ('/', ['GET'], Start.as_view('view')),
	('/login', ['GET','POST'], Log.as_view('log_alllist')),								#- Login into mockapi
	('/logout', ['GET'], Logout.as_view('logout')),											#- Logout 
	('/register', ['POST'], Reg.as_view('reg_alllist')),								#- Register user to create their mockform
	('/mockapi', ['GET','POST'], Dashboard.as_view('dashboard')),							# List all the mock API s
	('/mockapi/new', ['POST'], CreateForm.as_view('createnewform')),					#- New Mock API Form
	('/mockapi/edit/<slug>/<version>', ['POST','PUT'], EditJson.as_view('editslug')),	#- Edit {{version}}
	('/mockapi/<slug>/<version>', ['GET'], ViewJson.as_view('viewmock')) 			#- View mock apis version wise
]