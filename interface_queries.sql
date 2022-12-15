
insert into interface_placetype values (1, 'Single', 1000);
insert into interface_placetype values (2, 'Double', 1600);

insert into interface_bookingstatus values (1, 'A', 'Guest in the hostel');
insert into interface_bookingstatus values (2, 'N', 'Guest checked out');

insert into interface_places values (1, 2, True );
insert into interface_places values (2, 1, True);
insert into interface_places values (3, 2, True);
insert into interface_places values (4, 2, True);
insert into interface_places values (5, 1, True);
insert into interface_places values (6, 1, True);
insert into interface_places values (7, 1, True);
insert into interface_places values (8, 2, True);
insert into interface_places values (9, 1, True);
insert into interface_places values (10, 2, True);

SELECT * FROM interface_bookingstatus;
SELECT * FROM interface_bookings;
SELECT * FROM employee;
SELECT * FROM interface_guests;
SELECT * FROM hostels;
SELECT * FROM interface_placetype;
SELECT * FROM positions;
SELECT * FROM interface_places;
SELECT * FROM room;
SELECT * FROM service_hostel;
SELECT * FROM service_rendered;
SELECT * FROM services;

drop table if EXISTS interface_bookings;
drop table if EXISTS interface_bookingstatus;
drop table if EXISTS interface_places;
drop table if EXISTS interface_placetype;
drop table if EXISTS ROOM;
drop table if EXISTS SERVICE_RENDERED;
drop table if EXISTS interface_guests;
drop table if EXISTS EMPLOYEE;
drop table if EXISTS POSITIONS;
drop table if EXISTS SERVICE_HOSTEL;
drop table if EXISTS SERVICES;
drop table if EXISTS HOSTELS;


--Таблица 1. Хостел
CREATE TABLE HOSTELS(
	HOSTEL_ID UUID PRIMARY KEY,
	ADDRESS VARCHAR(100) NOT NULL,
	PHONE VARCHAR(11) NOT NULL,
	AVAILABLE BOOLEAN       	
);


--Таблица 2. Комната
CREATE TABLE ROOM (
	ROOM_ID UUID PRIMARY KEY, 
	GENDER CHAR(1) CHECK(GENDER  in('М', 'Ж', 'Н')) default 'Н',
	CAPACITY SMALLINT,
	AVAILAVILITY BOOLEAN,
	HOSTEL_ID UUID REFERENCES HOSTELS( HOSTEL_ID )
);

--Таблица 3. Тип места
CREATE TABLE interface_placetype(
	PLACE_TYPE_ID  UUID  PRIMARY KEY, 
	TYPE VARCHAR(100),
	PRICE MONEY
);

--Таблица 4. Места
CREATE TABLE interface_places (
	PLACE_ID UUID PRIMARY KEY,
	PLACE_TYPE_ID UUID REFERENCES interface_placetype ( PLACE_TYPE_ID ),
	ROOM_ID UUID REFERENCES ROOM ( ROOM_ID )
);


--Таблица 6. Статус брони
CREATE TABLE interface_bookingstatus (
	BK_ID UUID PRIMARY KEY,
	STATUS CHAR(1) CHECK(STATUS  in('A', 'B', 'C')) default 'A',
	DESCRIPTION VARCHAR(100)
);


--Таблица 8. Должности
CREATE TABLE POSITIONS(
	POSITION_ID UUID  PRIMARY KEY, 
	NAME VARCHAR(50),
	SALARY MONEY
);

--Таблица 7. Сотрудники
CREATE TABLE EMPLOYEE (
	EMPLOYEE_ID UUID PRIMARY KEY,
	PASSPORT VARCHAR(10) NOT NULL,
	SURNAME VARCHAR(20) NOT NULL,
	NAME VARCHAR(20) NOT NULL,
	FATHERNAME VARCHAR(20) NOT NULL,
	GENDER CHAR(1) CHECK(GENDER  in('М', 'Ж', 'Н')) default 'Н',
	ADDRESS VARCHAR(100),
	BIRTHDATE DATE NOT NULL,
	POSITION_ID UUID REFERENCES POSITIONS( POSITION_ID  ),
	PHONE_NUMBER VARCHAR(11),
	HOSTEL_ID UUID REFERENCES HOSTELS( HOSTEL_ID  )
);


--Таблица 9. Гости
CREATE TABLE interface_guests(
	GUEST_ID UUID  PRIMARY KEY, 
	PASSPORT VARCHAR(10),
	SURNAME VARCHAR(20), 
	NAME VARCHAR(20),
	FATHERNAME VARCHAR(20),
	SEX CHAR(1) CHECK(SEX in('М', 'Ж', 'Н')) default 'Н',
	ADDRESS VARCHAR(100),
	BIRTHDATE DATE, 
	PHONE_NUMBER VARCHAR(11),
	EMAIL VARCHAR(30)
);

--Таблица 5. Бронирования
CREATE TABLE interface_bookings (
	PB_ID UUID  PRIMARY KEY, 
	ARRIVAL_DATE TIMESTAMP WITH TIME ZONE,
	CHECKOUT_DATE TIMESTAMP WITH TIME ZONE, 
	MONEY_TOTAL MONEY,
	BK_ID UUID REFERENCES interface_bookingstatus( BK_ID  ),
	GUEST_ID UUID REFERENCES interface_guests( GUEST_ID  ),
	PLACE_ID UUID REFERENCES interface_places( PLACE_ID  )
);

--Таблица 10. Услуги
CREATE TABLE SERVICES(
	SERVICE_ID UUID  PRIMARY KEY, 
	PRICE MONEY,
	DESCRIPTION VARCHAR(100)
);


--Таблица 11. Услуги в хостеле
CREATE TABLE SERVICE_HOSTEL(
	SH_ID UUID  PRIMARY KEY, 
	SERVICE_ID  UUID REFERENCES SERVICES( SERVICE_ID ),
	HOSTEL_ID  UUID REFERENCES HOSTELS( HOSTEL_ID )
);


--Таблица 12. Оказанные услуги
CREATE TABLE SERVICE_RENDERED (
	SR_ID UUID PRIMARY KEY,
	AMOUNT SMALLINT,
	STATUS CHAR(1) CHECK(STATUS in('A', 'B', 'C')) default 'A',
	TIME TIMESTAMP WITH TIME ZONE,
	EMPLOYEE_ID UUID REFERENCES EMPLOYEE( EMPLOYEE_ID ),
	SH_ID  UUID REFERENCES SERVICE_HOSTEL( SH_ID ),
	GUEST_ID UUID REFERENCES interface_guests( GUEST_ID ),
	TOTAL_PRICE MONEY
);

INSERT INTO interface_guests VALUES (round(random()*10000000),'4752992885','Кузнецова','Алиса','Ивановна','Ж','Россия, г. Ангарск, Цветочная ул., д. 12 кв.104', '1998-02-20','79156133385','zahar26071979@gmail.com');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4893947169','Калачева','Таисия','Ильинична','Ж','Россия, г. Орёл, Первомайская ул., д. 14 кв.98', '1975-11-10','79341575150','varvara54@rambler.ru');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4441672082','Виноградов','Платон','Александрович','М','Россия, г. Севастополь, Колхозная ул., д. 6 кв.164', '1986-04-02','79129121615','viktoriya56@outlook.com');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4767437616','Сидорова','Алиса','Николаевна','Ж','Россия, г. Владивосток, Садовая ул., д. 11 кв.13', '2000-09-15','79821050774','konstantin1975@hotmail.com');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4322918289','Александров','Артур','Степанович','М','Россия, г. Бердск, Заслонова ул., д. 16 кв.212', '1976-07-30','79309833490','anjela5159@yandex.ru');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4292705552','Крылов','Дмитрий','Миронович','М','Россия, г. Стерлитамак, Севернаяул., д. 22 кв.108', '1974-02-05','79872306123','german1962@outlook.com');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4183717871','Игнатьева','Арина','Кирилловна','Ж','Россия, г. Дербент, Дружбы ул., д. 9 кв.26', '1973-03-01','79935655379','maryamna15081989@yandex.ru');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4894488064','Козлова','Аиша','Кирилловна','Ж','Россия, г. Салават, Радужная ул., д. 4 кв.194', '1974-12-24','79945072146','lidiya13@ya.ru');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4291704310','Крючков','Марсель','Ибрагимович','М','Россия, г. Новочеркасск, Шоссейная ул., д. 22 кв.198','1980-12-31','79669498015','lyudmila6870@outlook.com');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4486663144','Васильева','Ева','Сергеевна','Ж','Россия, г. Волжский, Советский пер., д. 6 кв.19', '1987-10-04','79342218870','ignat.tarasov@hotmail.com');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4457987182','Абрамов','Демид','Саввич','М','Россия, г. Барнаул, Красноармейская ул., д. 25 кв.27', '1981-07-04','79282786234','anton28071973@mail.ru');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4989158930','Калугин','Кирилл','Вадимович','М','Россия, г. Орёл, Коммунистическая ул., д. 22 кв.156', '1979-01-20','79052720898','oksana21@rambler.ru');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4985239341','Агеев','Иван','Вадимович','М','Россия, г. Раменское, Интернациональная ул., д. 23 кв.116', '1976-09-07','79858044513','olga.yamatina@gmail.com');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4182650931','Кондратова','София','Никитична','Ж','Россия, г. Череповец, Мирная ул., д. 10 кв.23', '1996-02-02','79500093494','alena7552@outlook.com');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4360938606','Маркин','Никита','Тигранович','М','Россия, г. Липецк, Новоселов ул., д. 11 кв.6', '1976-01-25','79542408728','mila58@outlook.com');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4163548665','Тихонов','Николай','Георгиевич','М','Россия, г. Муром, Мира ул., д. 25 кв.20', '1980-08-13','79895877817','afanasiy1978@yandex.ru');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4251934197','Андреев','Артём','Анатольевич','М','Россия, г. Сызрань, Центральная ул., д. 17 кв.87', '1979-05-06','79881844208','ivan4129@hotmail.com');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4626705650','Кузнецова','Виктория','Константиновна','Ж','Россия, г. Каменск - Уральский, Космонавтов ул., д. 17 кв.159', '1979-07-01','79616759774','apollinariya17091962@yandex.ru');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4093544095','Комарова','Амина','Саввична','Ж','Россия, г. Пятигорск, Первомайская ул., д. 14 кв.11', '1978-03-22','79829966140','ekaterina69@outlook.com');
INSERT INTO interface_guests VALUES (round(random()*10000000),'4855971200','Спиридонова','Кристина','Григорьевна','Ж','Россия, г. Вологда, Якуба Коласа ул., д. 8 кв.39', '1970-09-10','79817629910','maryana20081970@outlook.com');

INSERT INTO HOSTELS VALUES(uuid_in(md5(random()::text || random()::text)::cstring), '204903, Кировская область, город Талдом, проезд Косиора, 95', '79845181781', True);
INSERT INTO HOSTELS VALUES(uuid_in(md5(random()::text || random()::text)::cstring), '860715, Ярославская область, город Балашиха, наб. Домодедовская, 97', '79775294130', True);
INSERT INTO HOSTELS VALUES(uuid_in(md5(random()::text || random()::text)::cstring), '323187, Вологодская область, город Видное, пл. Ломоносова, 69', '79250335163', True);
INSERT INTO HOSTELS VALUES(uuid_in(md5(random()::text || random()::text)::cstring), '360289, Кировская область, город Клин, проезд Бухарестская, 52', '79081037619', True);
INSERT INTO HOSTELS VALUES(uuid_in(md5(random()::text || random()::text)::cstring), '901608, Московская область, город Дмитров, проезд Будапештсткая, 65', '79709408454', True);
INSERT INTO HOSTELS VALUES(uuid_in(md5(random()::text || random()::text)::cstring), '106744, Магаданская область, город Павловский Посад, пл. Чехова, 08', '79175059501', True);
INSERT INTO HOSTELS VALUES(uuid_in(md5(random()::text || random()::text)::cstring), '748610, Новосибирская область, город Серебряные Пруды, шоссе Гагарина, 18', '79046352478', True);
INSERT INTO HOSTELS VALUES(uuid_in(md5(random()::text || random()::text)::cstring), '315120, Омская область, город Домодедово, пер. Будапештсткая, 72', '79601457673', True);
INSERT INTO HOSTELS VALUES(uuid_in(md5(random()::text || random()::text)::cstring), '999574, Новгородская область, город Воскресенск, пл. Бухарестская, 31', '79204722866', False);
INSERT INTO HOSTELS VALUES(uuid_in(md5(random()::text || random()::text)::cstring), '858662, Курская область, город Истра, пл. Славы, 09', '79651823300', False);

INSERT INTO interface_placetype VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Восьмиместный', 750.00);
INSERT INTO interface_placetype VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Шестиместный', 800.00);
INSERT INTO interface_placetype VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Четырехместный', 900.00);
INSERT INTO interface_placetype VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Трехместный', 2500.00);
INSERT INTO interface_placetype VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Двухместный', 4400.00);
INSERT INTO interface_placetype VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Одноместный', 4800.00);
INSERT INTO interface_placetype VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Апартаменты', 5300.00);

INSERT INTO interface_bookingstatus VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'A', 'Бронь');
INSERT INTO interface_bookingstatus VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'B', 'Оплачено');
INSERT INTO interface_bookingstatus VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'C', 'Отмена');

INSERT INTO POSITIONS VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Сотрудник хостела', 40000.00);
INSERT INTO POSITIONS VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Администратор', 60000.00);
INSERT INTO POSITIONS VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Аналитик', 80000.00);
INSERT INTO POSITIONS VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Сотрудник отдела кадров', 60000.00);
INSERT INTO POSITIONS VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Администатор БД', 90000.00);
INSERT INTO POSITIONS VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 'Бухгалтер', 80000.00);

INSERT INTO SERVICES VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 100.00, 'Прачечная: Стиральная + сушильная машины');
INSERT INTO SERVICES VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 350.00, 'Завтрак: Заказ у администраторов');
INSERT INTO SERVICES VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 350.00, 'Велосипед: Аренда');
INSERT INTO SERVICES VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 20.00, 'Ксерокопия и печать');
INSERT INTO SERVICES VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 1500.00, 'Транспорт: Аренда');
INSERT INTO SERVICES VALUES (uuid_in(md5(random()::text || random()::text)::cstring), 300.00, 'Товары личной гигиены');

insert into EMPLOYEE values (gen_random_uuid(), round(random()*1000000000)::text, 'Спиридонова', 'Кристина', 'Григорьевна', 'Ж', 'Россия, г. Назрань, Гагарина ул., д. 6 кв.2', '1999-05-26', (select POSITION_ID from POSITIONS order by random() limit 1), '79669498015', (select HOSTEL_ID from HOSTELS order by random() limit 1));
insert into EMPLOYEE values (gen_random_uuid(), round(random()*1000000000)::text, 'Кузнецова', 'Варвара', 'Ивановна', 'Ж','Россия, г. Новочеркасск, Шоссейная ул., д. 22 кв.198', '1989-09-26', (select POSITION_ID from POSITIONS order by random() limit 1), '79342218870', (select HOSTEL_ID from HOSTELS order by random() limit 1));
insert into EMPLOYEE values (gen_random_uuid(), round(random()*1000000000)::text, 'Старостина', 'Ника', 'Алексеевна', 'Ж','Россия, г. Волжский, Советский пер., д. 6 кв.19', '1972-03-19', (select POSITION_ID from POSITIONS order by random() limit 1), '79282786234', (select HOSTEL_ID from HOSTELS order by random() limit 1));
insert into EMPLOYEE values (gen_random_uuid(), round(random()*1000000000)::text, 'Матвеев', 'Даниил', 'Егорович', 'М','Россия, г. Барнаул, Красноармейская ул., д. 25 кв.27', '2000-10-24', (select POSITION_ID from POSITIONS order by random() limit 1), '79052720898', (select HOSTEL_ID from HOSTELS order by random() limit 1));
insert into EMPLOYEE values (gen_random_uuid(), round(random()*1000000000)::text, 'Ковалев', 'Денис', 'Ярославович', 'М','Россия, г. Орёл, Коммунистическая ул., д. 22 кв.156', '1983-05-25', (select POSITION_ID from POSITIONS order by random() limit 1), '79858044513', (select HOSTEL_ID from HOSTELS order by random() limit 1));
insert into EMPLOYEE values (gen_random_uuid(), round(random()*1000000000)::text, 'Лаврова', 'Анна', 'Александровна', 'Ж','Россия, г. Раменское, Интернациональная ул., д. 23 кв.116', '1976-08-23', (select POSITION_ID from POSITIONS order by random() limit 1), '79500093494', (select HOSTEL_ID from HOSTELS order by random() limit 1));
insert into EMPLOYEE values (gen_random_uuid(), round(random()*1000000000)::text, 'Калинин', 'Вадим', 'Демьянович', 'М','Россия, г. Череповец, Мирная ул., д. 10 кв.23', '1991-02-18', (select POSITION_ID from POSITIONS order by random() limit 1), '79542408728', (select HOSTEL_ID from HOSTELS order by random() limit 1));
insert into EMPLOYEE values (gen_random_uuid(), round(random()*1000000000)::text, 'Усова', 'Ясмина', 'Семёновна', 'Ж','Россия, г. Липецк, Новоселов ул., д. 11 кв.6', '1977-09-07', (select POSITION_ID from POSITIONS order by random() limit 1), '79895877817', (select HOSTEL_ID from HOSTELS order by random() limit 1));
insert into EMPLOYEE values (gen_random_uuid(), round(random()*1000000000)::text, 'Семенова', 'Василиса', 'Евгеньевна', 'Ж','Россия, г. Муром, Мира ул., д. 25 кв.20', '1978-11-13', (select POSITION_ID from POSITIONS order by random() limit 1), '79881844208', (select HOSTEL_ID from HOSTELS order by random() limit 1));
insert into EMPLOYEE values (gen_random_uuid(), round(random()*1000000000)::text, 'Гончарова', 'Амина', 'Тимофеевна', 'Ж','Россия, г. Сызрань, Центральная ул., д. 17 кв.87', '1998-03-01', (select POSITION_ID from POSITIONS order by random() limit 1), '79616759774', (select HOSTEL_ID from HOSTELS order by random() limit 1));
insert into EMPLOYEE values (gen_random_uuid(), round(random()*1000000000)::text, 'Павлова', 'Кира', 'Романовна', 'Ж','Россия, г. Каменск - Уральский, Космонавтов ул., д. 17 кв.159', '1973-02-10', (select POSITION_ID from POSITIONS order by random() limit 1), '79829966140', (select HOSTEL_ID from HOSTELS order by random() limit 1));
insert into EMPLOYEE values (gen_random_uuid(), round(random()*1000000000)::text, 'Васильев', 'Али', 'Германович', 'М','Россия, г. Пятигорск, Первомайская ул., д. 14 кв.11', '1970-10-10', (select POSITION_ID from POSITIONS order by random() limit 1), '79817629910', (select HOSTEL_ID from HOSTELS order by random() limit 1));


-- class Bookings(Model):  # Таблица 5. Брони
--     pb_id = BigAutoField(primary_key=True)                       # UUID  PRIMARY KEY,
--     arrival_date = DateField(auto_now=True)                      # TIMESTAMP WITH TIME ZONE NOT NULL,
--     checkout_date = DateField(auto_now=True)                     # TIMESTAMP WITH TIME ZONE,
--     money_total = IntegerField()                            # MONEY,
--     bk_id = ForeignKey('BookingStatus', on_delete=CASCADE)       # UUID    REFERENCES    BOOKING_STATUS(BK_ID),
--     guest_id = ForeignKey('Guests', on_delete=CASCADE)           # UUID    REFERENCES    GUESTS(GUEST_ID),
--     place_id = ForeignKey('Places', on_delete=CASCADE)           # UUID    REFERENCES  

CREATE OR REPLACE FUNCTION add_bookings() 
returns void
AS $$
  DECLARE 
    ar_date date;
    days_in_book integer;
    _place_id integer;
    amount integer;
  BEGIN
    FOR r IN 1..10
    LOOP
      ar_date = current_date - round(random()*1000)::integer;
      days_in_book = round(random()*30)::integer;

      -- WHILE EXISTS (select * from interface_bookings where 
      --   (ar_date >= ARRIVAL_DATE and ar_date < CHECKOUT_DATE) 
      --   or (ar_date + days_in_book::integer >= ARRIVAL_DATE and ar_date + days_in_book::integer < CHECKOUT_DATE))
      -- LOOP
      --   ar_date = current_date - round(random()*1000)::integer;
      --   days_in_book = round(random()*30)::integer;
      -- END LOOP;

      _place_id = (select place_id from interface_places order by random() limit 1);
      amount = days_in_book * 300;
      -- (select price from interface_places as p left join interface_placetype as pt on p.place_type_id_id = pt.place_type_id where p.place_id = _place_id);
      insert into interface_bookings values (round(random()*1000), ar_date, ar_date + days_in_book,
      amount, (select bk_id from interface_bookingstatus order by random() limit 1),
      (select guest_id from interface_guests order by random() limit 1),
      _place_id
      );
    END LOOP;
  END;
$$ LANGUAGE plpgsql;

select add_bookings();



CREATE OR REPLACE FUNCTION add_rooms() 
returns void
AS $$
  DECLARE 
  gen char;
  gens char[];
  hostel uuid;
  BEGIN
    gens = ARRAY['М', 'Н', 'Ж'];
    FOR hostel IN (select HOSTEL_ID from HOSTELS)
    LOOP
      FOR i IN 1..(round(random()*20)::int)
      LOOP
        gen = gens[round(random()*2+1)::int];
        insert into ROOM values (gen_random_uuid(), gen, round(random()*20)::int, (round(random()+0.3)::int)::boolean, hostel);
      END LOOP;
    END LOOP;
  END;
$$ LANGUAGE plpgsql;

select add_rooms();



CREATE OR REPLACE FUNCTION add_places() 
returns void
AS $$
  DECLARE 
    _room uuid;
  BEGIN
    FOR _room IN (select ROOM_ID from ROOM)
    LOOP
      FOR i IN 1..(select CAPACITY from ROOM where ROOM_ID = _room)
      LOOP
        insert into interface_places values 
          (gen_random_uuid(), (select PLACE_TYPE_ID from interface_placetype order by random() limit 1), _room);
      END LOOP;
    END LOOP;
  END;
$$ LANGUAGE plpgsql;

select add_places();



CREATE OR REPLACE FUNCTION add_service_hostel() 
returns void
AS $$
  DECLARE 
  hostel uuid;
  _service uuid;
  BEGIN
    FOR hostel IN (select HOSTEL_ID from HOSTELS)
    LOOP
      FOR _service IN (select SERVICE_ID from SERVICES)
      LOOP
			IF round(random()+0.3)::int THEN
        insert into SERVICE_HOSTEL values (gen_random_uuid(), _service, hostel);
			END IF;
      END LOOP;
    END LOOP;
  END;
$$ LANGUAGE plpgsql;

select add_service_hostel();



CREATE OR REPLACE FUNCTION add_service_rendered() 
returns void
AS $$
  DECLARE 
  hostel uuid;
  stat char;
  stats char[];
  BEGIN
    stats = ARRAY['A', 'B', 'C'];
    FOR hostel IN (select HOSTEL_ID from HOSTELS)
    LOOP
      FOR i IN 1..(round(random()*150)::int)
      LOOP
        stat = stats[round(random()*2+1)::int];
        insert into SERVICE_RENDERED values 
          (gen_random_uuid(), round(random()*10+1)::int, stat,
          current_date - round(random()*1000)::integer,
          (select e.EMPLOYEE_ID from HOSTELS AS h
            join EMPLOYEE as e ON e.HOSTEL_ID = hostel
            where h.HOSTEL_ID = hostel
            order by random() limit 1),
          (select sh.SH_ID from HOSTELS AS h
            join SERVICE_HOSTEL as sh ON sh.HOSTEL_ID = hostel
            where h.HOSTEL_ID = hostel
            order by random() limit 1),
          (select GUEST_ID from interface_guests order by random() limit 1),
          round(random()*5000)::int::money
          );
      END LOOP;
    END LOOP;
  END;
$$ LANGUAGE plpgsql;

select add_service_rendered();



-- Бронирования гостя за этот год
select * from interface_bookings where GUEST_ID = (SELECT GUEST_ID from interface_guests limit 1);
-- Количество бронирований в каждом хостеле
select count(interface_bookings.PB_ID) as interface_bookings, hostels.* from hostels 
  left join room on hostels.HOSTEL_ID = room.HOSTEL_ID
  left join interface_places on interface_places.ROOM_ID = room.ROOM_ID 
  left join interface_bookings on interface_bookings.PLACE_ID = interface_places.PLACE_ID
group by hostels.HOSTEL_ID
order by count(interface_bookings.PB_ID) desc;
-- Количество мест в каждом хостеле
select count(interface_places.PLACE_ID) as interface_places, hostels.* from hostels 
  left join room on hostels.HOSTEL_ID = room.HOSTEL_ID
  left join interface_places on interface_places.ROOM_ID = room.ROOM_ID 
group by hostels.HOSTEL_ID
order by count(interface_places.PLACE_ID) desc;
-- Какие типы комнат есть в хостеле
select p.place_id, pt.type from interface_places p, hostels h, room r, interface_placetype pt where(p.room_id = r.room_id) and (h.hostel_id = r.hostel_id);
-- Активные заказы в хостеле
select b.pb_id from interface_bookings b , interface_bookingstatus bs where (b.bk_id = bs.bk_id) and (bs.status = 'C');
-- Доступные места в хостеле
select p.place_id, pt.type from interface_places p, hostels h, room r, interface_placetype pt where(p.room_id = r.room_id) and (h.hostel_id = r.hostel_id) and (r.availavility = true);
--услуги, которые есть в хостеле
select hostels.address, description from HOSTELS, SERVICES, SERVICE_HOSTEL
  where SERVICE_HOSTEL.hostel_id=HOSTELS.hostel_id and SERVICES.service_id=SERVICES.service_id
order by hostels.address;
--сотрудники женщины в хостеле
select surname, name, fathername, employee.hostel_id, hostels.address from EMPLOYEE, HOSTELS
  where employee.hostel_id=hostels.hostel_id and gender='Ж'
order by hostel_id;
--суммарная зп сотрудников в хостеле
select hostels.address, sum(salary) from employee, positions, hostels
  where employee.position_id=positions.position_id and employee.hostel_id=hostels.hostel_id
group by hostels.address;

SET lc_monetary TO "en_RU.UTF-8";