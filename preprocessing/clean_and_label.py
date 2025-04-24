# preprocessing/clean_and_label.py

import pandas as pd
import re
import os

def load_ingredient_blacklist(path="cleaned_data/harmful_ingredients_master.txt"):
    if not os.path.exists(path):
        print(f" Warning: ingredient blacklist not found at {path}. Using empty list.")
        return set()
    with open(path, "r", encoding="utf-8") as f:
        return set(line.strip().lower() for line in f if line.strip())

def label_ingredient_safety(ingredient_text, harmful_set):
    """
    Returns 1 if any harmful ingredient is found in the text, else 0.
    """
    ingredients = re.split(r"[,\(\)\[\]\s]+", ingredient_text.lower())
    for ing in ingredients:
        if ing.strip() in harmful_set:
            return 1
    return 0



def label_dataframe(df: pd.DataFrame, harmful_set: set) -> pd.DataFrame:
    """
    Adds a binary 'label' colum to the DataFrame: 1 = harmful, 0 = safe.
    """

    df = df.copy()
    df['label'] = df['ingredients_text'].apply(lambda x: label_ingredient_safety(x, harmful_set))
    return df