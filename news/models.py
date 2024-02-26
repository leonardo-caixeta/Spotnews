from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    role = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


def validate_title(value):
    if len(value.split()) < 2:
        raise ValidationError(_("O título deve conter pelo menos 2 palavras."))


class News(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, validators=[validate_title]) # NOQA
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news") # NOQA
    created_at = models.DateField(blank=False, null=False)
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    categories = models.ManyToManyField("Category", related_name="news", blank=False) # NOQA

    def clean(self):
        if not self.content.strip():
            raise ValidationError({'content': ['Este campo não pode estar vazio.']}) # NOQA

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
