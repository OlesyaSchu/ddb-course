# Generated by Django 4.1.3 on 2022-12-07 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingStatus',
            fields=[
                ('bk_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=1)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('passport', models.CharField(max_length=10)),
                ('surname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('fathername', models.CharField(max_length=20)),
                ('gender', models.CharField(default='Н', max_length=1)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField(auto_now=True)),
                ('phone_number', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('guest_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('passport', models.CharField(max_length=10)),
                ('surname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('fathername', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField(auto_now=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hostels',
            fields=[
                ('hostel_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('place_type_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('PRICE', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('position_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('salary', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceHostel',
            fields=[
                ('sh_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('HOSTEL_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.hostels')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('price', models.SmallIntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRendered',
            fields=[
                ('sr_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('amount', models.SmallIntegerField()),
                ('status', models.CharField(max_length=1)),
                ('time', models.TimeField()),
                ('total_price', models.SmallIntegerField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.employee')),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.guests')),
                ('sh_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.servicehostel')),
            ],
        ),
        migrations.AddField(
            model_name='servicehostel',
            name='service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.services'),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=1)),
                ('capacity', models.SmallIntegerField()),
                ('availability', models.BooleanField()),
                ('hostel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.hostels')),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('place_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('place_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.placetype')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.room')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='hostel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.hostels'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.positions'),
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('pb_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('arrival_date', models.DateField(auto_now=True)),
                ('checkout_date', models.DateField(auto_now=True)),
                ('money_total', models.SmallIntegerField()),
                ('bk_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.bookingstatus')),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.guests')),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.places')),
            ],
        ),
    ]
