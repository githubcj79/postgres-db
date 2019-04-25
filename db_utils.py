#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function, with_statement

import sys
import psycopg2
import ConfigParser

from pprint import pprint
 
def config(filename='database.ini', section='motor_prod'):
	# create a parser
	parser = ConfigParser.SafeConfigParser()

	# read config file
	parser.read(filename)

	# get section, default to postgresql
	db = dict()
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db[param[0]] = param[1]
	else:
		raise Exception('Section {0} not found in the {1} file'.format(section, filename))

	return db

def connect():
	""" Connect to the PostgreSQL database server """
	fname_ = 'connect: '

	conn = None
	try:
		# read connection parameters
		params = config()

		# connect to the PostgreSQL server
		conn = psycopg2.connect(**params)

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		return conn

def do_query(conn_, query_):
	fname_ = 'do_query: '

	column_names = list()
	data_rows = list()

	with conn_.cursor() as cursor:
		cursor.execute( query_ )
		column_names = [desc[0] for desc in cursor.description]
		for row in cursor:
			data_rows.append(row)

	return column_names, data_rows

def show_query_results(conn_, query_):
	column_names, data_rows = do_query(conn_, query_)
	print( '{fname_}query: {query_}'.format(fname_='', query_=query_) )
	print( '{fname_}Column names: {names_}'.format(fname_='', names_=column_names) )
	pprint( data_rows )
	print( '{fname_}{line_}'.format(fname_='', line_='_'*70) )


if __name__ == '__main__':
	fname_ = 'main: '
	
	conn_ = connect()
	if not conn_:
		print( '{fname_}Falló connect()'.format(fname_=fname_) )
		sys.exit(1)
	print( '{fname_}Database connection opened.'.format(fname_=fname_) )

	query_ = 'select distinct rut from traza.rut_dnd limit 30' # ok
	show_query_results(conn_, query_)

	query_ = 'select distinct rut, events, pdf from traza.rut_dnd limit 30'
	show_query_results(conn_, query_)

	query_ = "select distinct rut, events, pdf from traza.rut_dnd where rut = '96942120' limit 30"
	show_query_results(conn_, query_)

	query_ = "select distinct rut, events, pdf from traza.rut_dnd where rut = '1' limit 30"
	show_query_results(conn_, query_)

	if conn_:
		conn_.close()
		print( '{fname_}Database connection closed.'.format(fname_=fname_) )

	sys.exit(0)
