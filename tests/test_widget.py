import pytest

from src.widget import return_mask_card_account, return_date_from_str


@pytest.mark.parametrize("information_on_card, expected",
                         [("Счет 73654108430135874305", "Счет  **4305"),
                          ("Visa Classic 6831982476737658", "Visa Classic  6831 98** **** 7658")
                          ])
def test_return_mask_card_account(information_on_card, expected):
    assert return_mask_card_account(information_on_card) == expected


@pytest.mark.parametrize("information_on_card, expected",
                         [("Счет 7365410843013587430", "Неправильно введены данные номер карты/счета"),
                          ("Visa Classic 683198247673765813", "Неправильно введены данные номер карты/счета")
                          ])
def test_return_mask_card_account_invalid(information_on_card, expected):
    assert return_mask_card_account(information_on_card) == expected


@pytest.mark.parametrize("string_with_date, expected", [("2018-07-11T02:26:18.671407", "11.07.2018"),
                                                        ("2019-06-10T02:26:18.671407", "10.06.2019")])
def test_return_date_from_str(string_with_date, expected):
    assert return_date_from_str(string_with_date) == expected
