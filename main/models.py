from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Journalist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Журналист"
        verbose_name_plural = "Журналисты"


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    journalist = models.ForeignKey(Journalist, on_delete=models.SET_NULL, null=True, verbose_name="Журналист")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"