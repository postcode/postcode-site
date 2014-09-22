import os, json
from postcode import app
import simplejson
import urllib2

def get_product(product, attribute = None):
	f = open(os.path.join(app.root_path, 'static/content/products.js'))
	products = json.load(f)
	product_data = products[product]
	# json_data = json.load(action_json)
	if attribute:
		attr = product_data[attribute]
	else:
		attr = product_data['blurb']
	f.close()
	return attr
	
def get_api_stats(field):
	opener = urllib2.build_opener()
	url_request = urllib2.Request('http://records.oaklandnet.com/api/request')
	json_data = simplejson.load(opener.open(url_request))
	if field in json_data:
		return json_data[field]
	else:
		return "Field does not exist"