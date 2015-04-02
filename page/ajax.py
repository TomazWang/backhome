# page/ajax.py
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import Http404

from page.models import Member
from page.models import Group
from page.models import Decision

from page import dao

import json

KEY_ANS = "AAAAA55555"

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

	return key == KEY_ANS



def search_member(request):

	'''
	search member by name(key words)
	return a set of json
	'''
	to_json=[]

	if 'member_name' in request.GET:
		member_name = request.GET.get('member_name',"")
		members = dao.select_member(name=member_name)
		if members:
			for member in members:
				mDict = {}
				mDict['name'] = member.name
				# mDict['id'] = member.id
				to_json.append(mDict)

	response = json.dumps(to_json)

	return HttpResponse(response,content_type='application/json')



def login(request):

	to_json=[]
	member = False
	key = False

	if 'member_name' in request.GET:
		member_name = request.GET.get('member_name',False)
				
		if member_name : 
			members = Member.objects.filter(name=member_name)
			if members : 
				member = members[0]
	

	jDict = {}
	jDict['status'] = 'none'

	if 'key' in request.GET:
		key = request.GET.get('key',False)

	if  (key==KEY_ANS) and member:
		jDict['member_name'] = str(member.name)
		jDict['member_id'] = int(member.id)
		jDict['key'] = key
		jDict['status'] = 'success'

	elif (key==KEY_ANS) and (not member):
		jDict['status'] = 'member_wrong'

	elif (key!=KEY_ANS) and member:
		jDict['status'] = 'key_wrong'

	else : 
		jDict['status'] = 'error'

	to_json.append(jDict)
	response = json.dumps(to_json)
	return HttpResponse(response,content_type='application/json')




