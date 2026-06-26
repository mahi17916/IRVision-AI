from django.db import models


class ImageProject(models.Model):
    project_name = models.CharField(max_length=150)
    satellite = models.CharField(max_length=100)
    band_type = models.CharField(max_length=100)
    location = models.CharField(max_length=150, blank=True)
    original_image = models.ImageField(upload_to="uploads/")
    enhanced_image = models.ImageField(upload_to="enhanced/", blank=True)
    status = models.CharField(max_length=30, default="Completed")
    accuracy = models.CharField(max_length=10, default="92%")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
