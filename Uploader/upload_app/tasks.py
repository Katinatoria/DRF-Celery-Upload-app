from celery import shared_task
from .models import File


@shared_task
def process_file(file_id):
    file = File.objects.get(id=file_id)

    with open(file.file.path, 'r') as f:
        content = f.read()
        processed_content = content.upper()

    with open(file.file.path, 'w') as f:
        f.write(processed_content)

    file.processed = True
    file.save()