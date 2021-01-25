create database Tariff_Plan_Management;

use Tariff_Plan_Management;

CREATE TABLE Plan (
    plan_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    plan_name VARCHAR(255) NOT NULL,
    plan_type VARCHAR(255) NOT NULL,
    tariff INTEGER NOT NULL,
    validity INTEGER NOT NULL,
    rental FLOAT
)  auto_increment = 100;

INSERT INTO Plan (plan_name, plan_type, tariff, validity,rental) VALUES ( 'Trial', 'Data',63, 18, 0.5);
INSERT INTO Plan (plan_name, plan_type, tariff, validity,rental) VALUES ( 'Month','Data',98, 28,0.5);
INSERT INTO Plan (plan_name, plan_type, tariff, validity,rental) VALUES ( '2 Month', 'Data',196, 56,0.5);
INSERT INTO Plan (plan_name, plan_type, tariff, validity,rental) VALUES ( '3 Month', 'Data',294, 84,0.5);
INSERT INTO Plan (plan_name, plan_type, tariff, validity,rental) VALUES ( 'Year', 'Data',1278, 365,0.5);
INSERT INTO Plan (plan_name, plan_type, tariff, validity,rental) VALUES ( 'Trial', 'Voice', 40,18,0.4);
INSERT INTO Plan (plan_name, plan_type, tariff, validity,rental) VALUES ( 'Month', 'Voice', 100,28,0.4);
INSERT INTO Plan (plan_name, plan_type, tariff, validity,rental) VALUES ( '2 Month', 'Voice', 200,56,0.4);
INSERT INTO Plan (plan_name, plan_type, tariff, validity,rental) VALUES ( '3 Month', 'Voice', 300,84,0.4);
INSERT INTO Plan (plan_name, plan_type, tariff, validity,rental) VALUES ( 'Year', 'Voice', 1000,365,0.4);

CREATE TABLE ad_login (
    admin_login VARCHAR(255) NOT NULL,
    admin_pass VARCHAR(255) NOT NULL
);

CREATE TABLE cust_login (
    customer_login VARCHAR(255) NOT NULL,
    customer_pass VARCHAR(255) NOT NULL
);

insert into ad_login (admin_login, admin_pass) values ('shivani', 'qwerty123');

insert into cust_login (customer_login, customer_pass) values ('amit', 'asdfg123');
insert into cust_login (customer_login, customer_pass) values ('aniket', 'zxcvb123');
insert into cust_login (customer_login, customer_pass) values ('bhargavi', 'poiuy098');
insert into cust_login (customer_login, customer_pass) values ('bhumika', 'lkjhg098');
insert into cust_login (customer_login, customer_pass) values ('sana', 'mnbvc098');
insert into cust_login (customer_login, customer_pass) values ('osama', '4567');


select * from ad_login;

select * from cust_login;

