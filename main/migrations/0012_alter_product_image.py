# Generated by Django 3.2.3 on 2021-05-21 12:44

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=0, size=[5000, 3000], upload_to='images/'),
        ),
    ]