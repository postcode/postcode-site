import os, json
from postcode import app

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
	