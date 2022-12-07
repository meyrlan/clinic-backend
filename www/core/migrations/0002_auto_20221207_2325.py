# Generated by Django 3.2.12 on 2022-12-07 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'db_table': 'departments',
            },
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='department_id',
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='department', to='core.department', verbose_name='Department'),
            preserve_default=False,
        ),
    ]