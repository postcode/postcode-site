from postcode import helpers, app
# Register your filter here!
app.jinja_env.filters['get_product'] = helpers.get_product
