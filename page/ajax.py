# page/ajax.py
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import Http404

from page.models import Member
from page.models import Group
from page.models import Decision

from page import dao


def make_decision(request):

	if request.method != 'GET':
		raise Http404('Only GETs are allowed')

	if 'decision' not in request.GET:
		raise Http404('decision is not submitted')

	if request.session.get('member_id',False):
		member = dao.select_member(id = int(request.session["member_id"]))
		if member[0] :
			d = request.GET.get('decision',False)
			query = Decision.objects.create(member = member[0],decision = d)
			return HttpResponse("Decision compelete")
	raise Http404('member not longin')

def clear_cookie(request):
	
	request.session.clear()
	
	response = redirect('/')
	
	response.delete_cookie('key')
	response.delete_cookie('member_id')

	return response


def check_key(request):

	key = False


	if 'key' in request.COOKIES and (not key):
		key = request.COOKIES['key']

	if request.session.get('key',False) and (not key):
		key = request.session.get('key',False)

	if request.method == 'GET':
		get_data = request.GET
		if get_data.get('key',False): 	
			key = get_data.get('key',False)

	return key
