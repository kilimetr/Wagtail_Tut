from django.db import models

from wagtail.core.models import Page

from wagtail.admin.edit_handlers  import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.fields		  import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

from wagtail.core.models 		  import Orderable
from modelcluster.fields 		  import ParentalKey
from wagtail.admin.edit_handlers  import InlinePanel, MultiFieldPanel


class HomePageCarouselImages(Orderable):
	# BETWEEN 1 AND 5 IMAGES FOR THE HOME PAGE CAROUSEL

	page = ParentalKey("home.HomePage", related_name = "carousel_images")
	
	carousel_image = models.ForeignKey("wagtailimages.Image", null = True, blank = False, on_delete = models.SET_NULL, related_name = "+")

	panels = [ImageChooserPanel("carousel_image"),]


class HomePage(Page):

	templates = "home/home_page.html"

	max_count = 1

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


	class Meta:

		verbose_name = "Home Page"
		verbose_name_plural = "Home Pages"


