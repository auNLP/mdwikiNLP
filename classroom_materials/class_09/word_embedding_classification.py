"""
Training Word Embeddings
"""

import tensorflow as tf

import pandas as pd
import numpy as np
from gensim.models import KeyedVectors


def get_conll():
    with open("eng.train.txt") as f:
        raw = f.read()

    def filter_empty_string(t):
        return list(filter(lambda x: x, t))

    docs = raw.split("-DOCSTART- -X- O O")
    docs = filter_empty_string(docs)
    res = []
    for n, doc in enumerate(docs):
        sents = filter_empty_string(doc.split("\n\n"))
        for sent_n, sent in enumerate(sents):
            token_tags = filter_empty_string(sent.split("\n"))
            for t in token_tags:
                word, pos, dep, ne = t.split(" ")
                if len(s := ne.split("-")) == 2:
                    ne = s[1]
                res.append((n, sent_n, word, pos, dep, ne))
    df = pd.DataFrame(res, columns="doc_n sent_n, word pos dep ne".split())
    return df


def col_to_onehot(col):
    """
    turn column to one hot
    """
    preds = list(col.unique())
    n_predictions = len(preds)
    preds_one_hot = {pred: i for pred, i in zip(preds, range(n_predictions))}

    a = np.array(col.apply(lambda x: preds_one_hot[x]))
    b = np.zeros((a.size, a.max() + 1))
    b[np.arange(a.size), a] = 1
    return preds_one_hot, b


tf.config.run_functions_eagerly(True)


if __name__ == "__main__":
    # load tagged data
    df = get_conll()
    preds = list(df["ne"].unique())
    n_predictions = len(preds)

    # load in w2v
    w2v = KeyedVectors.load_word2vec_format(
        "GoogleNews-vectors-negative300.bin", binary=True
    )
    embedding = w2v.wv.syn0.shape
    vocab, embedding_size = embedding

    def get_embed(x):
        if x in w2v:
            return w2v[x]
        else:
            return w2v["UNK"]

    X2 = tf.constant([get_embed(w) for w in df["word"]])
    preds_one_hot, y = col_to_onehot(df["ne"])
    y = tf.constant(y)

    # build model
    # make embedding layer
    # emb = w2v.wv.get_keras_embedding(train_embeddings=False)

    model = tf.keras.Sequential()
    # model.add(emb)
    model.add(tf.keras.layers.Input(shape=(300,)))
    model.add(tf.keras.layers.Dense(128, activation="relu", name="hidden_layer"))
    model.add(
        tf.keras.layers.Dense(n_predictions,
                              activation="softmax",
                              name="prediction")
    )

    model.compile(optimizer="sgd", loss="categorical_crossentropy")
    model.summary()
    history = model.fit(X2, y, validation_split=0.1, epochs=1)

    x = tf.reshape(tf.constant(w2v["EU"]), shape=(1, 300))
    model.predict(x).round()
    preds_one_hot
    # plot loss and validation over time
