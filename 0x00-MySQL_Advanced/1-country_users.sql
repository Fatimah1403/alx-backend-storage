-- script that creates a table users
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN,\
-- never null (= default will be the first element of the enumeration, here US)

CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) not null unique,
    name VARCHAR(255),
    PRIMARY KEY (id);
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL 
    
);
