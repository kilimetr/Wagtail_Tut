from django.db import models

from wagtail.core.models		  import Page
from wagtail.admin.edit_handlers  import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields		  import StreamField

from streams import blocks

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from django.shortcuts					  import render

from wagtail.admin.edit_handlers import MultiFieldPanel
from wagtail.snippets.models 	 import register_snippet

from wagtail.core.models 			import Orderable
from modelcluster.fields 			import ParentalKey
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers	import InlinePanel

from modelcluster.fields import ParentalManyToManyField
from django 			 import forms


# 			STATIC
# class BlogListingPage(Page):
# 	# LISTING PAGE LISTS ALL THE BLOG DETAIL PAGES
# 	template = "blog/blog_listing_page.html"

# 	custom_title = models.CharField(max_length = 100, blank = False, null = False, help_text = "Overwrite the default title")

# 	content_panels = Page.content_panels + [
# 		FieldPanel("custom_title"),
# 	]

# 	def get_context(self, request, *args, **kwargs):
# 		# ADDING CUSTOM STUFF TO OUR CONTEXT
# 		context = super().get_context(request, *args, **kwargs)

# 		context["posts"] = BlogDetailPage.objects.live().public()

# 		return context



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

	cathegories = ParentalManyToManyField("blog.BlogCathegory", blank = True) # přidáno kvůli blog cathegory - snippet checkboxes

	content_panels = Page.content_panels + [
		FieldPanel("custom_title"),
		ImageChooserPanel("blog_image"),
		MultiFieldPanel([
			InlinePanel("blog_authors", label = "Author", min_num = 1, max_num = 4)
			],
			heading = "Author(s)",
			),
		MultiFieldPanel([
			FieldPanel("cathegories", widget = forms.CheckboxSelectMultiple)
			],
			heading = "Cathegory"),
		StreamFieldPanel("content"),
	]




			# ROUTABLE PAGE
class BlogListingPage(RoutablePageMixin, Page):
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
		context["a_special_link"] = self.reverse_subpage("latest_blog_posts")
		context["authors"] = BlogAuthor.objects.all()
		context["cathegories"] = BlogCathegory.objects.all()

		return context


	@route(r"^latest/?$", name = "latest_blog_posts") # ? znamená optional
	def latest_blog_posts_dalsinazvyexplicitniapresne(self, request, *args, **kwargs):
		context = self.get_context(self, request, *args, **kwargs)

		context["latest_posts"] = BlogDetailPage.objects.live().public()[:1]
		# context["name"]         = "Kalob Talin"
		# context["website"]      = "learnwagtail.com"

		return render(request, "blog/latest_posts.html", context)


	def get_sitemap_urls(self, request):
		# jestli to nechci zobrazit v xml sitemap stačí:
		# return []

		sitemap = super().get_sitemap_urls(request)

		sitemap.append({
				"location": self.full_url + self.reverse_subpage("latest_blog_posts"),
				"lastmod": (self.last_published_at or self.latest_revision_created_at),
				"priority": 0.9,
			})

		return sitemap



			# BLOG AUTHOR FOR SNIPPETS
class BlogAuthor(models.Model):
	name = models.CharField(max_length = 100)
	website = models.URLField(blank = True, null = True)
	image = models.ForeignKey("wagtailimages.Image", on_delete = models.SET_NULL, null = True, blank = False, related_name = "+")
	
	panels = [
		MultiFieldPanel([
			FieldPanel("name"),
			ImageChooserPanel("image"),],
			heading = "Name & Image",
		),
		MultiFieldPanel([
			FieldPanel("website"),],
			heading = "Links"
		),
	]

	def __str__(self):
		# STRING REPR OF THIS CLASS
		return self.name

	class Meta():
		verbose_name = "Blog Author"
		verbose_name_plural = "Blog AuthorsSs"

register_snippet(BlogAuthor)



			# ORDERABLES WITH SNIPPETS
class BlogAuthorsOrderable(Orderable):
	# THIS ALLOWS US TO SELECT ONE OR MORE BLOG AUTHORS FROM SNIPPETS

	page = ParentalKey("blog.BlogDetailPage", related_name = "blog_authors")
	author = models.ForeignKey("blog.BlogAuthor", on_delete = models.CASCADE)

	panels = [
		SnippetChooserPanel("author"),
		]



class BlogCathegory(models.Model):
	# BLOG CATHEGORY FOR SNIPPET
	
	name = models.CharField(max_length = 255)
	slug = models.SlugField(verbose_name = "slug", allow_unicode = 255, help_text = "Slug to identify posts by this cathegory")

	panels = [
		FieldPanel("name"),
		FieldPanel("slug"),
	]

	class Meta():
		verbose_name = "Blog CathegorY"
		verbose_name_plural = "Blog CathegoriesSs"
		ordering = ["name"]

	def __str__(self):
		return self.name

register_snippet(BlogCathegory)


