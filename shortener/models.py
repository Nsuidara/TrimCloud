from django.db import models

class Short(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=10, unique=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.code}]: {self.url}"