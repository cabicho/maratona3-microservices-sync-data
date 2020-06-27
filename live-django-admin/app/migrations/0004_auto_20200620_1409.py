# Generated by Django 3.0.6 on 2020-06-20 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200620_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('is_active', models.BooleanField(default=True, verbose_name='ativo?')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Category')),
            ],
            options={
                'verbose_name': 'produto',
            },
        ),
    ]
