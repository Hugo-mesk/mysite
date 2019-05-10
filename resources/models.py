from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from .blocks import PortifolioBlock, ServiceBlock

class Index(Page):
    portifolio = StreamField(blocks.StreamBlock([('portifolio', PortifolioBlock())],
                             required=False),
                             blank=True)
    service = StreamField(blocks.StreamBlock([('service', ServiceBlock())],
                          required=False),
                          blank=True)



    content_panels = Page.content_panels + [
        StreamFieldPanel('portifolio'),
        StreamFieldPanel('service'),
    ]
