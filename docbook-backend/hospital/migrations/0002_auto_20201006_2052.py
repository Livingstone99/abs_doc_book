# Generated by Django 3.0 on 2020-10-06 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(help_text='The company name', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_name', models.CharField(help_text='Enter the name for account', max_length=20)),
                ('Account_type', models.CharField(choices=[('M', 'Mastercard'), ('V', 'Visa')], help_text='Choose a type for the card', max_length=3)),
                ('Account_number', models.IntegerField()),
                ('Account_password', models.CharField(help_text='Enter the password', max_length=20)),
                ('Account_pin', models.SmallIntegerField()),
                ('Account_balance', models.IntegerField(help_text='The account balance')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialistType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialist_category', models.CharField(help_text='Enter the type of specialist', max_length=20)),
                ('specialist_type', models.CharField(choices=[('F', 'Freelance'), ('H', 'Hospital')], help_text='The type of specialist', max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='hospital',
        ),
        migrations.AddField(
            model_name='user',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='user-images'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='+234', max_length=15),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='hospital',
            field=models.ManyToManyField(blank=True, to='hospital.Hospital'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='Enter the date of birth', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], help_text='Enter gender', max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('patient', 'patient'), ('specialist', 'specialist'), ('doctor', 'doctor'), ('admin', 'admin'), ('technician', 'technician')], default='patient', max_length=10),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(help_text='The balance')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.OneToOneField(help_text='An id of the user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(choices=[('Hospital', 'Hospital'), ('Home', 'Home'), ('Online', 'Online')], default='Hospital', help_text='The venue for appointment', max_length=15)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('Aim', models.TextField()),
                ('alert', models.CharField(blank=True, choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], help_text='Choose the type of alert', max_length=2, null=True)),
                ('acceptance', models.BooleanField(blank=True, default=False)),
                ('reschedule_startime', models.DateTimeField(blank=True, default=models.DateTimeField())),
                ('reschedule_endtime', models.DateTimeField(blank=True, default=models.DateTimeField())),
                ('user_doctor', models.ForeignKey(blank=True, help_text='Choose the doctor', null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Doctor')),
                ('user_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_specialist', models.ForeignKey(blank=True, help_text='Choose the Specialist', null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Specialist')),
            ],
        ),
        migrations.AddField(
            model_name='specialist',
            name='specialist_type',
            field=models.ForeignKey(blank=True, help_text='choose the type of specialist', null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.SpecialistType'),
        ),
        migrations.AddField(
            model_name='user',
            name='account',
            field=models.ForeignKey(blank=True, help_text='The account details', null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Payment'),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Company'),
        ),
    ]
