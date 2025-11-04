from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
    
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    
    def should_be_product_added_to_basket_message(self):
        product_name = self.get_product_name()
        message_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == message_product_name, \
            f"Product name in message doesn't match. Expected: '{product_name}', got: '{message_product_name}'"
    
    def should_be_basket_total_message(self):
        product_price = self.get_product_price()
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, \
            f"Basket total doesn't match product price. Expected: '{product_price}', got: '{basket_total}'"
