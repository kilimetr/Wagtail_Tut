from django.db import models

from wagtail.core.models		  import Page
from wagtail.admin.edit_handlers  import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields		  import StreamField

from streams import blocks



class BlogListingPage(Page):
	# LISTING PAGE LISTS ALL THE BLOG DETAIL PAGES
	template = "blog/blog_listing_page.html"

	custom_title = models.CharField(max_length = 100, blank = False, null = False, help_text = "Overwrite the default title")

	content_panels = Page.content_panels + [
		FieldPanel("custom_title"),
	]

	def get_context(self, request, *args, **kwargs):
		# ADDING CUSTOM STUFF TO OUR CONTEXT
		context = super().get_context(request, *args, **kwargs)

		context["posts"] = BlogDetailPage.objects.live().public()

		return context



class BlogDetailPage(Page):
	# BLOG DETAIL PAGE
	template = "blog/blog_detail_page.html"

	custom_title = models.CharField(max_length = 100, blank = False, null = False, help_text = "Overwrite the default title")
	
	blog_image = models.ForeignKey("wagtailimages.Image", blank = False, null = True, related_name = "+", on_delete = models.SET_NULL)

	content = StreamField([
			("title_and_text",  blocks.TitleAndTextBlock()),
			("full_richtext",   blocks.RichtextBlock()),
			("simple_richtext", blocks.SimpleRichtextBlock()),
			("cards",           blocks.CardBlock()),
			("cta",             blocks.CTABlock()),
		])

	content_panels = Page.content_panels + [
		FieldPanel("custom_title"),
		ImageChooserPanel("blog_image"),
		StreamFieldPanel("content"),
	]


