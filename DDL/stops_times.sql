-- Table: public.stop_times

-- DROP TABLE IF EXISTS public.stop_times;

CREATE TABLE IF NOT EXISTS public.stop_times
(
    trip_id character varying(50) COLLATE pg_catalog."default",
    arrival_time time without time zone,
    departure_time time without time zone,
    stop_id character varying(50) COLLATE pg_catalog."default",
    stop_sequence integer,
    stop_times_id integer,
    CONSTRAINT fk_stop_times_calendar FOREIGN KEY (stop_times_id)
        REFERENCES public.calendar_cleaned (fecha_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_stop_times_stops FOREIGN KEY (stop_id)
        REFERENCES public.stops (stop_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.stop_times
    OWNER to postgres;