from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class My(models.Model):
    input_link = models.URLField(max_length=300)
    input_folder_path = models.CharField(max_length=100)

    def __str__(self):
        return self.input_folder_path

    class Meta:
        db_table = 'my'


# @receiver(post_save, sender=My)
# def selenium_uploads(sender, instance, *args, **kwargs):
#     if instance:
#         my_selen()
