
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords


class CalipsoContainer(models.Model):
    calipso_user = models.CharField(max_length=255)
    calipso_experiment = models.CharField(max_length=255)
    container_id = models.CharField(max_length=255)
    container_name = models.CharField(max_length=255)
    container_status = models.CharField(max_length=25)
    container_info = models.TextField()
    container_logs = models.TextField()
    guacamole_username = models.CharField(max_length=255, blank=True)
    guacamole_password = models.CharField(max_length=255, blank=True)
    vnc_password = models.CharField(max_length=255, blank=True)
    creation_date = models.DateTimeField(default=timezone.now, blank=True)
    host_port = models.CharField(max_length=255, blank=True)

    public_name = models.CharField(default='default', max_length=255)

    history = HistoricalRecords()

    class Meta:
        db_table = 'calipso_containers'

    def __str__(self):
        return self.container_name

