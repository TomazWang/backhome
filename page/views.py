from django.shortcuts import render
from django.http import HttpResponse

from page.models import Member
from page.models import Group
from page.models import Decision

from page import dao

import datetime




def select_page(request):

	# page = render(request,'select_page.html')
	page = render(request,'login_page.html')
	# output = ""

	# 1. check if login

	member_id = 0
	key = ""

	# check member_id and login
	if request.method == 'GET':
		get_data = request.GET
		if get_data.get('m_id',False):
			member_id = get_data.get('m_id',0)
		if get_data.get('key',False): 	
			key = get_data.get('key','0')
	else :
		return page

	if request.session.get('member_id',False):
		member_id = request.session.get('member_id',0)

	if request.session.get('key',False):
		key = request.session.get('key',"")




	
	# if True:
	if key == "6oHOME0NO7k3yFORpr12e" :

		# 2. pull out member data
		member = dao.select_member(id=member_id).first()
		# member_list = Member.objects.filter(id = member_id)

		if member:

			request.session['member_id'] = int(member.id)
			request.session['key'] = str(key)

			# check if this member has made decision this week
			decision = dao.select_decisions(member = member,this_week = True,get_last = True)

			if decision is not None:



			# 3. render into page
			page = render(
					request ,
					'select_page.html',
					{
						'member':member,
						'hasDecide': hasDecide,
					}
						)

			# output += member.name


	else :
		pass
	return page
	# return HttpResponse(output)



def see_all(request):


	# output = ""
	groups = []

	for group in Group.objects.all():
		members = []
		members_yes = []
		members_no = []

		for m in Member.objects.filter(group = group):


			decision = dao.select_decisions(
					member = m,
					this_week = True,
					get_last = True
					)

			if decision is not None :
				if decision.decision == True:
					members_yes.append((m,"YES"))
				elif decision.decision == False:
					members_no.append((m,"NO"))
			else :
				members.append((m,""))


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






