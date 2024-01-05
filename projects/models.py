from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=100)
	introtext = models.CharField(max_length=200, blank=True)
	description = models.TextField()
	technology = models.CharField(max_length=200)
	githuburl = models.URLField(max_length=250, blank=True)
	livesite = models.URLField(max_length=250, blank=True)

	# image = models.FilePathField(path="/img")
	image = models.FileField(upload_to="project_images/", blank=True)

	def __str__(self):
		return self.title
	

