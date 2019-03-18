from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ColumnBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'home/column.html'


class ThreeColumnBlock(blocks.StructBlock):

    left_column = ColumnBlock(icon='arrow-right', label='Left column content')
    center_column = ColumnBlock(icon='arrow-right', label='Center column content')
    right_column = ColumnBlock(icon='arrow-right', label='Right column content')

    class Meta:
        template = 'home/three_column.html'
        icon = 'placeholder'
        label = 'Three Columns'


class ServiceBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    column = ColumnBlock()
    grid = ThreeColumnBlock()

    class Meta:
        template = 'home/services.html'
        icon = 'placeholder'
        label = 'Three Columns'
