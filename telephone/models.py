from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Phone(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name='Upload a picture please', null=True)
    second_model = models.ImageField(upload_to='images/', verbose_name='Upload a second model', null=True)
    third_model = models.ImageField(upload_to='images/', verbose_name='Upload a third model', null=True)
    title = models.CharField(max_length=100)
    second_title = models.CharField(max_length=100, null=True)
    third_title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, verbose_name='Write some information', null=True)
    in_stock = models.BooleanField(default=True, verbose_name='In Stock', null=True)
    price_for_first = models.PositiveIntegerField(default=1000, null=True)
    price_for_second = models.PositiveIntegerField(default=1000, null=True)
    price_for_third = models.PositiveIntegerField(default=1000, null=True)
    sale = models.PositiveIntegerField(default=0, blank=True, verbose_name='Is has a sale?', null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    review_phone = models.ForeignKey(Phone, on_delete=models.CASCADE,
                                     related_name='review_phone')
    stars = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews', null=True)

    def __str__(self):
        return f'{self.review_phone}-{self.stars}'

# class TheMostPopularPhone(models.Model):



class Comment(models.Model):
    text = models.TextField(blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', null=True)

    def __str__(self):
        return self.text
