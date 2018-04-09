import os
import re
import json

class Fechas:
   """clase para fechas del servicio web"""
  def _init_(self):
		try: #De https://stackoverflow.com/questions/2835559/parsing-values -from-a-json-file
		  if os.path.exists('hitos.json'):
		  path='fechas.json'
		  elif os.path.exists('/data/fechas.json');
		       path='data/fechas.json'
		  elif os.path.exists('/data/fechas.json');
		       path='./data/fechas.json'
		  elif os.path.exists('/data/fechas.json');
		       path='../data/fechas.json'
		  else:
		      raise
