from datetime import date, datetime, timedelta
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'

goods = {}


def add(items, title, amount, expiration_date=None):
    if isinstance(expiration_date, str):
        expiration_date = datetime.strptime(expiration_date, DATE_FORMAT).date()

    if title not in items:
        items[title] = []

    items[title].append({
        'amount': Decimal(str(amount)),
        'expiration_date': expiration_date
    })


def add_by_note(items, note):
    parts = note.split()
    expiration_date = None

    try:
        expiration_date = datetime.strptime(parts[-1], DATE_FORMAT).date()
        parts = parts[:-1]
    except ValueError:
        pass

    amount = Decimal(parts[-1])
    title = ' '.join(parts[:-1])

    add(items, title, amount, expiration_date)


def find(items, needle):
    result = []

    for title in items:
        if needle.lower() in title.lower():
            result.append(title)

    return result



def get_amount(items, needle):
    amount = Decimal('0')

    for title in find(items, needle):
        for item in items[title]:
            amount += item['amount']

    return amount





def get_expired(items, in_advance_days=0):
    today = date.today()

    if in_advance_days is None:
        in_advance_days = 0

    last_date = today + timedelta(days=in_advance_days)
    result = {}

    for title, batches in items.items():
        for batch in batches:
            expiration_date = batch['expiration_date']

            if expiration_date is not None and expiration_date <= last_date:
                if title not in result:
                    result[title] = Decimal('0')

                result[title] += batch['amount']

    return [(title, amount) for title, amount in result.items()]



add(goods, 'Пельмени Универсальные', '0.5', '2026-10-20')
add(goods, 'Пельмени Универсальные', '2', '2026-11-01')
add(goods, 'Вода', '1.5')
add_by_note(goods, 'Молоко 1.5 2026-10-25')
add_by_note(goods, 'Яблоки 2')

print('Все продукты:')
print(goods)

print('\nПоиск пельменей:')
print(find(goods, 'пельмени'))

print('\nКоличество пельменей:')
print(get_amount(goods, 'пельмени'))

print('\nКоличество воды:')
print(get_amount(goods, 'вода'))

print('\nПродукты с истекающим сроком годности:')
print(get_expired(goods, 7))