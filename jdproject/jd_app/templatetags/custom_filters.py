from django import template

register = template.Library()

CURRENCIES_SYMBOLS = {
    'rub': 'Р',
    'usd': '$',
    'eur': '€',
}


@register.filter()
def currency(value, code='eur'):
    postfix = CURRENCIES_SYMBOLS[code]
    return f'{value} {postfix}'


