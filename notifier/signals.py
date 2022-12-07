from file_upload.models import BulkUpload
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=BulkUpload)
def announce_new_user(sender, instance, created, **kwargs):
    if instance.status != 'initiated':
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "file_notification", {"type": "user.file_notification",
                       "instance_id": instance.id,
                       "instance_status":instance.status,
                       "total_created":instance.total_created,
                       "total_errors":instance.total_errors,
                       "file_name":instance.file_name})
