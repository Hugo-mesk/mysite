from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock

class PortifolioItemBlock(blocks.StructBlock):
    document =  DocumentChooserBlock(required=False)
    image = ImageChooserBlock(required=False)
    heading = blocks.CharBlock(classname="full title", required=False)
    subheading = blocks.CharBlock(classname="full title", required=False)
    paragraph = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'resources/portifolio_item.html'
        label = 'Portifolio Item'

class PortifolioColumnBlock(blocks.StructBlock):

    left_column = PortifolioItemBlock(icon='arrow-right',
                                      label='Left column content',
                                      required=False)
    center_column = PortifolioItemBlock(icon='arrow-right',
                                        label='Center column content',
                                        required=False)
    right_column = PortifolioItemBlock(icon='arrow-right',
                                       label='Right column content',
                                       required=False)

    class Meta:
        template = 'resources/portifolio_column.html'
        label = 'Portifolio Columns'


class PortifolioRowBlock(blocks.StreamBlock):
    row = PortifolioColumnBlock(required=False)

    class Meta:
        label = 'Portifolio Rows'


class PortifolioBlock(blocks.StructBlock):
    heading = blocks.CharBlock(classname="full title", required=False)
    paragraph = blocks.RichTextBlock(required=False)
    grid = PortifolioRowBlock(required=False)

    class Meta:
        template = 'resources/portifolio.html'
        icon = 'placeholder'
        label = 'Portifolio'


class ServiceItemBlock(blocks.StructBlock):
    heading = blocks.CharBlock(classname="full title", required=False)
    paragraph = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = 'resources/service_item.html'


class ServiceColumnBlock(blocks.StructBlock):

    left_column = ServiceItemBlock(icon='arrow-right',
                                   label='Left column content',
                                   required=False)
    center_column = ServiceItemBlock(icon='arrow-right',
                                     label='Center column content',
                                     required=False)
    right_column = ServiceItemBlock(icon='arrow-right',
                                    label='Right column content',
                                    required=False)

    class Meta:
        template = 'resources/service_column.html'
        icon = 'placeholder'
        label = 'Service Columns'

class ServiceRowBlock(blocks.StreamBlock):
    row = ServiceColumnBlock(required=False)

    class Meta:
        label = 'Service Rows'


class ServiceBlock(blocks.StructBlock):
    heading = blocks.CharBlock(classname="full title", required=False)
    paragraph = blocks.RichTextBlock(required=False)
    grid = ServiceRowBlock(required=False)

    class Meta:
        template = 'resources/service.html'
        icon = 'placeholder'
        label = 'Service'
