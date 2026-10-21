import pytest

from data.test_data import PRODUCT_SEARCH_TERM, NAME, EMAIL, REVIEW, BRAND_NAME, BRAND_NAME2


def test_search_product(home_page, products_page):
    
    home_page.navigate()
    home_page.verify_home_page()
    home_page.click_products()

    products_page.verify_products_page()

    products_page.search_product(PRODUCT_SEARCH_TERM)

    # products_page.verify_searched_results()

    products_page.verify_search_results(
        "Blue Top"
    )
    
@pytest.mark.smoke
def test_product_details_page(home_page, products_page, product_detail_page):
    
    home_page.navigate()
    home_page.verify_home_page()
    home_page.click_products()

    products_page.verify_products_page()
    products_page.verify_products_list_visible()
    # products_page.first_product_link_click()
    products_page.open_first_product()
    product_detail_page.verify_product_details()

@pytest.mark.review
def test_write_review(home_page, products_page, product_detail_page):
    
    home_page.navigate()
    home_page.verify_home_page()
    home_page.click_products()

    products_page.verify_products_page()
    products_page.open_first_product()
    
    product_detail_page.verify_write_review()
    
    product_detail_page.submit_review(NAME, EMAIL, REVIEW)
    product_detail_page.verify_review_submission()
    
@pytest.mark.brand_filter
def test_brand_filter(home_page, products_page):
    
    home_page.navigate()
    home_page.verify_home_page()
    home_page.click_products()

    products_page.verify_brand_list_visible()
    # products_page.print_product_names()
    products_page.click_brand(BRAND_NAME)
    products_page.verify_brand_page(BRAND_NAME)
    products_page.click_brand(BRAND_NAME2)
    products_page.verify_brand_page(BRAND_NAME2)
    