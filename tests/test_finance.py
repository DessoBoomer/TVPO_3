import pytest
from finance import FinanceTracker

def test_add_income():
    t = FinanceTracker()
    t.add_income(1000)
    assert t.total_income() == 1000

def test_add_negative_income():
    t = FinanceTracker()
    with pytest.raises(ValueError):
        t.add_income(-500)

def test_add_zero_income():
    t = FinanceTracker()
    with pytest.raises(ValueError):
        t.add_income(0)

def test_add_expense():
    t = FinanceTracker()
    t.add_expense(300)
    assert t.total_expenses() == 300

def test_balance():
    t = FinanceTracker()
    t.add_income(1000)
    t.add_expense(400)
    assert t.balance() == 600

def test_balance_empty():
    t = FinanceTracker()
    assert t.balance() == 0
