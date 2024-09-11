# Generated by Django 5.1.1 on 2024-09-11 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('address', models.TextField()),
                ('contact_email', models.EmailField(max_length=255)),
                ('contact_phone', models.CharField(max_length=20)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company_logos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
