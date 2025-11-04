import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('offer', [
    "offer0", "offer1", "offer2", "offer3", "offer4",
    "offer5", "offer6",
    pytest.param("offer7", marks=pytest.mark.xfail(reason="Known bug in offer7")),
    "offer8", "offer9"
])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket_message()
    page.should_be_basket_total_message()
