
from __future__ import unicode_literals
from django.db import models

'''from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailsnippets.models import register_snippet
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.wagtailsearch import index
from users.models import Tutor
from users.models import Department


class WorkshopTagIndexPage(Page):
	intro = RichTextField(blank=True)
	content_panels = Page.content_panels + [
        FieldPanel('intro',classname='full'),
	]
	def get_context(self, request, *args):
		tag = request.GET.get('tag')
		workshoppages = WorkshopPage.object.filter(tags__name=tag)
		context = super(WorkshopTagIndexPage, self).get_context(request)
		context['workshops'] = workshoppages
		return context

# This class is for tagging workshops to search based on related topics
class WorkshopPageTag(TaggedItemBase):
    content_object = ParentalKey('WorkshopPage', related_name='tagged_items')

class WorkshopArchivePage(Page):

	topic = RichTextField()
	intro = RichTextField()
	tutor = models.ForeignKey(Tutor,null=True,blank=True,on_delete=models.SET_NULL)
	year  = models.DateField()
	term  = RichTextField()
	workshop_content = models.URLField(max_length=250)
	
	content_panels = Page.content_panels + [
        FieldPanel('topic'),
		FieldPanel('intro'),
		FieldPanel('tutor'),
		FieldPanel('year'),
		FieldPanel('term'),
		FieldPanel('workshop_content'),
        ]
	subpage_types=['workshop.WorkshopPage']

	def get_context(self,request):
		context = super(WorkshopArchivePage,self).get_context(request)
		workshop_pages = self.get_children().live().order_by('-year')
		context['workshops'] = workshop_pages
		return context
	
	def child_pages(self):
		return WorkshopArchivePage.objects.child_of(self).live()
        
class WorkshopPage(Page):
	
	#archive = ParentalKey('WorkshopArchivePage',related_name='Archive_Page')
	topic = RichTextField()
	intro = RichTextField()
	tutor = models.ForeignKey(Tutor,null=True,on_delete=models.SET_NULL)
	Date  = models.DatesField() # is date necessary or year is sufficient?
	term  = RichTextField()
	room  = RichTextField()
	registerLink = models.URLField(max_length=250)
	tags  = ClusterTaggableManager(through=WorkshopPageTag, blank=True)
	
	content_panels = Page.content_panels + [
        FieldPanel('topic'),
		FieldPanel('intro'),
		FieldPanel('tutor'),
		FieldPanel('year'),
		FieldPanel('term'),
		FieldPanel('room'),
		FieldPanel('registerLink'),
	
    ]
	
	search_fields = Page.search_fields + [
        index.SearchField('topic'),
		index.FilterField('year'),
		index.SearchField('term'),
    ]

	parent_page_types=['workshop.WorkshopArchivePage']
	
class WorkshopRelatedLinks(Orderable):
    page = ParentalKey('WorkshopPage', related_name='related_links')
	

class WorkshopManager(models.Manager):

	def view_upcoming_workshops(self):



@register_snippet
'''	
class Workshop(models.Model):
	#ws_id = models.AutoField(primary_key=True)
	topic = models.TextField()
	intro = models.TextField()
	content_link = models.URLField()
	#tutor = models.ForeignKey(Tutor,null = True, on_delete=models.SET_NULL)
	#department = models.ForeignKey(Department, null = True, blank = True, on_delete=models.SET_NULL)
	term = models.TextField()
	date = models.DateField()
	num_of_registered_participants = models.IntegerField(default = 0)
	num_of_actual_participants = models.IntegerField(default = 0)

	#objects=WorkshopManager()	
	
	def update_participants(self,registered,actual):
		self.num_of_registered_participants = registered
		self.num_of_actual_participants = actual
		self.save()
	
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name="Workshop"
