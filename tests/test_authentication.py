import pytest

from data.test_data import (
    INVALID_EMAIL,
    INVALID_PASSWORD,
    NAME,
    TITLE,
    VALID_EMAIL,
    VALID_PASSWORD,
    EMAIL
)

@pytest.mark.authentication
def test_signup(home_page, signup_page):
    home_page.navigate()
    home_page.verify_home_page()

    home_page.click_signup_login()

    signup_page.verify_signup_page()

    signup_page.signup(
        NAME,
        EMAIL
    )
    signup_page.verify_signup_info_page()
    
    signup_page.fill_account_information(TITLE, VALID_PASSWORD, day="10", month="5", year="2002", first_name="shubh", last_name="jais", company="JTC", address1="123 Main St", address2="123/225 fz", country="India", state="uttar Pradesh", city="kanpur", zipcode="123456", mobile_number="0123456789")

    signup_page.create_account()
    signup_page.verify_account_created()
    signup_page.continue_to_homepage()
    home_page.verify_logged_in_as(NAME)
    home_page.delete_account()
    home_page.verify_account_deleted()
    home_page.continue_after_delete()

@pytest.mark.logout
def test_logout(home_page, login_page):
    home_page.navigate()
    home_page.verify_home_page()

    home_page.click_signup_login()

    login_page.verify_login_page()

    login_page.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    home_page.verify_logged_in_as(NAME)
    home_page.logout()
    login_page.verify_login_page()

@pytest.mark.authentication
def test_signup_with_existing_email(home_page, signup_page):
    home_page.navigate()
    home_page.verify_home_page()

    home_page.click_signup_login()

    signup_page.verify_signup_page()

    signup_page.signup(
        NAME,
        VALID_EMAIL
    )

    signup_page.verify_signup_error()

@pytest.mark.validlogin
def test_login_with_valid_credentials(home_page, login_page):
    home_page.navigate()
    home_page.verify_home_page()

    home_page.click_signup_login()

    login_page.verify_login_page()

    login_page.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    home_page.verify_logged_in_as(NAME)
    home_page.delete_account()
    home_page.verify_account_deleted()
    home_page.continue_after_delete()

@pytest.mark.invalidlogin
def test_login_with_invalid_credentials(home_page, login_page):
    home_page.navigate()
    home_page.verify_home_page()

    home_page.click_signup_login()

    login_page.verify_login_page()

    login_page.login(
        INVALID_EMAIL,
        INVALID_PASSWORD
    )

    login_page.verify_login_error()