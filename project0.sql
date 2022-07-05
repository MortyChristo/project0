DROP TABLE IF EXISTS account;
DROP TABLE IF EXISTS customer;

CREATE TABLE customer (
	customer_name VARCHAR(40) UNIQUE NOT NULL,
	customer_id INTEGER UNIQUE NOT NULL PRIMARY KEY
);


CREATE TABLE account (
	customer_id INTEGER NOT NULL,
	account_num INTEGER UNIQUE NOT NULL,
	balance INTEGER NOT NULL,
	CONSTRAINT fk_users FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
	);

SELECT * FROM account WHERE customer_id = 5 AND balance > 1000 AND balance < 0

SELECT * FROM account 

INSERT INTO customer (customer_name, customer_id)
VALUES 
('Chris', 850)

INSERT INTO account (customer_id, account_num, balance)
VALUES 
(850, 123, 1000)