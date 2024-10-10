create database HOTEL;
USE HOTEL;
-- SHOW TABLES;

CREATE TABLE ROOMS (
  ID int(8) PRIMARY KEY auto_increment,
  ROOM_NO int(4) UNIQUE NOT NULL,
  ROOM_TYPE char(20),
  ROOM_RENT float(10,2),
  ROOM_BED char(20),
  STATUS char(20)
);

-- desc rooms;
insert into rooms values
(1, 1, 'AC', 2500.00, 'Single Bed', 'occupied'),
(2, 2, 'AC', 2500.00, 'Single Bed', 'free'),
(3, 3, 'AC', 2500.00, 'Single Bed', 'free'),
(4, 4, 'AC', 2500.00, 'Single Bed', 'free'),
(5, 5, 'AC', 3500.00, 'Double Bed', 'free'),
(6, 6, 'AC', 3500.00, 'Double Bed', 'free'),
(7, 7, 'AC', 3500.00, 'Double Bed', 'free'),
(8, 8, 'Delux', 4500.00, 'Double Bed', 'free'),
(9, 9, 'Delux', 4500.00, 'Double Bed', 'free'),
(10, 10, 'Delux', 4500.00, 'Double Bed', 'free'),
(11, 11, 'Super Delux', 5500.00, 'Double Bed', 'free'),
(12, 12, 'Super Delux', 5500.00, 'Double Bed', 'free'),
(13, 13, 'Queen Delight', 6500.00, 'Double Bed', 'free'),
(14, 14, 'Queen Delight', 6500.00, 'Double Bed', 'free'),
(15, 15, 'King Special', 7500.00, 'Double Bed', 'free'),
(16, 16, 'King Special', 7500.00, 'Double Bed', 'free'), 
(17, 17, 'Super Rich Special', 9500.00, 'Double Bed', 'free'),
(18, 18, 'Super Rich Special', 8500.00, 'Single Bed', 'free'),
(19, 19, 'Delux', 4000.00, 'Single Bed', 'free'),
(20, 20, 'Super Delux', 4500.00, 'Single Bed', 'free'),
(21, 21, 'Super Delux', 4500.00, 'Single Bed', 'free'),
(22, 22, 'AC', 2650.00, 'SINGLE', 'free'),
(23, 23, 'Non-AC', NULL, NULL, NULL),
(24, 24, 'Non-AC', NULL, NULL, NULL),
(25, 25, 'AC', 3500.00, 'SINGLE', 'free');

create table CUSTOMER (
  ID integer(20) primary key auto_increment,
  NAME char(50) not null,
  ADDRESS char(50) not null,
  PHONE integer(10) unique not null,
  EMAIL_ID char(40),
  ID_PROOF char(25) not null,
  ID_PROOF_NO char(25) unique not null,
  MALES int(2) not null,
  FEMALES int(2) not null,
  CHILDREN int(2) not null
);

alter table customer modify phone bigint(10) not null unique;
-- desc customer;

create table BOOKING (
  BOOK_ID integer(20) PRIMARY KEY auto_increment,
  ROOM_ID integer(20),
  CUST_ID integer(20),
  DOO date,
  DOL date,
  ADVANCE float(10,2)
);

alter table booking add constraint foreign key(ROOM_ID) references rooms(id);
alter table booking add constraint foreign key(CUST_ID) references customer(id);
-- desc booking;

create table BILL (
  BILL_ID INTEGER(20) primary key auto_increment,
  BOOK_ID integer(20),
  AMOUNT float(10,2),
  BILL_DATE date,
  GST int(10),
  ST int(10)
);

alter table bill add Foreign key(BOOK_ID) References booking (BOOk_ID);
-- desc bill;

create table SETTING (
  ID int(10) primary key auto_increment,
  FIELD_NAME char(30),
  VALUE char(100)
);

-- desc setting;

insert into setting values
(1, 'hotel_name', "GREAT GRAND HOTEL"),
(2, 'address', 'SurajMal Vihar, Delhi -92'),
(3, 'phone', '011-4353534,9356584621,7878858585'),
(4, 'email', 'greatgrandhoteldelhi@gmail.com');

-- select * from setting;

create table TAX (
  TAX char(30) not null,
  VALUE float not null
);

-- desc TAX;

insert into tax values ("GST",18),("ST",8);
