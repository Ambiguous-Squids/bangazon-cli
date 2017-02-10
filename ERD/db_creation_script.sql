CREATE TABLE Customers
(
	idCustomer		INTEGER			NOT NULL,
	first_name		VARCHAR(45)		NOT NULL,
	last_name		VARCHAR(45)		NOT NULL,
	address_1		VARCHAR(45)		NOT NULL,
	address_2		VARCHAR(45)			NULL,
	city			VARCHAR(45)		NOT NULL,
	state			VARCHAR(45)		NOT NULL,
	zip				VARCHAR(45)		NOT NULL,
	phone_number	VARCHAR(45)			NULL,
	email			VARCHAR(45)		NOT NULL,
	CONSTRAINT email_unique UNIQUE (email)	,
	PRIMARY KEY (idCustomer)
);

CREATE TABLE Payments
(
	idPayment		INTEGER			NOT NULL,
	first_name		VARCHAR(45)		NOT NULL,
	last_name		VARCHAR(45)		NOT NULL,
	acct_number		VARCHAR(45)		NOT NULL,
	exp_date		DATETIME		NOT NULL,
	ccv				INTEGER			NOT NULL,
	category		VARCHAR(45)		NOT NULL,
	idCustomer		INTEGER			NOT NULL,
	PRIMARY KEY (idPayment)					,
	FOREIGN KEY (idCustomer) REFERENCES Customers (idCustomer)
);

CREATE TABLE Orders
(
	idOrder			INTEGER			NOT NULL,
	active			BOOLEAN			NULL,
	idCustomer 		INTEGER			NOT NULL,
	PRIMARY KEY (idOrder)					,
	FOREIGN KEY (idCustomer) REFERENCES Customers (idCustomer)
);

CREATE TABLE Products
(
	idProduct		INTEGER			NOT NULL,
	name 			VARCHAR(45)		NOT NULL,
	price			DECIMAL(8, 2)	NOT NULL,
	quantity		INTEGER			NOT NULL,
	PRIMARY KEY (idProduct)
);

CREATE TABLE OrderItems
(
	idOrderItem		INTEGER			NOT NULL,
	idOrder			INTEGER			NOT NULL,
	idProduct		INTEGER			NOT NULL,
	PRIMARY KEY (idOrderItem)				,
	FOREIGN KEY (idOrder) REFERENCES Orders (idOrder),
	FOREIGN KEY (idProduct) REFERENCES Products (idProduct)
);

