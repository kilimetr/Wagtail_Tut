from django.db import models

from django_extensions.db.fields import AutoSlugField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.snippets.models 	 import register_snippet
from wagtail.core.models		 import Orderable
from modelcluster.fields		 import ParentalKey
from modelcluster.models 		 import ClusterableModel



# MENUS MODEL

class MenuItem(Orderable):
	link_title      = models.CharField(blank = True, null = True, max_length = 50)
	link_url        = models.CharField(blank = True, max_length = 500)
	link_page       = models.ForeignKey("wagtailcore.Page", blank = True, null = True, related_name = "+", on_delete = models.CASCADE)
	open_in_new_tab = models.BooleanField(default = False, blank = True)

	page = ParentalKey("Menu", related_name = "menu_items")

	panels = [
		FieldPanel("link_title"),
		FieldPanel("link_url"),
		PageChooserPanel("link_page"),
		FieldPanel("open_in_new_tab"),
	]

	@property
	def link(self):
		if self.link_page:
			return self.link_page
		elif self.link_url:
			return self.link_url
		else:
			return "#"
	
	@property
	def title(self):
		if self.link_page and not self.link_title:
			return self.link_page.title
		elif self.link_title:
			return self.link_title
		else:
			return "Missing Title"
	
	# @todo properties
	# link external vs internal
	# title



@register_snippet    # je jedno jestli to použiji jako dekorátor nebo funkci
class Menu(ClusterableModel):
	# MAIN MENU ClusterableModel MODEL
	title = models.CharField(max_length = 100)
	slug  = AutoSlugField(populate_from = "title", editable = True) # stejné jako models.SlugField()

	panels = [
		MultiFieldPanel([
			FieldPanel("title"),
			FieldPanel("slug")],
			heading = "Menu"),
		InlinePanel("menu_items", label = "Menu Item")
	]

	def __str__(self):
		return self.title

