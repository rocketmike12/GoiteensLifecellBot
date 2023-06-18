import telebot

bot = telebot.TeleBot('6292175138:AAGXtZiB2unBaOjvojxEQ9dw6cLRdyT0hLM', parse_mode=None)

tariffs = {
    'потужний': {
        'price': 100,
        'internet': 40,
        'calls_lifecell': 'unlimited',
        'calls_other': 800,
        'title': 'Потужний',
        'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/potuzhnyy/'

    },
    'інтернет_безмеж': {
        'price': 100,
        'internet': 'unlimited',
        'calls_lifecell': 'unlimited',
        'calls_other': 250,
        'title': 'Інтернет БЕЗМЕЖ',
        'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/int-bezmezh-2021/'
    },
    'дзвінкий_безмеж': {
        'price': 75,
        'internet': 0,
        'calls_lifecell': 'unlimited',
        'calls_other': 250,
        'title': 'Дзвінкий БЕЗМЕЖ',
        'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/dzvinkiy/'
    },
    'вільний_лайф_регіон': {
        'price': 150,
        'internet': 'unlimited',
        'calls_lifecell': 'unlimited',
        'calls_other': 1600,
        'title': 'Вільний Лайф. Регіон',
        'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-reg-2021/'
    },
    'вільний_лайф': {
        'price': 180,
        'internet': 'unlimited',
        'calls_lifecell': 'unlimited',
        'calls_other': 1600,
        'title': 'Вільний Лайф',
        'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/'
    },
    'смарт_лайф': {
        'price': 120,
        'internet': 25,
        'calls_lifecell': 'unlimited',
        'calls_other': 800,
        'title': 'Смарт Лайф',
        'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/'
    },
    'просто_лайф': {
        'price': 90,
        'internet': 8,
        'calls_lifecell': 'unlimited',
        'calls_other': 300,
        'title': 'Просто Лайф',
        'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/'
    },
    'platinum_лайф': {
        'price': 250,
        'internet': 'unlimited',
        'calls_lifecell': 'unlimited',
        'calls_other': 3000,
        'title': 'Platinum Лайф',
        'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/'
    },
    'шкільний_лайф': {
        'price': 150,
        'internet': 7,
        'calls_lifecell': 'unlimited',
        'calls_other': 0,
        'title': 'Шкільний Лайф',
        'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/'
    },
    'ґаджет': {
        'price': 90,
        'internet': 150,
        'calls_lifecell': 50,
        'calls_other': 0,
        'title': 'Ґаджет',
        'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/gadget-series/'
    },
    'смарт_сім\'я': {
        'price': 375,
        'internet': 20,
        'calls_lifecell': 'unlimited',
        'calls_other': 500,
        'title': 'Смарт Сім\'я',
        'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/smart-simya-series/'
    }
}
