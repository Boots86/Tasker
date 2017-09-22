from __future__ import unicode_literals

from django.db import models

class Group(models.Model):
	title = models.TextField(max_length=255)
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'groups'


class Card(models.Model):
	group = models.ForeignKey(Group)
	content = models.TextField(max_length=255)
	checked = models.BooleanField(default=False);
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'cards'

