def test_sorted_countries(app):
    app.admin.open_login_page()
    app.admin.login()
    app.admin.open_page("http://localhost/litecart/admin/?app=countries&doc=countries")
    countries = app.admin.get_list_countries()
    countries_sorted = sorted(countries)
    assert countries == countries_sorted
    list_zone = app.admin.get_list_countries_with_zone()
    for zone in list_zone:
        app.admin.open_page(zone)
        zones = app.admin.get_list_zone()
        zones_sorted = sorted(zones)
        assert zones == zones_sorted