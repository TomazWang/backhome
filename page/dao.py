# page/dao.py

from page.models import Member
from page.models import Group
from page.models import Decision


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

			elif name == 'name':
				member_list = Member.objects.filter(name__contains = value)
				return member_list

				

def makeNickName(member):

	name = member.name
	nickName = name[1:]
	print(nickName)
	member.nickName = nickName
	member.save()
