# Generated by Django 5.0.2 on 2024-03-25 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_vendor_cover_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='category.jpg', upload_to='category-images')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.category')),
            ],
            options={
                'verbose_name_plural': 'Category Images',
            },
        ),
    ]
