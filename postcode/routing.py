from postcode import app, views
from views import * # Import all the functions that render templates


routing = {
#   function_name: url
	'index':{
		'url': '/'
	},
	'any_page':{
		'url': '/<page>'
	}
}


def route_url(function_name):
	methods = None
	if 'methods' in routing[function_name]:
		methods = routing[function_name]['methods']
	app.add_url_rule(routing[function_name]['url'], function_name, eval(function_name), methods = methods)

for function_name in routing:
	route_url(function_name)
