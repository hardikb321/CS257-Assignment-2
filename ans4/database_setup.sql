CREATE DATABASE user_login_registration;

USE user_login_registration;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL UNIQUE,
    mobile_number VARCHAR(15) NOT NULL,
    password VARCHAR(255) NOT NULL
);
