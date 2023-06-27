import logging

from celery import shared_task

from .models import File


def parse_text(text_file):
    """Функция обработки текстового файла."""
    with open(text_file, "r") as file:
        lines = []
        for line in file:
            lines.append(line.strip())


@shared_task
def process_file(file_name):
    logger = logging.getLogger("celery")
    try:
        file = File.objects.get(name=file_name)
        # функции обработки
        file.processed = True
        file.save()
        logger.info("Файл успешно обработан")
    except File.DoesNotExist as error:
        logger.error(f"Возникла проблема во время обработки фала! {error} ")
