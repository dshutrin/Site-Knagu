from django.db import models

# Create your models here.
class Team(models.Model):
	title = models.CharField(max_length=50)
	normalized_title = models.CharField(max_length=60, default='')

	score1 = models.BooleanField()
	score2 = models.BooleanField()
	score3 = models.BooleanField()
	score4 = models.BooleanField()
	score5 = models.BooleanField()
	score6 = models.BooleanField()

	step_1_score = models.IntegerField(default=0)
	step_2_score = models.IntegerField(default=0)
	step_3_score = models.IntegerField(default=0)
	step_4_score = models.IntegerField(default=0)
	step_5_score = models.IntegerField(default=0)
	step_6_score = models.IntegerField(default=0)

	all_score = models.IntegerField(default=0)

	style = models.TextField(default="")

	def __str__(self):
		return self.title


class Step(models.Model):
	coef = models.IntegerField(default=100)


class Sub(models.Model):
	value = models.BooleanField(default=False)