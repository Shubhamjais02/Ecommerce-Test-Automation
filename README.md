
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
| Products | 4 |
| Cart | 3 |
| Checkout | 5 |
| Contact | 1 |

```
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
```

## Installation

```bash
git clone <repository>
cd automationexercise-playwright

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

playwright install