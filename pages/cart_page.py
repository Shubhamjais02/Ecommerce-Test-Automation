from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.cart_rows = page.locator("#cart_info_table tbody tr")
        self.quantity_colm = page.locator(".cart_quantity")

    def verify_cart_has_products(self, expected_count):
        expect(self.cart_rows).to_have_count(expected_count)

    def verify_product_in_cart(
        self, product_name, expected_price, expected_quantity, expected_total
    ):
        row = self.cart_rows.filter(has=self.page.get_by_text(product_name, exact=True))

        expect(row).to_have_count(1)
        expect(row.locator(".cart_price")).to_contain_text(expected_price)
        expect(row.locator(".cart_quantity button")).to_have_text(
            str(expected_quantity)
        )
        expect(row.locator(".cart_total")).to_contain_text(expected_total)
    
    def verify_product_quantity(self,expected_quantity):
        row = self.cart_rows.first
        expect(row.locator(".cart_quantity button")).to_have_text(str(expected_quantity))
        