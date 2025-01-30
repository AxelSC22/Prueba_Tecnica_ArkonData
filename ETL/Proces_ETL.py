import sys
import os



from routes import process_data as process_routes_data
from shape import process_data as process_shape_data
from stop_times import process_data as process_stop_times_data
from Proces_calendar import process_data as process_calendar_data
from stop import process_data as process_stop_data

def main():
    # Llamar a las funciones 
    process_routes_data
    process_shape_data
    process_stop_times_data
    process_calendar_data
    process_stop_data

if __name__ == "__main__":
    main()
