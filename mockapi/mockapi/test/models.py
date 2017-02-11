import sqlite3 as sql
import uuid
import os
from flask import g
import datetime

class DBActivity:
	"""docstring for DBActivity"""
	def __init__(self):
		# get project folder
		# x = os.getcwd()
		# #get database folder
		# print x
		#DATABASE = x+'/test/Database/database.db'
		DATABASE = '/tmp/database.db'
		db = getattr(g, '_database', None)
		"""
		 here if db has an object of database assign 
		"""
		if db :
			db = None


		if db is None:
			self.db = g._database = sql.connect(DATABASE) #create database.db in the folder if not exist
			self.cur = self.db.cursor()
			self.cur.execute("CREATE TABLE IF NOT EXISTS profile (id varchar primary key, username varchar, fullname varchar, email varchar, password varchar)")
			self.cur.execute("CREATE TABLE IF NOT EXISTS slug (id varchar primary key, userid varchar, slug varchar, title varchar)")
			self.cur.execute("CREATE TABLE IF NOT EXISTS slug_version (id varchar primary key, slugid varchar, version varchar, jsondata JSON, date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
		else:
			self.cur = db.cursor()

		
	def insert_into_profile(self, data):
		self.cur.execute("INSERT INTO profile (id , username, fullname, email, password) VALUES (?,?,?,?,?)", (str(uuid.uuid4()), str(data['username']), str(data['fullname']), str(data['email']), str(data['password'])))
		self.db.commit()
	
	def insert_into_slug(self, data):
		self.cur.execute("INSERT INTO slug (id, userid, slug, title) VALUES (?,?,?,?)", (str(uuid.uuid4()), str(data['userid']), str(data['slug']), str(data['title'])))
		self.db.commit()

	def insert_into_slug_version(self, data):
		# print dir(self)
		self.cur.execute("INSERT INTO slug_version (id, slugid, version, jsondata, date_time) VALUES (?,?,?,?,?)",(str(uuid.uuid4()), str(data['slugid']), str(data['version']), data['jsondata'],datetime.datetime.now()))
		self.db.commit()

	def insert_into_slug_new_version(self, slugid, version, jsondata):
		# print dir(self)
		self.cur.execute("INSERT INTO slug_version (id, slugid, version, jsondata, date_time) VALUES (?,?,?,?,?)",(str(uuid.uuid4()), str(slugid), str(version), str(jsondata), datetime.datetime.now()))
		self.db.commit()

	def select_from_profile(self, email):
		self.cur.execute("SELECT * from profile where email = ?",[email])
		return self.cur.fetchall()
	
	def select_from_slug(self, slug):
		self.cur.execute("SELECT * FROM slug WHERE slug = ?", [slug])
		return self.cur.fetchall()

	def select_from_slug_version2(self, versionid):
		self.cur.execute("SELECT * FROM slug_version WHERE id = ?", [versionid])
		return self.cur.fetchall()

	def select_from_slug_version(self, slugid, version):
		self.cur.execute("SELECT * FROM slug_version WHERE slugid = ? AND version = ?", (slugid, version))
		return self.cur.fetchall()
		

	def select_from_profile_by_id(self, userid):
		self.cur.execute("SELECT * FROM profile WHERE id = ?",[userid])
		return self.cur.fetchall()

	def select_all_slug_version(self):
		self.cur.execute("SELECT slug.slug, slug.title, slug_version.* FROM slug LEFT JOIN slug_version ON slug_version.slugid = slug.id");
		return self.cur.fetchall()
	
	def update_slug_jsondata(self, json, slugversionid):
		self.cur.execute("UPDATE slug_version SET jsondata = ? WHERE id =  ?", (str(json), str(slugversionid)))
		self.db.commit()

	# def select(self):
	# 		self.cur.execute("SELECT * from jsondb")
	# 		return self.cur.fetchall()

	# def selectByHash(self, hash):
	# 	self.cur.execute("SELECT * from jsondb where data = ?",[hash])
	# 	return self.cur.fetchall()

	def close(self):
		self.db.close()

