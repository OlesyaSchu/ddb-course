# from django.db import models
from django.db.models import IntegerField, ForeignKey, UUIDField, CharField, BooleanField, SmallIntegerField, \
    DateTimeField, TimeField, Model, CASCADE, DateField, BigAutoField
from datetime import date
# Create your models here.

class PlaceType(Model):  # Таблица 3. Тип места
    place_type_id = BigAutoField(primary_key=True)               # UUID  PRIMARY KEY,
    type = CharField(max_length=100)                             # VARCHAR(100) NOT NULL,
    PRICE = SmallIntegerField()


class Places(Model):  # Таблица 4. Места
    place_id = BigAutoField(primary_key=True)                    # UUID PRIMARY KEY,
    place_type_id = ForeignKey('PlaceType', on_delete=CASCADE)   # UUID REFERENCES PLACE_TYPE ( PLACE_TYPE_ID ),
    # room_id = ForeignKey('Room', on_delete=CASCADE)              # UUID REFERENCES ROOM ( ROOM_ID )


class BookingStatus(Model):  # Таблица 6. Статус брони
    bk_id = BigAutoField(primary_key=True)                       # UUID PRIMARY KEY,
    status = CharField(max_length=1)                             # CHAR(1) CHECK(STATUS  in('A', 'B', 'C')) default 'A'
    description = CharField(max_length=100)                      # VARCHAR(100)


class Guests(Model):  # Таблица 9. Гости
    guest_id = BigAutoField(primary_key=True)                    # UUID  PRIMARY KEY,
    passport = CharField(max_length=10)
    surname = CharField(max_length=20)
    name = CharField(max_length=20)
    fathername = CharField(max_length=20)
    gender = CharField(max_length=1)                             # CHAR(1) CHECK(SEX in('М', 'Ж', 'Н')) default 'Н',
    address = CharField(max_length=100)                          # VARCHAR(100) NOT NULL,
    birthdate = DateField(auto_now=True)                         # DATE
    phone_number = CharField(max_length=11)                      # VARCHAR(11)
    email = CharField(max_length=30)                             # VARCHAR(30)


class Bookings(Model):  # Таблица 5. Брони
    pb_id = BigAutoField(primary_key=True)                       # UUID  PRIMARY KEY,
    arrival_date = DateField(auto_now=True)                      # TIMESTAMP WITH TIME ZONE NOT NULL,
    checkout_date = DateField(auto_now=True)                     # TIMESTAMP WITH TIME ZONE,
    money_total = SmallIntegerField()                            # MONEY,
    bk_id = ForeignKey('BookingStatus', on_delete=CASCADE)       # UUID    REFERENCES    BOOKING_STATUS(BK_ID),
    guest_id = ForeignKey('Guests', on_delete=CASCADE)           # UUID    REFERENCES    GUESTS(GUEST_ID),
    place_id = ForeignKey('Places', on_delete=CASCADE)           # UUID    REFERENCES    PLACES(PLACE_ID)

#
# class Hostels(Model):  # Таблица 1. Хостелы
#     hostel_id = BigAutoField(primary_key=True)
#     address = CharField(max_length=100)
#     phone = CharField(max_length=11)
#     available = BooleanField()


# class Room(Model):  # Таблица 2. Комната
#     room_id = BigAutoField(primary_key=True)                     # UUID PRIMARY KEY,
#     gender = CharField(max_length=1)                             # CHAR(1) CHECK(GENDER  in('М', 'Ж', 'Н')) default 'Н'
#     capacity = SmallIntegerField()                               # SMALLINT NOT NULL,
#     availability = BooleanField()                                # BOOLEAN NOT NULL,
#     hostel_id = ForeignKey('Hostels', on_delete=CASCADE)         # UUID REFERENCES HOSTELS( HOSTEL_ID )
#
#
# class Positions(Model):  # Таблица 8. Должности
#     position_id = BigAutoField(primary_key=True)                 # UUID  PRIMARY KEY,
#     name = CharField(max_length=50)                              # VARCHAR(50) NOT NULL,
#     salary = SmallIntegerField()                                 # MONEY

#
# class Employee(Model):  # Таблица 7. Сотрудники
#     employee_id = BigAutoField(primary_key=True)                 # UUID PRIMARY KEY,
#     passport = CharField(max_length=10)                          # VARCHAR(10) NOT NULL,
#     surname = CharField(max_length=20)                           # VARCHAR(20) NOT NULL,
#     name = CharField(max_length=20)                              # VARCHAR(20) NOT NULL,
#     fathername = CharField(max_length=20)                        # VARCHAR(20) NOT NULL,
#     gender = CharField(max_length=1, default='Н')                # CHAR(1) CHECK(GENDER  in('М', 'Ж', 'Н')) default 'Н'
#     address = CharField(max_length=100)                          # VARCHAR(100) NOT NULL,
#     birthdate = DateField(auto_now=True)                         # DATE NOT NULL,
#     position_id = ForeignKey('Positions', on_delete=CASCADE)     # UUID REFERENCES POSITIONS( POSITION_ID  ),
#     phone_number = CharField(max_length=11)                      # VARCHAR(11),
#     hostel_id = ForeignKey('Hostels', on_delete=CASCADE)         # UUID REFERENCES HOSTELS( HOSTEL_ID  )


#
# class Services(Model):  # Таблица 10. Услуги
#     service_id = BigAutoField(primary_key=True)                  # UUID  PRIMARY KEY,
#     price = SmallIntegerField()                                  # MONEY,
#     description = CharField(max_length=100)                      # VARCHAR(100)
#
#
# class ServiceHostel(Model):  # Таблица 11. Услуги в хостеле
#     sh_id = BigAutoField(primary_key=True)       #  UUID  PRIMARY KEY,
#     service_id = ForeignKey('Services', on_delete=CASCADE)       # UUID REFERENCES SERVICES( SERVICE_ID ),
#     HOSTEL_ID = ForeignKey('Hostels', on_delete=CASCADE)         # UUID REFERENCES HOSTELS( HOSTEL_ID )
#
#
# class ServiceRendered(Model):  # Таблица 12. Оказанные услуги
#     sr_id = BigAutoField(primary_key=True)                       # UUID PRIMARY KEY
#     amount = SmallIntegerField()                                 # SMALLINT,
#     status = CharField(max_length=1)                             # CHAR(1) CHECK(STATUS in('A', 'B', 'C')) default 'A'
#     time = TimeField()                                           # TIMESTAMP WITH TIME ZONE NOT NULL,
#     employee_id = ForeignKey('Employee', on_delete=CASCADE)      # UUID REFERENCES EMPLOYEE( EMPLOYEE_ID ),
#     sh_id = ForeignKey('ServiceHostel', on_delete=CASCADE)       # UUID REFERENCES SERVICE_HOSTEL( SH_ID ),
#     guest_id = ForeignKey('Guests', on_delete=CASCADE)           # UUID REFERENCES GUESTS( GUEST_ID ),
#     total_price = SmallIntegerField()                            # MONEY
