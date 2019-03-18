# Generated by Django 2.1.7 on 2019-03-18 00:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20190317_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portifolioindex',
            name='body',
            field=wagtail.core.fields.StreamField([('service', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('grid', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('subheading', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], icon='arrow-right', label='Left column content', required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('subheading', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], icon='arrow-right', label='Right column content', required=False))], required=False))]))]),
        ),
    ]