import os

from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    if os.path.exists(SCORES_FILE_NAME):
        if os.stat(SCORES_FILE_NAME).st_size == 0:
            file = open(SCORES_FILE_NAME, 'a+')
            file.write(str(POINTS_OF_WINNING))
        else:
            file = open(SCORES_FILE_NAME,'r')
            last_score = int(file.read())
            score = last_score + POINTS_OF_WINNING
            file = open(SCORES_FILE_NAME, 'w')
            file.write(str(score))
            file.close()

    else:
        file = open(SCORES_FILE_NAME,'w')
        file.write(str(POINTS_OF_WINNING))
        file.close()


add_score(1)