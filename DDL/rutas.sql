-- Table: public.rutas

-- DROP TABLE IF EXISTS public.rutas;

CREATE TABLE IF NOT EXISTS public.rutas
(
    route_id integer NOT NULL,
    agency_id integer,
    route_short_name text COLLATE pg_catalog."default",
    route_long_name text COLLATE pg_catalog."default",
    route_type integer,
    route_color text COLLATE pg_catalog."default",
    route_text_color text COLLATE pg_catalog."default",
    route_sort_order integer,
    continuous_pickup boolean,
    continuous_drop_off boolean,
    ruta_id integer NOT NULL,
    CONSTRAINT rutas_pkey PRIMARY KEY (ruta_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.rutas
    OWNER to postgres;