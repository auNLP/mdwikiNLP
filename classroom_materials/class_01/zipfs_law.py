"""
A short python script on Zipf's Law

Pick any book from (I will use Harry Potter):
http://www.glozman.com/textpages.html
"""
import requests
import string
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt


def download_txt(url, name=None, write=True):
    if write and name is None:
        raise ValueError("Name is None")
    r = requests.get(url)

    # write content to a .txt file
    with open(name, 'w') as f:
        f.write(r.content.decode("windows-1252")

def tokenize(txt, remove=string.punctuation, lowercase=True):
    for ch in ["\n", "\t", "\r"]:
        if ch in txt:
            txt = txt.replace(ch, "")
    translation_table = str.maketrans('', '', remove)
    txt = txt.translate(translation_table)
    if lowercase:
        txt = txt.lower()
    return txt.split()


def counter_to_df(counter):
    df = pd.DataFrame.from_dict(counter, orient='index')
    df = df.reset_index()
    df = df.rename(columns={"index": "tokens", 0: "count"})
    return df


if __name__ == "__main__":
    url = """http://www.glozman.com/TextPages/Harry%20Potter%201%20-%20Sorcerer's%20Stone.txt"""
    book_name = "harry_potter_sorcerers_stone.txt"

    download_txt(url, name=book_name)
    with open(book_name, "r") as f:
        txt = f.read()

    tokens = tokenize(txt)
    counts = Counter(tokens)

    df = counter_to_df(counts)
    df = df.sort_values(by=['count'], ascending=False)
    df = df.reset_index(drop=True)

    # is the first one "the"
    df["tokens"][0] == "the"

    # proportion of "the"
    df["count"][0]/sum(df["count"])

    # given the freq of the what should the freq of all other words be?
    df['pred'] = [round(df["count"][0]/(i+1), 0)
                  for i in range(len(df["tokens"]))]
    df['diff'] = df['pred'] - df['count']

    # does the Zipf's law apply to Harry Potter?
    fig, ax = plt.subplots()
    n = 300
    x = range(len(df["count"][:n]))
    ax.plot(x, df["count"][:n], label="Actual")
    ax.plot(x, df["pred"][:n], ls='--', label="Predicted")
    ax.set(xlabel='Token rank', ylabel='Frequency',
           title="Zipf's Law in Harry Potter (top 300)")
    ax.grid()
    plt.legend()
    plt.show()

    # with log scale?
    fig, ax = plt.subplots()
    x = range(len(df["count"]))
    ax.plot(x, df["count"], label="Actual")
    ax.plot(x, df["pred"], ls='--', label="Predicted")
    ax.set(xlabel='log(Token rank)', ylabel='log(Frequency)',
           title="Zipf's Law in Harry Potter (all)")
    ax.grid()
    plt.legend()
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.show()
