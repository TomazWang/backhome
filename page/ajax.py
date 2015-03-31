# page/ajax.py
from django.shortcuts import render
from django.http import HttpResponse

from page.models import Member
from page.models import Group
from page.models import Decision


def make_decision(request):

	post_data = request.GET

	member_id = int(post_data.get('member_id',0))
	member_list = Member.objects.filter(id = member_id)

	# default page
	page = render(request,'login_page.html')


	for member in member_list:
		decision = post_data.get('decision','NDY')
		decisiton_data = Decision.objects.create(member = member, decision = decision)
		decisiton_data.save()

		# page = render(request, 'see_all.html')
