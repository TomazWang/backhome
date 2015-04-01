# page/ajax.py
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from page.models import Member
from page.models import Group
from page.models import Decision

from page import dao


# def make_decision(request):

# 	post_data = request.GET

# 	member_id = int(post_data.get('member_id',0))
# 	member_list = Member.objects.filter(id = member_id)

# 	# default page
# 	page = render(request,'login_page.html')


# 	for member in member_list:
# 		decision = post_data.get('decision','NDY')
# 		decisiton_data = Decision.objects.create(member = member, decision = decision)
# 		decisiton_data.save()


		# page = render(request, 'see_all.html')
	

def make_decision(request):

	if request.method != 'GET':
		raise Http404('Only GETs are allowed')

	if 'decision' not in request.GET:
		raise Http404('decision is not submitted')

	if request.session.get('member_id',False):
		member = dao.select_member(id = int(request.session["member_id"]))
		if member[0] :
			d = request.POST.get('decision',False)
			query = Decision.objects.create(member = member[0],decision = d)
			return HttpResponse("Decision compelete")
	raise Http404('member not longin')

