Module	Examples
Home	Home page, navigation, subscription
Authentication	Register, login, logout
Negative auth	Invalid login, existing email
Products	Product list, details, search
Cart	Add/remove/update products
Checkout	Address/order validation
Payment	Place order
Contact	Contact form + file upload
UI	Scroll, navigation
Download	Invoice
API	Product/user APIs


tests/test_cart.py

TC12 Add products
TC13 Verify product quantity
TC20 Search products + cart


tests/test_checkout.py

TC14 Register during checkout
TC15 Register before checkout
TC16 Login before checkout
TC23 Verify address
TC24 Download invoice




automationexercise-playwright/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── config/
│   └── settings.py
│
├── data/
│   ├── test_data.py
│   └── users.json
│
├── pages/
│   ├── __init__.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   ├── products_page.py
│   ├── product_detail_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── payment_page.py
│   └── contact_page.py
│
├── tests/
│   ├── test_home.py
│   ├── test_authentication.py
│   ├── test_products.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_contact.py
│
├── utils/
│   ├── __init__.py
│   ├── test_data_generator.py
│   └── helpers.py
│
├── artifacts/
│   ├── screenshots/
│   ├── videos/
│   └── traces/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE



# Automation Exercise - Playwright Python Automation Framework

End-to-end test automation framework for Automation Exercise using:

- Python
- Playwright
- Pytest
- Page Object Model
- Pytest Fixtures
- GitHub Actions
- HTML Reporting

## Features

- Page Object Model
- Reusable fixtures
- Test data management
- Dynamic test data
- Cross-browser testing
- Screenshot on failure
- Trace on failure
- HTML reports
- Smoke/regression test suites
- CI/CD using GitHub Actions

## Test Coverage

| Module | Tests |
|---|---|
| Authentication | 5 |
| Products | ... |
| Cart | ... |
| Checkout | ... |
| Contact | ... |

## Installation

```bash
git clone <repository>
cd automationexercise-playwright

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

playwright install