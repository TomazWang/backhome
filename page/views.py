from django.shortcuts import render
from django.http import HttpResponse

from page.models import Member
from page.models import Group
from page.models import Decision

from page import dao

import datetime




def select_page(request):

	# 1. check if login
	# check POST data

	member_id = 0
	key = ""

	if request.method == 'GET':
		post_data = request.GET
		member_id = post_data.get('m_id',0)
		key = post_data.get('key','0')

	else :
		member_id = request.session.get('member_id',0)
		key = request.session.get('key',"")

	# page = render(request,'select_page.html')
	page = render(request,'login_page.html')
	# output = ""

	# if True:
	if key == "6oHOME0NO7k3yFORpr12e" :

		# 2. pull out member data
		member = dao.select_member(id=member_id).first()
		# member_list = Member.objects.filter(id = member_id)

		if member:

			request.session['member_id'] = int(member.id)
			request.session['key'] = str(key)

			# 3. render into page
			page = render(
					request ,
					'select_page.html',
					{
						'member':member,
						'session':request.session['member_id'],
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






