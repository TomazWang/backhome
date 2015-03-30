from django.db import models

class Member(models.Model):

	name = models.CharField(max_length = 50)
	group = models.ForeignKey('Group', related_name='members')

	def __str__(self):
		return str(self.id) + self.name


class Group(models.Model):

	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name
