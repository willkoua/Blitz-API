# Generated by Django 2.0.8 on 2019-03-20 20:25

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blitz_api', '0016_user_student_number_faculty_academic_program_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='actiontoken',
            name='data',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='historicalactiontoken',
            name='data',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='actiontoken',
            name='type',
            field=models.CharField(choices=[('account_activation', 'Account activation'), ('password_change', 'Password change'), ('email_change', 'Email change')], max_length=100, verbose_name='Type of action'),
        ),
        migrations.AlterField(
            model_name='historicalactiontoken',
            name='type',
            field=models.CharField(choices=[('account_activation', 'Account activation'), ('password_change', 'Password change'), ('email_change', 'Email change')], max_length=100, verbose_name='Type of action'),
        ),
    ]
