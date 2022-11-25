-- Бронирования гостя за этот год
select * from bookings where GUEST_ID = (SELECT GUEST_ID from guests limit 1);
-- Количество бронирований в каждом хостеле
select count(bookings.PB_ID) as bookings, hostels.* from hostels 
  left join room on hostels.HOSTEL_ID = room.HOSTEL_ID
  left join places on places.ROOM_ID = room.ROOM_ID 
  left join bookings on bookings.PLACE_ID = places.PLACE_ID
group by hostels.HOSTEL_ID
order by count(bookings.PB_ID) desc;
-- Количество мест в каждом хостеле
select count(places.PLACE_ID) as places, hostels.* from hostels 
  left join room on hostels.HOSTEL_ID = room.HOSTEL_ID
  left join places on places.ROOM_ID = room.ROOM_ID 
group by hostels.HOSTEL_ID
order by count(places.PLACE_ID) desc;
-- Какие типы комнат есть в хостеле
select p.place_id, pt.type from places p, hostels h, room r, place_type pt where(p.room_id = r.room_id) and (h.hostel_id = r.hostel_id);
-- Активные заказы в хостеле
select b.pb_id from bookings b , booking_status bs where (b.bk_id = bs.bk_id) and (bs.status = 'C');
-- Доступные места в хостеле
select p.place_id, pt.type from places p, hostels h, room r, place_type pt where(p.room_id = r.room_id) and (h.hostel_id = r.hostel_id) and (r.availavility = true);
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