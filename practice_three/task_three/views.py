import random
import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def heads_or_tails(request, number_throws: int):

    coin: list = ["heads", "tails"]

    resalt: list[str] = []

    for _ in range(number_throws):
        resalt.append(random.choice(coin))

    logger.info(f'heads_or_tails page accessed, get message: {resalt}')

    context = {
        "title": "Игра орел или решка",
        "resalt": resalt,
        "number_throws": number_throws
    }

    return render(request, "task_three_heads_or_tails.html", context)


def playing_dice(request, number_throws: int):

    start: int = 1
    stop: int = 6

    resalt: list[int] = []

    for _ in range(number_throws):
        resalt.append(get_random_number(start=start, stop=stop))

    logger.info(f'playing_dice page accessed, get message: {str(resalt)}')

    context = {
        "title": "Игра брось игральный кубик",
        "resalt": resalt,
        "number_throws": number_throws
    }

    return render(request, "task_three_playing_dice.html", context)


def random_number(request, number_throws: int):

    start: int = 0
    stop: int = 100

    resalt: list[int] = []

    for _ in range(number_throws):
        resalt.append(get_random_number(start=start, stop=stop))

    logger.info(f'playing_dice page accessed, get message: {str(resalt)}')

    context = {
        "title": f"Игра получи случайное число от {start} до {stop}",
        "resalt": resalt,
        "number_throws": number_throws
    }

    return render(request, "task_three_random_number.html", context)



def get_random_number(start: int, stop: int) -> int:
    return random.randint(start, stop)