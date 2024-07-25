from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver

class NewWorkerUser(User):
    SPECIALCISE = (
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('mobile', 'Mobile'),
    )
    age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(5), MaxValueValidator(99)])
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    developer_type = models.CharField(max_length=100, choices=SPECIALCISE)
    years_of_experience = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    salary = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3000)])
    level = models.CharField(max_length=100, blank=True)

@receiver(post_save, sender=NewWorkerUser)
def set_way(sender, instance, created, **kwargs):
    if created:
        print("Сигнал обработан пользователь создан")
        years_of_experience = instance.years_of_experience
        if years_of_experience >= 1 and years_of_experience <= 2:
            instance.level = 'Junior'
        elif years_of_experience >= 3 and years_of_experience <= 4:
            instance.level = 'Middle'
        elif years_of_experience >= 4 and years_of_experience <= 5:
            instance.level = 'Middle+'
        elif years_of_experience >= 6:
            instance.level = 'Senior'
        else:
            instance.level = 'Уровень не определен'
        instance.save()