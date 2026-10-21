import pytest
from playwright.sync_api import Page

from pages.contact_page import ContactPage
from pages.signup_page import SignUpPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage

@pytest.fixture
def home_page(page: Page):
    return HomePage(page)

@pytest.fixture
def signup_page(page: Page):
    return SignUpPage(page)

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def products_page(page: Page):
    return ProductsPage(page)

@pytest.fixture
def product_detail_page(page: Page):
    return ProductDetailPage(page)

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)

@pytest.fixture
def contact_page(page: Page):
    return ContactPage(page)
    