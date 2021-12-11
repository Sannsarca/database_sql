-- Creating Country table --

CREATE TABLE country
(
	country_id		char(10)	NOT NULL UNIQUE, 
	country_name	VARCHAR(100)	NOT NULL, 
	country_region	VARCHAR(100)	NOT NULL  
);

-- Create Years table --

CREATE TABLE years
(
	year_id 	char(10) NOT NULL UNIQUE,
	country_id	char(10) NOT NULL ,
	year_data	INT		 NOT NULL
);

-- Create Information table --

CREATE TABLE information
(
	year_country_id	char(10)  NOT NULL,
	points 	decimal NOT NULL,
	place	INT NOT NULL
);

-- Define primary keys --

ALTER TABLE country ADD CONSTRAINT PK_country PRIMARY KEY (country_id);
ALTER TABLE years ADD CONSTRAINT PK_year PRIMARY KEY (year_id);
ALTER TABLE information ADD CONSTRAINT PK_info PRIMARY KEY (year_country_id);

-- Define foreign keys --

ALTER TABLE years ADD CONSTRAINT FK_country_year FOREIGN KEY (country_id) REFERENCES country (country_id);
ALTER TABLE information ADD CONSTRAINT FK_year_info FOREIGN KEY (year_country_id) REFERENCES years (year_id);