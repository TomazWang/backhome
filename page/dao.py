# page/dao.py

from page.models import Member
from page.models import Group
from page.models import Decision

import datetime


# select member by name key words or id
def select_member(**kwargs):
	'''
	select member by name or id
	 - use kwargs id to get a queryset with only 1 member
	 - use kwargs name to get a queryset with member name contains "name"

	 '''

	# kwargs : name, id
	if kwargs is not None :

		member_list = []
		for name,value in kwargs.items():

			if name == 'id':
				member_list = Member.objects.filter(id = value)
				return member_list

			if name == 'name':
				member_list = Member.objects.filter(name__contains = value)
				return member_list
	else : 
		return False;

def makeNickName(member):

	name = member.name
	nickName = member.nickName

	if nickName != name and nickName != "家人":
		return True
		
	nickName = name[1:]
	print(nickName)
	member.nickName = nickName
	member.save()

	return True


def select_decisions(**kwargs):

	if kwargs is not None:

		decisions = None
		member = False
		isThisWeek = False
		isGetLast = False

		for name,value in kwargs.items():

			if name == 'm_id':
				member = Member.objects.get(id = value)

			if name == 'member':
				member = value

			if name == 'this_week':
				isThisWeek = value

			if name == 'get_last':
				isGetLast = value


		if member:
			if isThisWeek:
				today = datetime.date.today()
				thisMonday = today - datetime.timedelta(days=-today.weekday(), weeks=1)
				nextMonday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
				decisions = Decision.objects.filter(member = member, create_at__range = (thisMonday,nextMonday))

			else :
				# get all decision this member has made
				decisions = Decision.objects.filter(member =  member)



			if isGetLast and decisions is not None:
				return decisions.last()
			else :
				return decisions

		else:
			return None # no member select

		# decisions = Decision.objects.filter(member=m,create_at__range=(thisMonday,nextMonday))

