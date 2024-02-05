from lib.single_function_recipe import *






# def reading_time(book):
#     book = book.split()
#     len(book) / 200 = number of minutes
#     number_of_minutes/ 60 = hours
#     decimal * 60 = minutes
#     return hours: minutes



def test_single_function_recipe():
    result = reading_time("A In the bustling heart of Tokyo, neon lights painted the night sky in a kaleidoscope of colors. Amidst the towering skyscrapers and the ceaseless hum of urban life, nestled a quaint, ivy-covered teahouse. The air inside was steeped in the gentle aroma of green tea and the soothing hum of soft koto music. Inside, patrons sat on tatami mats, sipping their tea in quiet contemplation. Some were salarymen seeking respite from the day's pressure, others were lost in conversation with friends, and still others were immersed in the pages of well-worn books. Each cup of tea held a silent story, a moment of peace snatched from the city's relentless rhythm. Outside, the rain began to fall, a gentle patter against the paper windows. The sound seemed to draw the patrons closer, creating a sense of shared intimacy. As the hours melted away, the teahouse became a haven, a refuge from the outside world, where time seemed to slow down and worries dissolved in the steam of a warm cup. And as they stepped back into the neon-drenched night, each person carried a piece of that serenity, a reminder of the simple beauty found in the midst of urban chaos.")
    assert result == 'The time it would take to read this is 0:01'
