import os
import time
SCORES_FILE_NAME="Scores.txt"
BAD_RETURN_CODE=-1
def Screen_cleaner(time_delay):
    time.sleep(time_delay)
    os.system('clear')
