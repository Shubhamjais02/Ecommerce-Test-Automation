from data.test_data import NAME, EMAIL, SUBJECT, MESSAGE

def test_contact_us_form(home_page, contact_page):
    home_page.navigate()
    home_page.click_contact_us()
    contact_page.verify_header()
    contact_page.fill_contact_form(
        name=NAME,
        email=EMAIL,
        subject=SUBJECT,
        message=MESSAGE
    )
    contact_page.upload_file("tests/test_file.txt")
    # contact_page.on(event:"dialog",handle_dialog)
    contact_page.submit_form()
    contact_page.verify_success_message()
    contact_page.click_home_button()
    home_page.verify_home_page()
