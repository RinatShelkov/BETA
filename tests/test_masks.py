import pytest

from src.masks import return_mask_bank_account, return_mask_cards


@pytest.mark.parametrize(
    "numbers_card, expected",
    [("1234 1234 1234 1234", "1234 12** **** 1234"), ("1234123456473215", "1234 12** **** 3215")],
)
def test_return_mask_cards(numbers_card, expected):
    assert return_mask_cards(numbers_card) == expected


@pytest.mark.parametrize(
    "numbers_card, expected",
    [("1234 1234 1234 ", "Неправильно введен номер карты"), ("1234123456473215145", "Неправильно введен номер карты")],
)
def test_return_mask_cards_invalid(numbers_card, expected):
    assert return_mask_cards(numbers_card) == expected


@pytest.mark.parametrize(
    "number_account, expected", [("1234 1234 12341 23 41 2 34", "**1234"), ("12341234121341234354", "**4354")]
)
def test_return_mask_bank_account(number_account, expected):
    assert return_mask_bank_account(number_account) == expected


@pytest.mark.parametrize(
    "number_account, expected",
    [
        ("1234 1234 12341234123", "Неправильно введен номер счета"),
        ("1234123412134123435413", "Неправильно введен номер счета"),
    ],
)
def test_return_mask_bank_account_invalid(number_account, expected):
    assert return_mask_bank_account(number_account) == expected
