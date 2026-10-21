from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        
        self.signup_login_link = page.get_by_role(
            "link",
            name="Signup / Login"
        )
        
        self.test_cases_link = page.get_by_role(
            "link",
            name="Test Cases"
        )
        
        self.products_link = page.locator(
            "a[href='/products']"
        )
        
        self.contact_us_link = page.get_by_role(
            "link", 
            name="Contact Us"
        )
        
        self.cart_link = page.get_by_role(
            "link",
            name="Cart"
        )
        
        self.logged_in_as_text = page.get_by_text(
            "Logged in as"
        )

        self.delete_account_link = page.get_by_role(
            "link",
            name="Delete Account"
        )
        self.account_deleted_heading = page.get_by_text(
            "Account Deleted!"
        )
                
        self.continue_after_delete_button = page.locator("a[data-qa='continue-button']")
        
        self.logout_link = page.get_by_role(
            "link",
            name="Logout"
        )
        
        self.view_product = page.get_by_role(
            "link",
            name="View Product"
        )
        
    def navigate(self):
        self.page.goto("https://automationexercise.com/")

    def verify_home_page(self):
        expect(self.page).to_have_title("Automation Exercise")
    
    def click_signup_login(self):
        self.signup_login_link.click()
    
    def click_products(self):
        self.products_link.click()

    def click_cart(self):
        self.cart_link.click()

    def click_contact_us(self):
        self.contact_us_link.click()

    def click_test_cases(self):
        self.test_cases_link.click()
        
    def verify_logged_in_as(self, name: str):
        expect(self.logged_in_as_text).to_contain_text(f"Logged in as {name}")
            
    def delete_account(self):
        self.delete_account_link.click()
            
    def verify_account_deleted(self):
        expect(self.account_deleted_heading).to_be_visible()
        
    def continue_after_delete(self):
        self.continue_after_delete_button.click()
        
    def logout(self):
        self.logout_link.click()
        
    def click_view_first_product(self):
        self.view_product.first.click()
        
    