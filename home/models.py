from django.db import models

from wagtail.core.models import Page

from wagtail.admin.edit_handlers  import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.fields		  import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

from wagtail.core.models 		  import Orderable
from modelcluster.fields 		  import ParentalKey
from wagtail.admin.edit_handlers  import InlinePanel, MultiFieldPanel

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from django.shortcuts					  import render

from wagtail.api import APIField

from wagtail.admin.edit_handlers import ObjectList, TabbedInterface



class HomePageCarouselImages(Orderable):
	# BETWEEN 1 AND 5 IMAGES FOR THE HOME PAGE CAROUSEL

	page = ParentalKey("home.HomePage", related_name = "carousel_images")
	
	carousel_image = models.ForeignKey("wagtailimages.Image", null = True, blank = False, on_delete = models.SET_NULL, related_name = "+")

	panels = [ImageChooserPanel("carousel_image"),]

	# api_fields = [
	# 	APIField("carousel_images"),
	# 	APIField("a_different_field_name"),
	# ]


		# STATIC
# class HomePage(Page):

# 	templates = "home/home_page.html"

# 	max_count = 1

# 	banner_title    = models.CharField(max_length = 100, blank = False, null = True)
# 	banner_subtitle = RichTextField(features = ["bold", "italic"])
# 	banner_image    = models.ForeignKey("wagtailimages.Image", blank = False, null = True, on_delete = models.SET_NULL, related_name = "+")

# 	banner_cta = models.ForeignKey("wagtailcore.Page", blank = True, null = True, on_delete = models.SET_NULL, related_name = "+")

# 	content = StreamField(
# 			[
# 				("cta", blocks.CTABlock()),
# 			],
# 			null = True,
# 			blank = True,
# 		)

# 	content_panels = Page.content_panels + [
# 		MultiFieldPanel([
# 			FieldPanel("banner_title"), 
# 			FieldPanel("banner_subtitle"),
# 			ImageChooserPanel("banner_image"),
# 			PageChooserPanel("banner_cta"),
# 			], 
# 			heading = "Banner Options"),

# 		MultiFieldPanel([
# 			InlinePanel("carousel_images", max_num = 5, min_num = 1, label = "IMAGE"), 
# 			], 
# 			heading = "Carousel Images"),

# 		MultiFieldPanel([
# 			StreamFieldPanel("content"),
# 			],
# 			heading = "Content"),
# 		]


# 	class Meta:

# 		verbose_name = "Home Page"
# 		verbose_name_plural = "Home Pages"




			# ROUTABLE PAGE
class HomePage(RoutablePageMixin, Page):

	templates = "home/home_page.html"

	subpage_types = ["blog.BlogListingPage", "contact.ContactPage", "flex.FlexPage"] # přidáno kvůli jaký parrent může mít children
	parent_page_type = ["wagtailcore.Page"] # přidáno kvůli jaký parrent může mít children
	# max_count = 1 # přidáno kvůli jaký parrent může mít children

	banner_title    = models.CharField(max_length = 100, blank = False, null = True)
	banner_subtitle = RichTextField(features = ["bold", "italic"])
	banner_image    = models.ForeignKey("wagtailimages.Image", blank = False, null = True, on_delete = models.SET_NULL, related_name = "+")

	banner_cta = models.ForeignKey("wagtailcore.Page", blank = True, null = True, on_delete = models.SET_NULL, related_name = "+")

	content = StreamField(
			[
				("cta", blocks.CTABlock()),
			],
			null = True,
			blank = True,
		)

	api_fields = [
		APIField("banner_title"),
		APIField("banner_subtitle"),
		APIField("banner_image"),
		APIField("banner_cta"),
		APIField("carousel_images"),
		APIField("banner_cta"),
	]

	content_panels = Page.content_panels + [
		MultiFieldPanel([
			FieldPanel("banner_title"), 
			FieldPanel("banner_subtitle"),
			ImageChooserPanel("banner_image"),
			PageChooserPanel("banner_cta"),
			], 
			heading = "Banner Options"),

		MultiFieldPanel([
			InlinePanel("carousel_images", max_num = 5, min_num = 1, label = "IMAGE"), 
			], 
			heading = "Carousel Images"),

		MultiFieldPanel([
			StreamFieldPanel("content"),
			],
			heading = "Content"),
		]

	# úprava na admin pages content/promote/settings
	# promote_panels  = []
	# settings_panels = []
	sidebar_panels = [
		MultiFieldPanel([
			FieldPanel("banner_title"),
			FieldPanel("banner_subtitle"),
			ImageChooserPanel("banner_image"),
			PageChooserPanel("banner_cta")],
			heading = "Custom 1"),
		]
	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading = "Custom"),
		ObjectList(Page.promote_panels, heading = "Promotional Stuff"),
		ObjectList(Page.settings_panels, heading = "Setting Stuff"),
		ObjectList(sidebar_panels, heading = "SideBarrr Settings"),
		])


	class Meta:

		verbose_name = "Home Page"
		verbose_name_plural = "Home Pages"


	@route(r"^subscribe/$")
	def the_subscribe_page(self, request, *args, **kwargs):
		context = self.get_context(request, *args, **kwargs)

		context["a_special_test"] = "Hello World 123321"

		return render(request, "home/subscribe.html", context)

		# pojmenování Home page jinak
	def get_admin_display_title(self):
		return "Houmíček"

		# customize wagtail page property values
# HomePage._meta.get_field("title").verbose_name = "To any verbose name"
# HomePage._meta.get_field("title").help_text	   = ""
# HomePage._meta.get_field("title").default	   = "Some Default title"
# HomePage._meta.get_field("slug").default	   = "Some Default slug"







