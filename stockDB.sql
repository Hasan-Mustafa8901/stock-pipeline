-- DROP DATABASE stockdb;

CREATE DATABASE stockDB;

USE stockDB;

CREATE TABLE stocksdata(
	date DATE,
    open DOUBLE,
    high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume BIGINT,
    ticker VARCHAR(15),
    prev_close DOUBLE,
    daily_return DOUBLE,
    MA_7 DOUBLE,
    MA_20 DOUBLE
);

SELECT * FROM stocksdata LIMIT 5;

