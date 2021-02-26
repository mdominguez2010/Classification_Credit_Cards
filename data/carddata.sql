CREATE DATABASE credit_default;

\connect credit_default;

CREATE TABLE customers(
  ID INT,
  LIMIT_BAL INT,
  SEX TEXT,
  EDUCATION TEXT,
  MARRIAGE TEXT,
  AGE INT,
  PAY_0 INT,
  PAY_2 INT,
  PAY_3 INT,
  PAY_4 INT,
  PAY_5 INT,
  PAY_6 INT,
  BILL_AMT1 INT,
  BILL_AMT2 INT,
  BILL_AMT3 INT,
  BILL_AMT4 INT,
  BILL_AMT5 INT,
  BILL_AMT6 INT,
  PAY_AMT1 INT,
  PAY_AMT2 INT,
  PAY_AMT3 INT,
  PAY_AMT4 INT,
  PAY_AMT5 INT,
  PAY_AMT6 INT,
  default_payment_next_month INT
);

\copy customers FROM 'card_data.csv' DELIMITER ',' CSV HEADER;


