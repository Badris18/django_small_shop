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

class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
         return self.name

    class Meta:
        db_table = 'author'


class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title  = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student'

class MarkList(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL,null=True)
    subject_name = models.CharField(max_length=255)
    mark = models.IntegerField()

    def __str__(self):
        return self.student.name

    class Meta:
        db_table = 'mark_list'