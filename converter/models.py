from django.db import models
from django.contrib.auth.models import User
import os

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')
    markdown_file = models.FileField(upload_to='markdowns/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Delete files from disk when model is deleted
        if self.pdf_file:
            if os.path.isfile(self.pdf_file.path):
                os.remove(self.pdf_file.path)
        if self.markdown_file:
            if os.path.isfile(self.markdown_file.path):
                os.remove(self.markdown_file.path)
                
        super().delete(*args, **kwargs)
