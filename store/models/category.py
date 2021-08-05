from django.db import models

class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length = 200)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()