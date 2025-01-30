-- Table: public.shape_cleaned

-- DROP TABLE IF EXISTS public.shape_cleaned;

CREATE TABLE IF NOT EXISTS public.shape_cleaned
(
    shape_id integer,
    shape_pt_lat double precision,
    shape_pt_lon double precision,
    shape_pt_sequence integer,
    id_shape integer
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.shape_cleaned
    OWNER to postgres;