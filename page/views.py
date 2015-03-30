from django.shortcuts import render
from django.http import HttpResponse

from page.models import Member
from page.models import Group
from page.models import Decision
# Create your views here.



def select_page(request):

	# 1. check if login
	# check POST data

	post_data = request.POST
	member_id = post_data.get('usr_id',str(0))
	key = post_data.get('key','0')

	# page = render(request,'select_page.html')
	page = render(request,'login_page.html')

	if key == "6oHOME0NO7k3yFORpr12e" :

		# 2. pull out member data
		member = Member.objects.filter(id = member_id)

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


def select(request):

	post_data = request.POST

	member_id = post_data.get('member_id',str(0))
	member = Member.objects.filter(id=member_id)

	decision = post_data.get('decision','NDY')

	decisiton_data = Decision.objects.create(member = member, decision = decision)

	decisiton_data.save()

	page = render(request, 'see_all')