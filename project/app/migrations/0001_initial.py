# Generated by Django 3.2.7 on 2021-09-10 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('description', models.CharField(max_length=300)),
                ('cash', models.IntegerField()),
                ('balance_type', models.CharField(choices=[
                 ('收入', '收入'), ('支出', '支出')], max_length=2)),
                ('category', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.category')),
            ],
        ),
    ]
