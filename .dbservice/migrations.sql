-- create the table
CREATE TABLE IF NOT EXISTS public.test_user
(
    user_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    first_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
 last_name character varying(50) COLLATE pg_catalog."default" NULL,
    CONSTRAINT test_user_pkey PRIMARY KEY (user_id)
);

-- insert test values
INSERT INTO test_user (first_name, last_name) VALUES
('John', 'Doe'),
('Jane', 'Smith'),
('Michael', 'Johnson'),
('Emily', 'Davis'),
('David', 'Brown'),
('Sarah', 'Miller'),
('James', 'Wilson'),
('Jessica', 'Moore'),
('Daniel', 'Taylor'),
('Laura', 'Anderson');