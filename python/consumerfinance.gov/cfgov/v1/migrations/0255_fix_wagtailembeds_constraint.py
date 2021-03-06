# Generated by Django 2.2.16 on 2021-04-07 15:47

from django.db import migrations

# This migration was a temporary fix for an inconsistency between the expected
# state of the wagtailembeds_embed table constrains and its actual state. This
# manifested as a failure of the wagtailembeds_0008_allow_long_urls migration
# to apply.
#
# This migration was successfully applied and the raw SQL required has been
# removed now that the Django ORM and database state is consistent. This
# migration is now a noop.
class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0254_delete_homepagecarouselitem'),
    ]

    run_before = [
        ('wagtailembeds', '0008_allow_long_urls'),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop, atomic=True),
    ]
