
CREATE SCHEMA bills;
use bills
CREATE TABLE utilitybills (
    id int primary key auto_increment,
    monthName varchar(10),
    UnitsUsed int,
    PayableAmount int
);

INSERT into utilitybills (monthName, UnitsUsed, PayableAmount)
VALUES ('Jan',120,870);
INSERT into utilitybills (monthName, UnitsUsed, PayableAmount)
VALUES ('Feb',87,730);
INSERT into utilitybills (monthName, UnitsUsed, PayableAmount)
VALUES ('Mar',92,810);



create SCHEMA macrobuy;

SELECT * FROM utilitybills;

