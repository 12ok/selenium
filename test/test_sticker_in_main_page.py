def test_sticker_in_main_page(app):
    app.store.open_main_page()
    cart = app.store.get_list_product()
    for i in cart:
        assert app.store.get_count_sticker(i) == 1
