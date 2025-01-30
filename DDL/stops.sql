-- Table: public.stops

-- DROP TABLE IF EXISTS public.stops;

CREATE TABLE IF NOT EXISTS public.stops
(
    stop_id character varying(255) COLLATE pg_catalog."default" NOT NULL,
    stop_code character varying(255) COLLATE pg_catalog."default",
    stop_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    stop_lat numeric(10,8) NOT NULL,
    stop_lon numeric(10,8) NOT NULL,
    location_type integer,
    parent_station character varying(255) COLLATE pg_catalog."default",
    wheelchair_boarding integer,
    paradas_id integer NOT NULL,
    alcaldia character varying(255) COLLATE pg_catalog."default",
    ruta_id integer,
    CONSTRAINT stops_pkey PRIMARY KEY (stop_id),
    CONSTRAINT fk_stops_rutas FOREIGN KEY (ruta_id)
        REFERENCES public.rutas (ruta_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.stops
    OWNER to postgres;