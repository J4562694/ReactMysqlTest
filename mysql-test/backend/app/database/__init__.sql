CREATE DATABASE ReactMysqlTest;

USE ReactMysqlTest;

-- 將帳號密碼加入資料庫
CREATE TABLE users(
    ID VARCHAR(255) NOT NULL,
    Account VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    PRIMARY KEY(ID)
);
INSERT INTO users(ID, Account, Password)
VALUE ("idNumber", "account", "password")

-- SELECT ID, Account, Password from users;