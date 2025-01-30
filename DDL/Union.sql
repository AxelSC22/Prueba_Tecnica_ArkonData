ALTER TABLE stop_times 
ADD CONSTRAINT fk_stop_times_calendar FOREIGN KEY (stop_times_id) 
REFERENCES calendar_cleaned (fecha_id);

ALTER TABLE shape_cleaned 
ADD CONSTRAINT fk_shape_rutas FOREIGN KEY (id_shape) 
REFERENCES rutas (ruta_id);

ALTER TABLE stop_times 
ADD CONSTRAINT fk_stop_times_stops FOREIGN KEY (stop_id) 
REFERENCES stops (paradas_id);

ALTER TABLE stop_times 
ADD CONSTRAINT fk_stop_times_shape FOREIGN KEY (stop_times_id) 
REFERENCES shape_cleaned (id_shape);
