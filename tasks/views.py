from __future__ import unicode_literals
import json
import requests
import re
from urlparse import urlparse

from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from forms import *

class index(View):
	template_name = 'home/index.html'

	def get(self, request, *args, **kwargs):
		groupForm = GroupForm()
		cardForm = CardForm()
		groups = Group.objects.all()
		return render(request, self.template_name, {
			'group_form': groupForm,
			'groups': groups,
			'card_form': cardForm
		})

class NewGroup(View):

	def post(self, request, *args, **kwargs):
		group_form = GroupForm(request.POST)
		if group_form.is_valid():
			title = group_form.cleaned_data.get('title')
			group = Group(title=title)
			group.save()
			card_form = CardForm({
				'group_id': group.id
			})
			html = render_to_string('home/group_partial.html', {
				'group': group,
				'card_form': card_form
			})
			return HttpResponse(html)
		else:
			return HttpResponse('Error: ' + str(form.title.error_messages))

class NewCard(View):

	def post(self, request, *args, **kwargs):
		card_form = CardForm(request.POST)
		if card_form.is_valid():
			card_has_img = False
			image = ''
			content = card_form.cleaned_data.get('content')
			group_id = card_form.cleaned_data.get('group_id')
			group = Group.objects.get(id=group_id)
			url_test = re.search('(?P<url>https?://[^\s]+)', content)
			img_formats = ['jpg', 'jpeg', 'png', 'bmp', 'gif']
			if url_test:
				url = url_test.group('url')
				try:
					parsed_url = urlparse(url)
					if parsed_url.path.split('.')[1] in img_formats:
						if requests.get(url).status_code == 200:
							card_has_img = True
							image = url
							content = content.replace(url, '')
				except IndexError:
					content = content.replace(url, '<a href="' + url + '">' + url + '</a>')

			card = Card(group=group, content=content, has_img=card_has_img, image=image)
			card.save()
			html = render_to_string('home/card_partial.html', {
				'card': card
			})
			return HttpResponse(json.dumps({
				'html': html,
				'group_id': group_id	
			}))
		else:
			return HttpResponse(str(card_form.errors))


@csrf_exempt
def delCard(request):
	if request.method == 'POST':
		card_id = request.POST.get('card_id')
		deleted_card = Card.objects.filter(id=card_id).delete()
		return HttpResponse(card_id)

@csrf_exempt
def checkCard(request):
	if request.method == 'POST':
		card_id = request.POST.get('card_id')
		checked_card = Card.objects.get(id=card_id)
		checked_card.checked = True
		checked_card.save()
		return HttpResponse(card_id)

@csrf_exempt
def uncheckCard(request):
	if request.method == 'POST':
		card_id = request.POST.get('card_id')
		unchecked_card = Card.objects.get(id=card_id)
		unchecked_card.checked = False
		unchecked_card.save()
		return HttpResponse(card_id)

@csrf_exempt
def delGroup(request):
	if request.method == 'POST':
		group_id = request.POST.get('group_id')
		deleted_group = Group.objects.filter(id=group_id).delete()
		return HttpResponse(group_id)
