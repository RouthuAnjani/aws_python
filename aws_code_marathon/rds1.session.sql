CREATE SCHEMA ride_details;

use ride_details;


CREATE TABLE ride_details (
    RideNo int primary key auto_increment,
    DriverName varchar(30),
    CustomerName varchar(30),
    PassengerCount int
);

drop TABLE ride_details;

SELECT * FROM ride_details;
