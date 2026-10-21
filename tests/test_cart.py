import pytest

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
    
@pytest.mark.check
def test_product_quantity_cart(cart_page, home_page, products_page, product_detail_page):
    home_page.navigate()
    home_page.verify_home_page()
    home_page.click_view_first_product()
    product_detail_page.verify_product_details_page()
    product_detail_page.increase_quantity(quantity='4')
    product_detail_page.click_add_to_cart()
    product_detail_page.click_view_cart()
    cart_page.verify_product_quantity(expected_quantity='4')
    
