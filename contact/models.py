from django.db import models

from wagtail.admin.edit_handlers  import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel
from modelcluster.fields 		  import ParentalKey
from wagtail.core.fields 		  import RichTextField
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm

from wagtailcaptcha.models import WagtailCaptchaEmailForm



class FormField(AbstractFormField):
	page = ParentalKey("ContactPage", on_delete = models.CASCADE, related_name = "form_fields")



# class ContactPage(AbstractEmailForm):   BEFORE INSTALLED CAPTCHA
class ContactPage(WagtailCaptchaEmailForm):   #	AFTER INSTALLED CAPTCHA
	template = "contact/contact_page.html"

	subpage_types = [] # přidáno kvůli jaký parrent může mít children
	parent_page_types = ["home.HomePage"] # přidáno kvůli jaký parrent může mít children
	
	intro          = RichTextField(blank = True)
	thank_you_text = RichTextField(blank = True)

	content_panels = AbstractEmailForm.content_panels + [
		FieldPanel("intro"),
		InlinePanel("form_fields", label = "Form Fields"),
		FieldPanel("thank_you_text"),
		MultiFieldPanel([
			FieldRowPanel([
				FieldPanel("from_address", classname = "col6"),
				FieldPanel("to_address", classname = "col6"),
				]),
			FieldPanel("subject"),	
			],
			heading = "Email Settings"),
	]


