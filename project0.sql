DROP TABLE IF EXISTS account;
DROP TABLE IF EXISTS customer;

CREATE TABLE customer (
	customer_name VARCHAR(40) NOT NULL,
	customer_id INTEGER UNIQUE NOT NULL PRIMARY KEY
);


CREATE TABLE account (
	customer_id INTEGER NOT NULL,
	account_num INTEGER UNIQUE NOT NULL,
	balance INTEGER NOT NULL,
	CONSTRAINT fk_users FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
	);


INSERT INTO customer (customer_name, customer_id)
VALUES 
('Chris Sullivan', 850),
('John Doe', 1),
('Jane Doe', 5);

INSERT INTO account (customer_id, account_num, balance)
VALUES 
(1, 101, 5500),
(1, 102, 2000),
(1, 103, 4000),
(1, 104, 500),
(850, 85001, 5500),
(5, 501, 2000),
(5, 502, 5000000);

SELECT * FROM customer 

SELECT * FROM account 

SELECT * FROM account WHERE customer_id = 1

SELECT * FROM account WHERE customer_id = 1 AND balance > 1000 AND balance < 1000000

