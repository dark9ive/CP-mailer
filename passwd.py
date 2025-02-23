import random
from constant import PASS_DIGIT, PASS_DICT

def rand_pass():
    return ''.join(random.choices(PASS_DICT, k=PASS_DIGIT))
