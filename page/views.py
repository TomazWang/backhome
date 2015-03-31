from django.shortcuts import render
from django.http import HttpResponse

from page.models import Member
from page.models import Group
from page.models import Decision

import datetime

# Create your views here.



def select_page(request):

	# 1. check if login
	# check POST data

	post_data = request.GET
	member_id = post_data.get('usr_id',str(0))
	key = post_data.get('key','0')

	# page = render(request,'select_page.html')
	page = render(request,'login_page.html')

	if key == "6oHOME0NO7k3yFORpr12e" :

		# 2. pull out member data
		member_list = Member.objects.filter(id = member_id)

		if len(member_list) > 0 :
			# get a member
			member = member_list[0]

			# 3. render into page
			page = render(
					request ,
					'select_page.html',
					{	
						'member':member,
					}	
						)


	else :
		pass
	return page



def see_all(request):


	# output = ""
	groups = []

	for group in Group.objects.all():
		members = []
		members_yes = []
		members_no = []

		for m in Member.objects.filter(group = group):

			today = datetime.date.today()
			thisMonday = today - datetime.timedelta(days=-today.weekday(), weeks=1)
			nextMonday = today + datetime.timedelta(days=-today.weekday(), weeks=1)

			decisions = Decision.objects.filter(member=m,create_at__range=(thisMonday,nextMonday))
			decision = decisions.last()
			if decision :
				if decision.decision == "YES":
					members_yes.append((m,decision.decision))
				elif decision.decision == "NO":
					members_no.append((m,decision.decision))
			else :
				members.append((m,"NDY"))

			
			# output += str(decisions)
		if len(members_yes) > 0 : 
			members_yes.extend(members)
			members = members_yes
		if len(members_no) > 0 :
			members.extend(members_no)

		groups.append((group.name,members))
	
	# test output 
	# page = HttpResponse(groups)
	page = render(request,'see_all.html',{'groups':groups})

	return page






# select member by name key words or id
def select_member(**kwargs):

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