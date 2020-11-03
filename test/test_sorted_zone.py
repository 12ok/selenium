def test_sorted_zone(app):
    app.admin.open_login_page()
    app.admin.login()
    app.admin.open_page("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    countries = app.admin.get_country_from_geo_zone()
    for i in range(len(countries)):
        countries[i].click()
        zones = app.admin.get_zone_from_geo_zone()
        zones_sorted = sorted(zones)
        assert zones == zones_sorted
        app.wd.back()
        countries = app.admin.get_country_from_geo_zone()