from django.db import models

# Category Model
class Category(models.Model):
    id = models.BigAutoField(primary_key=True)  # Auto-incrementing big integer for primary key
    name = models.CharField(max_length=255)     # Category name field

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"  # Custom table name for Category model

class Brand(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image_path = models.ImageField(upload_to='brand', null=True, blank=True, default="no_image_available.png")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brand'