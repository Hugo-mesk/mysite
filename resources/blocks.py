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

    left_column = PortifolioItemBlock(icon='arrow-right', label='Left column content', required=False)
    center_column = PortifolioItemBlock(icon='arrow-right', label='Center column content', required=False)
    right_column = PortifolioItemBlock(icon='arrow-right', label='Right column content', required=False)

    class Meta:
        template = 'resources/portifolio_column.html'
        icon = 'placeholder'
        label = 'Portifolio Columns'


class PortifolioBlock(blocks.StructBlock):
    heading = blocks.CharBlock(classname="full title", required=False)
    paragraph = blocks.RichTextBlock(required=False)
    grid = PortifolioColumnBlock(required=False)

    class Meta:
        template = 'resources/portifolio.html'
        icon = 'placeholder'
        label = 'Portifolio'
