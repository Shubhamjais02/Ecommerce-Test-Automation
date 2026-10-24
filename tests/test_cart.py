import pytest

from data.test_data import PRODUCT_SEARCH_TERM, VALID_EMAIL, VALID_PASSWORD

def test_add_products(cart_page, home_page, products_page):
    home_page.navigate()
    home_page.click_products()
    products_page.hover_over_first_product()
    products_page.click_continue_shopping()
    products_page.hover_over_second_product()
    products_page.click_view_cart()
    cart_page.verify_cart_has_products(2)

    cart_page.verify_product_in_cart(
        product_name="Blue Top",
        expected_price="Rs. 500",
        expected_quantity=1,
        expected_total="Rs. 500"
    )

    cart_page.verify_product_in_cart(
        product_name="Men Tshirt",
        expected_price="Rs. 400",
        expected_quantity=1,
        expected_total="Rs. 400"
    )
    
def test_product_quantity_cart(cart_page, home_page, product_detail_page):
    home_page.navigate()
    home_page.verify_home_page()
    home_page.click_view_first_product()
    product_detail_page.verify_product_details_page()
    product_detail_page.increase_quantity(quantity='4')
    product_detail_page.click_add_to_cart()
    product_detail_page.click_view_cart()
    cart_page.verify_product_quantity(expected_quantity='4')


def test_search_products_cart(home_page, products_page, cart_page, login_page):
    home_page.navigate()
    home_page.verify_home_page()
    home_page.click_products()
    
    products_page.verify_products_page()
    
    products_page.search_product(PRODUCT_SEARCH_TERM)
    products_page.verify_search_results(PRODUCT_SEARCH_TERM)
    products_page.hover_over_first_product()
    products_page.click_view_cart()
    cart_page.verify_cart_has_products(1)
    home_page.click_signup_login()
    login_page.verify_login_page()
    
    login_page.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )
    home_page.click_cart()
    cart_page.verify_cart_has_products(1)
    