
class CPInsufficientError(Exception):
    """CPが不足している場合に発生する例外"""
    pass

class CPService:
    """CP（Compute Point）を管理するサービス"""

    def __init__(self, initial_balance: int = 0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._balance = initial_balance

    @property
    def balance(self) -> int:
        """現在のCP残高を返す"""
        return self._balance

    def consume(self, amount: int) -> bool:
        """
        指定された量のCPを消費する。

        Args:
            amount: 消費するCP量。

        Returns:
            消費が成功した場合は True。

        Raises:
            CPInsufficientError: CPが不足している場合。
            ValueError: amountが負の場合。
        """
        if amount < 0:
            raise ValueError("Cannot consume a negative amount.")
        if self.balance < amount:
            raise CPInsufficientError(f"Insufficient CP: Required {amount}, but have {self.balance}")
        self._balance -= amount
        return True

    def deposit(self, amount: int) -> None:
        """
        指定された量のCPを追加する。

        Args:
            amount: 追加するCP量。

        Raises:
            ValueError: amountが負の場合。
        """
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount.")
        self._balance += amount
