
import pytest
from app.cp_service import CPService, CPInsufficientError

def test_initial_balance_default():
    """初期残高がデフォルトで0であることをテスト"""
    service = CPService()
    assert service.balance == 0

def test_initial_balance_positive():
    """正の初期残高で初期化できることをテスト"""
    service = CPService(initial_balance=100)
    assert service.balance == 100

def test_initial_balance_negative_raises_error():
    """負の初期残高で初期化するとValueErrorが発生することをテスト"""
    with pytest.raises(ValueError):
        CPService(initial_balance=-10)

def test_deposit_positive_amount():
    """正の量をデポジットできることをテスト"""
    service = CPService(initial_balance=50)
    service.deposit(50)
    assert service.balance == 100

def test_deposit_zero():
    """0をデポジットしても残高が変わらないことをテスト"""
    service = CPService(initial_balance=50)
    service.deposit(0)
    assert service.balance == 50

def test_deposit_negative_amount_raises_error():
    """負の量をデポジットするとValueErrorが発生することをテスト"""
    service = CPService()
    with pytest.raises(ValueError):
        service.deposit(-10)

def test_consume_successful():
    """CPの消費が成功するケースをテスト"""
    service = CPService(initial_balance=100)
    result = service.consume(30)
    assert result is True
    assert service.balance == 70

def test_consume_exact_balance():
    """残高ぴったりのCPを消費できることをテスト"""
    service = CPService(initial_balance=50)
    result = service.consume(50)
    assert result is True
    assert service.balance == 0

def test_consume_insufficient_balance_raises_error():
    """残高不足の場合にCPInsufficientErrorが発生することをテスト"""
    service = CPService(initial_balance=20)
    with pytest.raises(CPInsufficientError):
        service.consume(30)
    assert service.balance == 20 # Ensure balance is unchanged

def test_consume_negative_amount_raises_error():
    """負の量を消費しようとするとValueErrorが発生することをテスト"""
    service = CPService(initial_balance=100)
    with pytest.raises(ValueError):
        service.consume(-10)
    assert service.balance == 100 # Ensure balance is unchanged

def test_consume_zero():
    """0を消費しても残高が変わらないことをテスト"""
    service = CPService(initial_balance=100)
    result = service.consume(0)
    assert result is True
    assert service.balance == 100
