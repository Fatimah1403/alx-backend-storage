-- script that creates a table users
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN,\
-- never null (= default will be the first element of the enumeration, here US)

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    email varchar(255) not null unique,
    name varchar(255),
    primary key (id);
    country enum('US', 'CO', 'TN') DEFAULT 'US' NOT NULL 
    
);
