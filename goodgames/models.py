from django.db import models

# Create your models here.
class Team(models.Model):
    text = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __str__(self):
        return '(%s) %s' % (self.question.text, self.text)


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    SEX = (
        ('01', 'male'),
        ('02', 'female')
    )
    type = models.CharField(max_length=2, choices=SEX, default='01')
    birthday = models.DateField()
    phone1 = models.CharField(max_length=10)
    phone2 = models.CharField(max_length=10)
    province = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

