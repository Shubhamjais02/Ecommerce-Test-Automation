from playwright.sync_api import Page, expect

class ProductDetailPage:
    def __init__(self, page: Page):
        self.page = page
        
        
        self.product_name = page.locator(
            ".product-information h2"
        )
        self.product_category = page.locator(
            ".product-information p:has-text('Category')"
        )
        self.product_price = page.locator(
            ".product-information span span"
        )
        self.product_availability = page.locator(
            ".product-information p:has-text('Availability')"
        )
        self.product_condition = page.locator(
            ".product-information p:has-text('Condition')"
        )
        self.product_brand = page.locator(
            ".product-information p:has-text('Brand')"
        )
        self.product_quantity = page.locator("#quantity")
        self.add_to_cart_buttton = page.get_by_role(
            "button",
            name="Add to cart"
        )
        self.view_cart_link = page.get_by_role(
            "link",
            name="View Cart"
        )
        
        self.write_review_button = page.locator("a[href='#reviews']")
        
        self.review_name_input = page.locator("#name")
        self.review_email_input = page.locator("#email")
        self.review_textarea = page.locator("#review")
        self.submit_review_button = page.locator("#button-review")
        self.review_success_message = page.get_by_text(
            "Thank you for your review."    
        )
        
    def verify_product_details_page(self):
        self.page.url.__contains__("product_details/")
        # expect(self.page.url).to_contain_text("product_details/")
        
    def verify_product_details(self):
        expect(self.product_name).to_be_visible()
        expect(self.product_category).to_be_visible()
        expect(self.product_price).to_be_visible()
        expect(self.product_availability).to_be_visible()
        expect(self.product_condition).to_be_visible()
        expect(self.product_brand).to_be_visible()
        
    def verify_write_review(self):
        self.write_review_button.click()
        
    def submit_review(self, name: str, email: str, review: str):
        self.review_name_input.fill(name)
        self.review_email_input.fill(email)
        self.review_textarea.fill(review)
        self.submit_review_button.click()
    
    def verify_review_submission(self):
        expect(self.review_success_message).to_be_visible()
    
    def increase_quantity(self, quantity: str):
        self.product_quantity.fill(quantity)
        
    def click_add_to_cart(self):
        self.add_to_cart_buttton.click()
        
    def click_view_cart(self):
        self.view_cart_link.click()