-- CREATE DATABASE team3db;
USE team3db;

CREATE TABLE member (
  mem_id VARCHAR(255) PRIMARY KEY NOT NULL,
  mem_pass INTEGER NOT NULL
);

INSERT INTO member VALUES ('boyun', '0802');
INSERT INTO member VALUES ('donguk', '1112');
INSERT INTO member VALUES ('jaehyun', '0218');
INSERT INTO member VALUES ('jaekyung', '1017');
INSERT INTO member VALUES ('seoyun', '0912');