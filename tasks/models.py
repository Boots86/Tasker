from __future__ import unicode_literals

from django.db import models

class Group(models.Model):
	title = models.TextField(max_length=255)
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'groups'


class Card(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	content = models.TextField(max_length=255)
	image = models.TextField(max_length=255, default='')
	has_img = models.BooleanField(default=False)
	checked = models.BooleanField(default=False)
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'cards'

