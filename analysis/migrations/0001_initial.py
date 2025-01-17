# Generated by Django 5.0.6 on 2024-09-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('pie_chart', models.TextField()),
                ('donut_chart', models.TextField()),
                ('line_chart', models.TextField()),
                ('bar_chart', models.TextField()),
                ('plot_image', models.ImageField(blank=True, null=True, upload_to='plots/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
