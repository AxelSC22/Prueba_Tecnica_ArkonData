-- Table: public.calendar_cleaned

-- DROP TABLE IF EXISTS public.calendar_cleaned;

CREATE TABLE IF NOT EXISTS public.calendar_cleaned
(
    service_id character varying(50) COLLATE pg_catalog."default",
    monday integer,
    tuesday integer,
    wednesday integer,
    thursday integer,
    friday integer,
    saturday integer,
    sunday integer,
    start_date date,
    end_date date,
    fecha_id integer NOT NULL,
    CONSTRAINT calendar_cleaned_pkey PRIMARY KEY (fecha_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.calendar_cleaned
    OWNER to postgres;