
def test_menu_title(app):
    app.admin.open_login_page()
    app.admin.login()
    number = len(app.admin.get_main_menu())
    for i in range(number):
        list = app.admin.get_main_menu()
        list[i].click()
        assert app.session.is_displayed("//h1")
        number2 = len(app.admin.get_not_selected_podmenu())
        for i in range(number2):
            list_in = app.admin.get_not_selected_podmenu()
            list_in[i].click()
            assert app.session.is_displayed("//h1")
