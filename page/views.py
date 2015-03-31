from django.shortcuts import render
from django.http import HttpResponse

from page.models import Member
from page.models import Group
from page.models import Decision
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


def make_decision(request):

	post_data = request.GET

	member_id = int(post_data.get('member_id',0))
	member_list = Member.objects.filter(id = member_id)

	# default page
	# page = render(request,'login_page.html')

	output = ""

	output+= str("member_id : " + str(member_id) + "<br />")
	output+= str("member_list : " + str(member_list) + "<br>")

	all_member_list = Member.objects.all()

	output += str(all_member_list)

	# test output
	return HttpResponse(output)

	for member in member_list:
		decision = post_data.get('decision','NDY')
		decisiton_data = Decision.objects.create(member = member, decision = decision)
		decisiton_data.save()

		# page = render(request, 'see_all.html')


def select_member(request):

	# use GET, input member_id = member_id
	get_data = request.GET
	member_id = get_data.get('member_id',0)
	all_member_list = Member.objects.all()
	member_list = Member.objects.filter(id = member_id)

		
