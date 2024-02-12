# визначаємо курс обміну між різними валютами, для цього
# використовуємо конвертер з сайту мінфін "https://minfin.com.ua/ua/currency/converter"
currency_exchange = {
    "USD": {"CHF": 0.85, "EUR": 0.91},
    "EUR": {"CHF": 0.92, "USD": 1.07},
    "CHF": {"USD": 1.11, "EUR": 1.03},
}


class Price:
    def __init__(self, value: int, currency: str) -> None:
        self.value: int = value
        self.currency: str = currency

    def __add__(self, other):
        # якщо використовуємо однакову валюту
        if self.currency == other.currency:
            new_value = self.value + other.value
            return Price(new_value, self.currency)
        else:
            # використовуємо конвертацію валют через проміжну валюту CHF
            converted_value = (
                self.value * currency_exchange[self.currency]["CHF"]
            )
            converted_value += (
                other.value * currency_exchange[other.currency]["CHF"]
            )
            new_value = (
                converted_value / currency_exchange[self.currency]["CHF"]
            )
            return Price(new_value, self.currency)

    # Операція віднімання цін
    def __sub__(self, other):
        if self.currency == other.currency:
            new_value = self.value - other.value
            return Price(new_value, self.currency)
        else:
            converted_value = (
                self.value * currency_exchange[self.currency]["CHF"]
            )
            converted_value -= (
                other.value * currency_exchange[other.currency]["CHF"]
            )
            new_value = (
                converted_value / currency_exchange[self.currency]["CHF"]
            )
            return Price(new_value, self.currency)

    def __str__(self):
        return f"{self.value} {self.currency}"
