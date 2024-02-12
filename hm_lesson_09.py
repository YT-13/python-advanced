# визначаємо курс обміну між різними валютами, для цього
# використовуємо конвертер з сайту мінфін 'https://minfin.com.ua/ua/currency/converter

currency_exchange = {
    "USD": {"CHF": 0.85, "EUR": 0.91},
    "EUR": {"CHF": 0.92, "USD": 1.07},
    "CHF": {"USD": 1.11, "EUR": 1.03},
}


class Price:
    def __init__(self, value: int, currency: str) -> None:
        # ініціалізує клас Price з заданими значенням і валютою.
        self.value: int = value
        self.currency: str = currency

    def __add__(self, other):
        # виконує операцію додавання для двох об'єктів Price.
        if self.currency == other.currency:
            # Якщо валюти однакові, просто додаємо їх
            return Price(self.value + other.value, self.currency)
        else:
            # якщо валюти різні, конвертуємо до проміжної валюти CHF
            converted_value = (
                self.value * currency_exchange[self.currency]["CHF"]
            )
            converted_value += (
                other.value * currency_exchange[other.currency]["CHF"]
            )
            # визначаємо валюту результату відповідно до вимог завдання
            result_currency = (
                self.currency if self.currency != "CHF" else other.currency
            )
            return Price(
                converted_value / currency_exchange[result_currency]["CHF"],
                result_currency,
            )

    def __sub__(self, other):
        # виконує операцію віднімання для двох об'єктів Price.
        if self.currency == other.currency:
            # якщо валюти однакові, просто віднімаємо їх
            return Price(self.value - other.value, self.currency)
        else:
            # якщо валюти різні, конвертуємо до проміжної валюти CHF
            converted_value = (
                self.value * currency_exchange[self.currency]["CHF"]
            )
            converted_value -= (
                other.value * currency_exchange[other.currency]["CHF"]
            )
            # визначаємо валюту результату відповідно до вимог завдання
            result_currency = (
                self.currency if self.currency != "CHF" else other.currency
            )
            return Price(
                converted_value / currency_exchange[result_currency]["CHF"],
                result_currency,
            )

    def __str__(self):
        return f"{self.value} {self.currency}"
