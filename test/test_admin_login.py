def test_admin_login(app):
    app.admin.open_login_page()
    app.admin.login()
