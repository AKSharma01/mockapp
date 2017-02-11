from flask import Flask, render_template, session, redirect, request, jsonify
from flask.views import MethodView
from forms import FormActivity
import json, uuid, re

class Start(MethodView):
	def __init__(self):
		pass

	def get(self):
		return "welcome to the flask mockapi project"


class Log(MethodView):
	"""docstring for log"""
	def __init__(self):
		pass

	def get(self):
		# if 'username' in session:
		# 	return "Your r loggedin"
		# return "logout"
		pass

	def post(self):
		jsondata = request.get_json()
		reg = FormActivity(jsondata)
		if reg.logvalidate()=="True":
			data = jsonify({'data':{'userid': session['userid'], 'username' : session['username']}})
			session.pop('username')
			session.pop('userid')
			return data
		elif reg.logvalidate()=="False1":
			return jsonify({'data':'Password is wrong!'})
		return jsonify({'data':'User doesn\'t exist'})



class Reg(MethodView):
	"""docstring for Reg"""
	def __init__(self):
		pass

	def post(self):
		msg = {}
		jsondata = request.get_json()
		if re.search(r'\w+@sourceeasy.com',jsondata['email']):
			reg = FormActivity(jsondata)
			reg.register()
			return jsonify({'data':"You have been successfully registered"})
		else :
			msg = {'data' : "Mail domain should be of sourceeasy.com"}
		return jsonify(msg)


class Dashboard(MethodView):
	"""docstring for Dashboard"""
	def __init__(self):
		pass

	def get(self):
		data = {
			'welcome' : "welcome via get method.  "
		}
		return jsonify(data)

	def post(self):
		jsondata = request.get_json()
		# return jsonify({"data" : str(request.get_json()['username'])})
		msg = "welcome to Dashboard Mr. {}".format(str(request.get_json()['username']))
		userid =jsondata['userid']
		user_details = FormActivity(jsondata)
		details = user_details.select_profile()
		all_data_in_array = FormActivity(jsondata).select_all_slug_data()
		data = {
			'welcome' :msg,
			'username' : details['username'],
			'fullname' : details['fullname'],
			'email' : details['email'],
			"alldata" : all_data_in_array
			
		}
		return jsonify(data)
		# return "Sorry Session has been expired or you has been logged out"


class CreateForm(MethodView):
	"""docstring for CreateForm"""
	def __init__(self):
		pass

	def post(self):
		# if 'username' in session:
		jsondata = request.get_json()
		
		jsondata1 = {
			"userid" : jsondata['userid'],
			"slug" : uuid.uuid1().bytes.encode('base64').rstrip('=\n').replace('/', '_'),
			"title" : jsondata['title']   # change after agree
		}
		slugcreate = FormActivity(jsondata1)
		slugid = slugcreate.create_slug()
		jsondata2 = {
			"slugid" : slugid,
			"version" : jsondata['version'],
			"jsondata" : jsondata['jsondata']
		}
		slugversioncreate = FormActivity(jsondata2)
		versionid = slugversioncreate.create_slug_version()
		return jsonify({
			"data":str(versionid), 
			"title" : jsondata['title'],
			"slug": jsondata1['slug'],
			'version': jsondata2['version']
		})
		# return "Sorry Please login first"

class EditJson(MethodView):
	"""docstring for EditJson"""
	def __init__(self):
		pass

	def post(self, slug, version):
		# if 'username' in session:
		modified_json = request.get_json()
		dict_val = {
			'slug' : slug,
			'versionid' : modified_json['versionID'],
			'version' : modified_json['version'],
			'jsondata' : modified_json['jsondata']
		}
		print dict_val
		FA = FormActivity(dict_val)
		FA.update_slug_version_id();
		return jsonify({'val':'updated value of slug version'})
		
	# def put(self, slug, version):
	# 	# if 'username' in session:
	# 	jsondata = request.get_json()
	# 	if jsondata['confirm']:
	# 		data = FormActivity(jsondata)
	# 		data.update_slug_jsondata()

				
		

class ViewJson(MethodView):
	"""docstring for ViewJson"""
	def __init__(self):
		pass

	def get(self,slug,version):
		# if 'username' in session:
		dict_val = { 'slug' : slug, 'version' : version }
		data = FormActivity(dict_val)
		onlyjson,slugversionid = data.select_json()
		version_detail = {
			"jsondata" : onlyjson,
			"id" : slugversionid
		}
		return jsonify(version_detail) #return to the view page with option to update or "go back to home"

		# return "Sorry Please login first"


class Logout(MethodView):
	"""docstring for Logout"""
	def __init__(self):
		pass

	def get(self):
		data = {'data':'nothing'}
		if 'username' in session:
			# data = {'userid' : session['userid'],'username':session['username']}
			session.pop('username', None)
			session.pop('userid',None)
		return jsonify(data)
