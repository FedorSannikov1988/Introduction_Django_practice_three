import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):

    ip_user = request.META.get('REMOTE_ADDR',
                               'Не удалось получить IP-адрес пользователя')
    logger.info(f'ip address user: {ip_user}, page: index')

    context = {
        "title": "Главная страница",
    }

    return render(request, "task_one/task_three_heads_or_tails.html", context)


def about_me(request):

    ip_user = request.META.get('REMOTE_ADDR',
                               'Не удалось получить IP-адрес пользователя')

    logger.info(f'ip address user: {ip_user}, page: about_me')

    context = {
        "title": "Обо мне",
        "name": "Фёдор"
    }

    return render(request, "task_one/about_me.html", context)
