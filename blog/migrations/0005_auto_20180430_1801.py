# Generated by Django 2.0.3 on 2018-04-30 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180430_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, max_length=160, null=True, verbose_name='Краткое описание')),
                ('to_publish', models.BooleanField(default=True, verbose_name='Опубликовать')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='post',
            name='to_publish',
            field=models.BooleanField(default=True, verbose_name='Опубликовать'),
        ),
        migrations.AddField(
            model_name='post',
            name='rubric',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='blog.Rubric', verbose_name='Рубрика'),
            preserve_default=False,
        ),
    ]