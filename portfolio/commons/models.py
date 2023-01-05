
from datetime import timezone
from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,related_name='%(class)s_createdby', null=True, blank=True,)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_updated_by', on_delete=models.SET_NULL,null=True, blank=True,)

    class Meta:
        abstract = True