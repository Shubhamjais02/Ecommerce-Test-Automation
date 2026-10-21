from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.all_products_heading = page.get_by_text(
            "All Products"
        )
        self.product_cards = page.locator(
            ".features_items .product-image-wrapper"
        )
        self.first_product_link = page.locator(
            ".features_items .product-image-wrapper p"
        ).first
        
        self.view_product_link = page.locator(
            ".features_items .product-image-wrapper .choose"
        ).first
        
        self.no_products_found_message = page.get_by_text(
            "No products found"
        )
        self.search_results_heading = page.get_by_text(
            "Searched Products"
        )
        
        # self.add_to_cart_button = page.locator(".product-overlay .add-to-cart")
        
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        
        self.brand_list = page.locator(".brands-name .nav-stacked")
        self.brand_page_heading = page.locator(".features_items h2.title.text-center")
        
        self.view_cart = page.get_by_role(
            "link",
            name="View Cart"
        )
        self.continue_shopping = page.get_by_role(
            "button",
            name="Continue Shopping"
        )
        
    def verify_products_page(self):
        # expect(self.products_link).to_be_visible()
        expect(self.all_products_heading).to_be_visible()
        # expect(self.product_cards).to_have_count_greater_than(0)
        
    def search_product(self, product_name: str):
        self.search_input.fill(product_name)
        self.search_button.click()

    def verify_search_results(self, product_name: str):
        expect(self.search_results_heading).to_be_visible()
        expect(self.first_product_link).to_contain_text(product_name)
        
    def verify_products_list_visible(self):
        expect(self.product_cards.first).to_be_visible()
    
    def open_first_product(self):
        self.view_product_link.click()
    
    def verify_brand_list_visible(self):
        expect(self.brand_list.first).to_be_visible()
    
    def click_brand(self, brand_name: str):
        self.brand_list.get_by_text(brand_name).click()
        
    def verify_brand_page(self, brand_name: str):
        expect(self.brand_page_heading).to_contain_text(brand_name)
        
    # def click_add_to_cart(self):
    #     self.product_cards.first.hover()
    #     self.add_to_cart_button.click()
    
    def hover_over_first_product(self):
        first_product = self.product_cards.nth(0)
    
        first_product.hover()
    
        add_to_cart_button = first_product.get_by_text(
            "Add to cart",
            exact=True
        ).nth(1)
    
        add_to_cart_button.click()
    
    
    def hover_over_second_product(self):
        second_product = self.product_cards.nth(1)

        second_product.hover()

        add_to_cart_button = second_product.get_by_text(
            "Add to cart",
            exact=True
        ).nth(1)

        add_to_cart_button.click()

    def click_continue_shopping(self):
        self.continue_shopping.click()
        
    def click_view_cart(self):
        self.view_cart.click()