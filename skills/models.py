from django.db import models


class SkillType(models.Model):
    title = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=64, unique=True)
    content = models.TextField()
    type = models.ForeignKey('SkillType', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
