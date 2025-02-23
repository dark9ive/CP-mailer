import pandas as pd
from constant import CSV_FN, EXIST_FN
import re

df = None
exist_dict = None

def parse_name(full_name):
    """
    Parser of name field.
    You may have to edit this function for different cases.
    """
    
    full_name = full_name.strip().replace("\xa0", "")
    
    # Regex pattern: Match the Chinese part (Unicode range) and the English part
    match = re.match(r"([\u4e00-\u9fff]+)([A-Z ,\-]+)", full_name)
    
    if match:
        chinese_name = match.group(1).strip()
        english_name = match.group(2).strip()
        return chinese_name
    else:
        return full_name

def parse_id(ID):
    """
    Parser of id field.
    You may have to edit this function for different cases.
    """

    ID = ID.strip().replace("\xa0", "")
    return ID

def check_exist(username):
    global exist_dict
    if exist_dict is None:
        with open(EXIST_FN, 'r', encoding='utf-8') as file:
            exist_dict = {line.strip() for line in file}
    return username in exist_dict

def get_data(*args):
    global df

    if df is None:
        df = pd.read_csv(CSV_FN)

    return [{arg: getattr(row, arg, None) for arg in args} for row in df.itertuples(index=False)]
