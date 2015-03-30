from django.db import models

class Member(models.Model):

	name = models.CharField(max_length = 50)
	group = models.ForeignKey('Group', related_name='members')
	password = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.id) + self.name




class Group(models.Model):

	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name




class Decision(models.Model):

	YES = 'YES'
	NO = 'NO'
	NOT_SURE = 'NS'
	NOT_DECIDED_YET = 'NDY'

	DECISION_CHOICES = {
		(YES,'YES'),
		(NO,'NO'),
		(NOT_SURE,'NOT_SURE'),
		(NOT_DECIDED_YET,'NOT_DECIDED_YET'),
	}

	member = models.ForeignKey('Member',related_name='decisions')
	create_at = models.DateTimeField(auto_now_add = True)
	decision = models.CharField(max_length = 5, choices = DECISION_CHOICES,default = NOT_DECIDED_YET)




