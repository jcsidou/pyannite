from django.db import models

class Transcription(models.Model):
    video = models.FileField(upload_to='videos/')
    transcription_json = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transcription {self.id}"
