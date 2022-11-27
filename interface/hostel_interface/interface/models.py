# from django.db import models
from django.db.models import IntegerField, ForeignKey, UUIDField, CharField, BooleanField, SmallIntegerField, \
    DateTimeField, Model, CASCADE
# Create your models here.
# class
# class BookingStatus(Model):

# class Booking(Model):
#     pb_id = UUIDField()
#     arrival_date = DateTimeField()       #     TIMESTAMP    WITH    TIME    ZONE    NOT    NULL,
#     checkout_date = DateTimeField()      # CHECKOUT_DATE    TIMESTAMP    WITH    TIME    ZONE,
#     money_total = IntegerField()         #    MONEY,
#     bk_id = ForeignKey('BookingStatus')                 #     UUID    REFERENCES    BOOKING_STATUS(BK_ID),
#     guest_id = ForeignKey('Guests')              #     UUID    REFERENCES    GUESTS(GUEST_ID),
#     place_id = ForeignKey('Places')              #     UUID    REFERENCES    PLACES(PLACE_ID)


#Таблица 1. Хостелы
class Hostels(Model):
    hostel_id = UUIDField()
    address = CharField(max_length=100)
    phone = CharField(max_length=11)
    AVAILABLE = BooleanField()


#Таблица 2. Комната
class Room(Model):
    room_id = UUIDField()             # UUID PRIMARY KEY,
    gender = CharField(max_length=1)             # CHAR(1) CHECK(GENDER  in('М', 'Ж', 'Н')) default 'Н',
    capacity = SmallIntegerField()    #  SMALLINT NOT NULL,
    availability = BooleanField()     # BOOLEAN NOT NULL,
    hostel_id = ForeignKey('Hostels', on_delete=CASCADE)          #  UUID REFERENCES HOSTELS( HOSTEL_ID )


#Таблица 3. Тип места
class PlaceType(Model):
    place_type_id = UUIDField()  #   UUID  PRIMARY KEY,
    type = CharField(max_length=100)        # VARCHAR(100) NOT NULL,
    PRICE = SmallIntegerField()


#Таблица 4. Места
class Places(Model):
    place_id = UUIDField()       #  UUID PRIMARY KEY,
    place_type_id = ForeignKey('PlaceType', on_delete=CASCADE) #  UUID REFERENCES PLACE_TYPE ( PLACE_TYPE_ID ),
    room_id = ForeignKey('Room', on_delete=CASCADE)       #  UUID REFERENCES ROOM ( ROOM_ID )


#Таблица 6. Статус брони
class BookingStatus(Model):
    bk_id = UUIDField(  )          #  UUID PRIMARY KEY,
    status = CharField(max_length=1)        #  CHAR(1) CHECK(STATUS  in('A', 'B', 'C')) default 'A',
    description = CharField(max_length=100) # VARCHAR(100)


#Таблица 8. Должности
class Positions(Model):
    position_id = UUIDField()    # UUID  PRIMARY KEY,
    name = CharField(max_length=50)         # VARCHAR(50) NOT NULL,
    salary = SmallIntegerField() # MONEY


#Таблица 7. Сотрудники
class Employee(Model):
    employee_id = UUIDField()    #  UUID PRIMARY KEY,
    passport = CharField(max_length=10)     #  VARCHAR(10) NOT NULL,
    surname = CharField(max_length=20)      # VARCHAR(20) NOT NULL,
    name = CharField(max_length=20)         #  VARCHAR(20) NOT NULL,
    fathername = CharField(max_length=20)   #  VARCHAR(20) NOT NULL,
    gender = CharField(max_length=1)        # CHAR(1) CHECK(GENDER  in('М', 'Ж', 'Н')) default 'Н',
    address = CharField(max_length=100)     # VARCHAR(100) NOT NULL,
    birthdate = DateTimeField()  # DATE NOT NULL,
    position_id = ForeignKey('Positions', on_delete=CASCADE)   #  UUID REFERENCES POSITIONS( POSITION_ID  ),
    phone_number = CharField(max_length=11) #  VARCHAR(11),
    hostel_id = ForeignKey('Hostels', on_delete=CASCADE)     #  UUID REFERENCES HOSTELS( HOSTEL_ID  )


#Таблица 9. Гости
class Guests(Model):
    guest_id = UUIDField()  #  UUID  PRIMARY KEY,
    passport = CharField(max_length=10)
    surname = CharField(max_length=20)
    name = CharField(max_length=20)
    fathername = CharField(max_length=20)
    gender = CharField(max_length=1) #  CHAR(1) CHECK(SEX in('М', 'Ж', 'Н')) default 'Н',
    address = CharField(max_length=100) #  VARCHAR(100) NOT NULL,
    birthdate = DateTimeField()
    phone_number = CharField(max_length=11)
    email = CharField(max_length=30) # VARCHAR(30)


#Таблица 5. Брони
class Bookings(Model):
    pb_id = UUIDField()               # UUID  PRIMARY KEY,
    arrival_date = DateTimeField()    # TIMESTAMP WITH TIME ZONE NOT NULL,
    checkout_date = DateTimeField()   # TIMESTAMP WITH TIME ZONE,
    money_total = SmallIntegerField()                # MONEY,
    bk_id = ForeignKey('BookingStatus', on_delete=CASCADE)     #     UUID    REFERENCES    BOOKING_STATUS(BK_ID),
    guest_id = ForeignKey('Guests', on_delete=CASCADE)              #     UUID    REFERENCES    GUESTS(GUEST_ID),
    place_id = ForeignKey('Places', on_delete=CASCADE)              #     UUID    REFERENCES    PLACES(PLACE_ID)


#Таблица 10. Услуги
class Services(Model):
    service_id = UUIDField() # UUID  PRIMARY KEY,
    price = SmallIntegerField() # MONEY,
    description = CharField(max_length=100) # VARCHAR(100)



#Таблица 11. Услуги в хостеле
class ServiceHostel(Model):
    sh_id = UUIDField()       #  UUID  PRIMARY KEY,
    service_id = ForeignKey('Services', on_delete=CASCADE) #   UUID REFERENCES SERVICES( SERVICE_ID ),
    HOSTEL_ID  = ForeignKey('Hostels', on_delete=CASCADE) # UUID REFERENCES HOSTELS( HOSTEL_ID )


#Таблица 12. Оказанные услуги
class ServiceRendered(Model):
    sr_id = UUIDField()             #  UUID PRIMARY KEY
    amount = SmallIntegerField()    #  SMALLINT,
    status = CharField(max_length=1)           #  CHAR(1) CHECK(STATUS in('A', 'B', 'C')) default 'A',
    time = DateTimeField()          #  TIMESTAMP WITH TIME ZONE NOT NULL,
    employee_id = ForeignKey('Employee', on_delete=CASCADE)      #  UUID REFERENCES EMPLOYEE( EMPLOYEE_ID ),
    sh_id = ForeignKey('ServiceHostel', on_delete=CASCADE)            #  UUID REFERENCES SERVICE_HOSTEL( SH_ID ),
    guest_id = ForeignKey('Guests', on_delete=CASCADE)         # UUID REFERENCES GUESTS( GUEST_ID ),
    total_price = SmallIntegerField()      # MONEY
