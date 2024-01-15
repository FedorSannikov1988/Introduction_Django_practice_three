import logging
from django.shortcuts import render


logger = logging.getLogger(__name__)


def index(request):

    ip_user = request.META.get('REMOTE_ADDR',
                               'Не удалось получить IP-адрес пользователя')
    logger.info(f'ip address user: {ip_user}, page: index')

    context = {
        "title": "Главная страница",
    }

    return render(request, "task_one/index.html", context)


def about_me(request):

    ip_user = request.META.get('REMOTE_ADDR',
                               'Не удалось получить IP-адрес пользователя')

    logger.info(f'ip address user: {ip_user}, page: about_me')

    context = {
        "title": "Обо мне",
        "name": "Фёдор"
    }

    return render(request, "task_one/about_me.html", context)
