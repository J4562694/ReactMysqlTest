CREATE DATABASE ReactMysqlTest;

USE ReactMysqlTest;

-- 將帳號密碼加入資料庫
CREATE TABLE users(
    ID BINARY(16) PRIMARY KEY,
    Account VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL
);
INSERT INTO users(ID, Account, Password)
VALUE (UUID(), 'admin', '123456')