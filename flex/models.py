from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

# FLEXIBLE PAGE

class FlexPage(Page):
	template = "flex/flex_page.html"

	# @todo add streamfields
	# content = StreamField()

	subtitle = models.CharField(max_length = 100, null = True, blank = True)

	content_panels = Page.content_panels + [
		FieldPanel("subtitle"),
	]

	class Meta:
		verbose_name = "Flex Page"
		verbose_name_plural = "Flex Pages"
