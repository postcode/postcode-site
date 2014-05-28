from postcode import helpers, app
# Register your filter here!
app.jinja_env.filters['get_product'] = helpers.get_product
app.jinja_env.filters['get_api_stats'] = helpers.get_api_stats