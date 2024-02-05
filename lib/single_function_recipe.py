
from datetime import timedelta

def reading_time(book):
    book = book.split()
    mins = len(book) / 200
    time_delta = timedelta(minutes = mins)
    hours = time_delta.seconds // 3600     # only concerned with the whole hour so that's why we are floor dividing
    minutes = (time_delta.seconds % 3600) // 60 # only concerned with the remainder and then floor div that by 60 to get the number of whole minutes
    time_spent_reading = f'The time it would take to read this is {hours}:{minutes:02d}'
    return(time_spent_reading)


