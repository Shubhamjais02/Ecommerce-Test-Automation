from playwright.sync_api import Page, expect

class SignUpPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.signup_heading = page.get_by_text(
            "New User Signup!"
        )

        self.name_input = page.locator("input[data-qa='signup-name']")
        self.email_input = page.locator("input[data-qa='signup-email']")
        self.signup_button = page.locator("button[data-qa='signup-button']")
        
        self.signup_error = page.get_by_text(
            "Email Address already exist!"
        )
        
        self.signup_info_heading = page.get_by_text(
            "Enter Account Information"
        )
        
        self.signup_info_title1 = page.locator("#uniform-id_gender1")
        self.signup_info_title2 = page.locator("#uniform-id_gender2")
        self.signup_info_password = page.locator("#password")
        self.DOB_day = page.locator("#days")
        self.DOB_month = page.locator("#months")
        self.DOB_year = page.locator("#years")
        self.signup_checkbox_newsletter = page.locator("#newsletter")
        self.signup_checkbox_offers = page.locator("#optin")
        
        self.first_name_input = page.locator("#first_name")
        self.last_name_input = page.locator("#last_name")
        self.company_input = page.locator("#company")
        self.address1_input = page.locator("#address1")
        self.address2_input = page.locator("#address2")
        self.country_select = page.locator("#country")
        self.state_input = page.locator("#state")
        self.city_input = page.locator("#city")
        self.zipcode_input = page.locator("#zipcode")
        self.mobile_number_input = page.locator("#mobile_number")
        
        self.create_account_button = page.locator("button[data-qa='create-account']")
        self.account_created_heading = page.get_by_text(
            "Account Created!"
        )
        self.continue_button = page.locator("a[data-qa='continue-button']")
        
        # self.logged_in_as_text = page.get_by_text(
        #     "Logged in as"
        # )
        
        # self.delete_account_link = page.get_by_role(
        #     "link",
        #     name="Delete Account"
        # )
        
        # self.account_deleted_heading = page.get_by_text(
        #     "Account Deleted!"
        # )
        
        # self.continue_after_delete_button = page.locator("a[data-qa='continue-button']")

    def verify_signup_page(self):
        expect(self.signup_heading).to_be_visible()

    def signup(self, name: str, email: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_button.click()

    def verify_signup_error(self):
        expect(self.signup_error).to_be_visible()
    
    def verify_signup_info_page(self):
        expect(self.signup_info_heading).to_be_visible()
        
        
    def fill_account_information(self, title: str, password: str, day: str = "10", month: str = "5", year: str = "2002", first_name: str = "first_name", last_name: str = "last_name", company: str = "company", address1: str = "address1", address2: str = "address2", country: str = "country", state: str = "state", city: str = "city", zipcode: str = "zipcode", mobile_number: str = "mobile_number"):
        if title.lower() == "mr":
            self.signup_info_title1.check()
        elif title.lower() == "mrs":
            self.signup_info_title2.check()
        else:
            raise ValueError("Invalid title. Use 'Mr' or 'Mrs'.")
        self.signup_info_password.fill(password)
        self.DOB_day.select_option(day)
        self.DOB_month.select_option(month)
        self.DOB_year.select_option(year)
        self.signup_checkbox_newsletter.check()
        self.signup_checkbox_offers.check()
        
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.company_input.fill(company)
        self.address1_input.fill(address1)
        self.address2_input.fill(address2)
        self.country_select.select_option(country)
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zipcode_input.fill(zipcode)
        self.mobile_number_input.fill(mobile_number)
        
    def create_account(self):
        self.create_account_button.click()

    def verify_account_created(self):
        expect(self.account_created_heading).to_be_visible()

    def continue_to_homepage(self):
        self.continue_button.click()
    
    # def verify_logged_in_as(self, name: str):
    #     expect(self.logged_in_as_text).to_contain_text(f"Logged in as {name}")
        
    # def delete_account(self):
    #     self.delete_account_link.click()
        
    # def verify_account_deleted(self):
    #     expect(self.account_deleted_heading).to_be_visible()
    
    # def continue_after_delete(self):
    #     self.continue_after_delete_button.click()