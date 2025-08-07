def set_url(app, cls, view_name, url_path):
    # Create view function for item list
    item_view = cls.as_view(view_name)
    # Add URL rules for list and detail views
    app.add_url_rule(f"/{url_path}/", defaults={'id': None}, view_func=item_view, methods=['GET'])
    app.add_url_rule(f"/{url_path}/", view_func=item_view, methods=['POST'])
    app.add_url_rule(f"/{url_path}/<int:id>", view_func=item_view, methods=['GET', 'PUT', 'DELETE'])
