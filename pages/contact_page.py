from playwright.sync_api import Page, expect

class ContactPage:
    def __init__(self, page: Page):
        self.page = page
    
        self.get_in_touch_header = page.locator(".contact-form .title")
        self.name_input = page.locator("input[data-qa='name']")
        self.email_input = page.locator("input[data-qa='email']")
        self.subject_input = page.locator("input[data-qa='subject']")
        self.message_textarea = page.locator("textarea[data-qa='message']")
        self.upload_file_input = page.locator("input[type='file']")
        self.submit_button = page.locator("input[data-qa='submit-button']")
        self.success_message = page.locator('.status.alert.alert-success')
        self.home_button = page.locator(".btn.btn-success")
        
    def verify_header(self):
        expect(self.get_in_touch_header).to_be_visible()
        
    def fill_contact_form(self, name, email, subject, message):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_textarea.fill(message)
        
    def upload_file(self, file_path):
        self.upload_file_input.set_input_files(file_path)
        
    def submit_form(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.submit_button.click()
        
    def verify_success_message(self):
        expect(self.success_message).to_be_visible()
        
    def click_home_button(self):
        self.home_button.click()
    