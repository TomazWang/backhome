from django.shortcuts import render
from django.http import HttpResponse

from page.models import Member
from page.models import Group
from page.models import Decision

from page import dao

import datetime


def select_page(request):

	# response = render(request,'select_page.html')
	response = render(request,'login_page.html')
	# output = ""

	# 1. check if login

	member_id = False
	key = False

	# check member_id and login
	if request.method == 'GET':
		get_data = request.GET
		if get_data.get('m_id',False):
			member_id = get_data.get('m_id',0)
		if get_data.get('key',False): 	
			key = get_data.get('key','0')

	if 'member_id' in request.COOKIES and (not member_id):
		member_id = request.COOKIES['member_id']
		# output += str("<p>request.COOKIES['member_id'] = " + str(request.COOKIES['member_id']) + "</p>")

	if 'key' in request.COOKIES and (not key):
		key = request.COOKIES['key']
		# output += str("request.COOKIES['key'] = " + str(request.COOKIES['key']) + "</p>")

	if request.session.get('member_id',False) and (not member_id):
		member_id = request.session.get('member_id',0)
		# output += str("request.session.get('member_id',0) = " + str(request.session.get('member_id',0))+ "</p>")

	if request.session.get('key',False) and (not key):
		key = request.session.get('key',"")
		# output += str("request.session.get('key',"") = " + str(request.session.get('key',"")) + "</p>")



	
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

			hasDecided = False
			decisionStr = ""
			if decision is not None:
				hasDecided = True
				decisionStr = decision.get_decision_display

			# 3. render into response
			response = render(
					request ,
					'select_page.html',
					{
						'member':member,
						'hasDecided': hasDecided,
						'decision' : decisionStr
					}
						)

			response.set_cookie('member_id',member_id)
			response.set_cookie('key',key)

			# output += member.name


	else :
		pass
	return response
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
				md_set = (m,decision.get_decision_display())
				if decision.decision == 1:
					members_yes.append(md_set)
				elif decision.decision == 0:
					members_no.append(md_set)
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
	# response = HttpResponse(groups)
	response = render(request,'see_all.html',{'groups':groups})

	return response






