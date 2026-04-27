class Jar:

    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity cannot be less then 0")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("deposit amount can't be a negative integer")
        if self._size + n > self._capacity:
            raise ValueError("Too Many Cookies")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("withdraw amount must not be a negative integer")
        if n > self._size:
            raise ValueError("Not Enough Cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
