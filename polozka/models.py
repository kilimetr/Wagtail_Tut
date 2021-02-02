from django.db import models

from wagtail.core.models import Page

from wagtail.admin.edit_handlers  import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


class PolozkaPage(Page):
	templates = "polozka/polozka_page.html"
	
	picture = models.ForeignKey("wagtailimages.Image", blank = False, null = True, on_delete = models.SET_NULL, help_text = "položka obrázek", 
			  related_name = "+")
	name    = models.CharField(max_length = 100, blank = False, null = True)
	price   = models.FloatField(blank = False, null = True)
	shop    = models.CharField(max_length = 100, blank = False, null = True)
	# add_to_cart = models.


	content_panels = Page.content_panels + [
		MultiFieldPanel([
			ImageChooserPanel("picture"),
			FieldPanel("name"),
			FieldPanel("price"),
			FieldPanel("shop"),
			],
			heading = "Polozka content"),
		]


	class Meta:
		verbose_name = "Polozka_vn"
		verbose_name_plural = "Polozka_vnp"





