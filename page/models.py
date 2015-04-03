from django.db import models

class Member(models.Model):

	name = models.CharField(max_length = 50)
	group = models.ForeignKey('Group', related_name='members')
	password = models.CharField(max_length = 100 , blank=True)
	generation = models.IntegerField(default = 1)
	gender = models.BooleanField(default = True)
	seniority = models.IntegerField(default = 1)
	nickName = models.CharField(max_length = 10,blank = True)

	def __str__(self):
		return str(self.id) +". "+ self.name


	class Meta:
		ordering = ['group','generation','seniority','-gender']

class Group(models.Model):

	name = models.CharField(max_length = 100)
	generation = models.IntegerField(default = 2)
	seniority = models.IntegerField(default = 9)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['generation','seniority']


class Decision(models.Model):

	member = models.ForeignKey('Member',related_name='decisions')
	create_at = models.DateTimeField(auto_now_add = True)

	DECISION_CHOICES = (
		(0,'No'),
		(1,'Yes'),
		(2,'Later')
	)

	decision = models.IntegerField(default = 0, choices = DECISION_CHOICES)


	def __str__(self):
		return str(self.member.name) + ": "+str(self.get_decision_display())+" @"+str(self.create_at.date())


