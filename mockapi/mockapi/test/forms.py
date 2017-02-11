from flask import session, jsonify
from models import *

class FormActivity:
	"""docstring for RegForm"""
	def __init__(self, data ):
		self.data = data  			# This data is in dict format
		self.db = DBActivity()


	def register(self):
		self.db.insert_into_profile(self.data)
		# username = self.db.select_from_profile(self.data['email'])[0][1]
		self.db.close()
		# return username


	def logvalidate(self):
		verify = self.db.select_from_profile(self.data['email'])
		if verify:
			if self.data['password'] == verify[0][4]:
				session['userid'] = verify[0][0]
				session['username'] = verify[0][1]
				self.db.close()
				return "True"
			return "False1"
		return "False2"
	
	def create_slug(self):
		self.db.insert_into_slug(self.data)
		sulgid = self.db.select_from_slug(self.data['slug'])[0][0] ##it can have similar slugid 
		self.db.close()
		return sulgid

	def create_slug_version(self):
		self.db.insert_into_slug_version(self.data)
		slugversionid = self.db.select_from_slug_version(self.data['slugid'],self.data['version'])[0][0] #it can have 
		self.db.close()
		return slugversionid

	def select_json(self):
		slug = self.db.select_from_slug(self.data['slug'])
		slugvesion = self.db.select_from_slug_version(slug[0][0], self.data['version'])
		self.db.close()
		# session['slugversionid'] = slugvesion[0][0]
		return slugvesion[0][3], slugvesion[0][0]

	def update_slug_jsondata(self):
		self.db.update_slug_jsondata(self.data['jsondata'], session['slugversionid'])
		self.db.close()

	def select_profile(self):
		details = self.db.select_from_profile_by_id(self.data['userid'])
		details = {
			'username' : details[0][1],
			'fullname' : details[0][2],
			'email' : details[0][3]
		}
		self.db.close()
		return details

	def select_all_slug_data(self):
		details = self.db.select_all_slug_version()
		self.db.close()
		return details
	
	# def update_slug_version_id(self):
		# slugid = self.db.select_from_slug(self.data['slug'])[0][0]
		# slugversionid = self.db.select_from_slug_version(slugid, self.data['version'])[0][0]
		# print slugversionid
		# print self.data['jsondata']
		# if slugversionid:
		# 	self.db.update_slug_jsondata(self.data['jsondata'], slugversionid)
		# else:
		# 	self.db.insert_into_slug_new_version(slugid,self.data['jsondata'], self.data['version'])
		# data = self.db.select_from_slug_version2(slugversionid)
		# print data
		# self.db.close()
		# return data

	def update_slug_version_id(self):
		slug_version = self.db.select_from_slug_version2(self.data['versionid'])

		if slug_version[0][2] == self.data['version']:
			self.db.update_slug_jsondata(self.data['jsondata'], self.data['versionid'])
		else : 
			self.db.insert_into_slug_new_version(slug_version[0][1], self.data['version'], self.data['jsondata'])
