-- 내부접근자(localhost) : 외부에서 접근 안됨
-- IDENTIFIED BY : 패스워드 설정 
CREATE user 'team3'@localhost IDENTIFIED BY 'dbdb';
-- 데이터베이스 지정하기
USE mysql;


/*
<2. Database 생성>
*/
CREATE DATABASE team3db;

-- DB 정보 조회하기 : root계정 선택 -> 새로고침 

/*
<3. 사용자에게 DB 접근 권한 부여하기>
	- grant : 권한 생성
	- all : 모든 권한(접속, 생성, 조회, 수정, 삭제,입력)
*/
-- 내부사용자
GRANT ALL PRIVILEGES ON team3db.* TO 'team3'@'localhost';
FLUSH PRIVILteam3dbEGES;
