from django.shortcuts import render
from django.http import HttpResponse

from page.models import Member
# Create your views here.



def select(request):

	# 1. check if login
	# check POST data

	post_data = request.POST
	member_id = post_data.get('usr_id',str(0))
	key = post_data.get('key','0')

	page = render(request,'login_page.html')

	if key == "6oHOME0NO7k3yFORpr12e" :

		# 2. pull out member data
		member = Member.objects.filter(id = member_id)

		# 3. render into page
		page = render(
				request ,
				'select_page,html',
				{	
					'member':member,
				}
					)



	else :
		pass
	return page
