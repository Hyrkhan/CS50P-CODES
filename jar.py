class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        if self._capacity <= 0:
            raise ValueError(self._capacity)
        self.cookiejar = 0
        ...

    def __str__(self):
        return "🍪" * self.cookiejar
        ...

    def deposit(self, n):
        self.cookiejar += n
        if self.cookiejar > self.capacity:
            raise ValueError("Too much")
        ...

    def withdraw(self, n):
        if self.cookiejar >= n:
            self.cookiejar -= n
        else:
            raise ValueError("No more cookies")
        ...

    @property
    def capacity(self):
        return self._capacity
        ...

    @property
    def size(self):
        return self.cookiejar
        ...

def main():
    ...

if __name__ == "__main__":
    main()
