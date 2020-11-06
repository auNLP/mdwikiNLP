# Class 10: Huggingface Transformers

Note: This lecture will take place on zoom at 8.15 using the meeting ID: 314 159 1711 or this [link](https://aarhusuniversity.zoom.us/j/3141591711). Furthermore changes to the plan may occur but required readings will not change.

### TL:DR
 - Required:
   - Make sure that you have downloaded a BERT model
   - Make sure that you have a google collab account set up
     - Especially make sure you can:
       - run code
       - install huggingface
       - add data
 - Recommended:
   -  Read Ch. 1-2 in the amazing introduction to Deep Neural Networks by Michael Nielsen ([ref](http://neuralnetworksanddeeplearning.com))
 - Optional
   - Read the [white paper](https://arxiv.org/abs/1910.03771) on the Transformer Library
   -  Read the original paper on transformers; [Attention is all You Need](https://arxiv.org/abs/1706.03762)
   -  Read the original paper on BERT; [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)

---

## Plan for Class

In this class we will use the `transformers` and `PyTorch` package by Huggingface 🤗 to do Named Entity Recognition classification on token sequences. The class structure will be as follows:
- Introduction to the transformer architecture
  - Including potential applications
- Using Huggingface's transformers for NER and inspecting the model
- Recent developments in Transformers
  - Transformers is a generalization of RNN
  - Transformers is a Hopfield network (what does this mean?)
  - Transformers are open-knowledge graphs (are they really?)

<!--
- Classification of NER using Embeddings and a feed-forward NN
- Classification of NER using LSTM
- Classification of NER using BERT 
- Recent developments in Transformer (transformers are RNN and hopfield networks)
  - What are the implication that attention == memory?
-->

---

## HuggingFace Transformers
HuggingFace is an NLP company which have the open-source library `transformers` as well as a couple of other convenient libraries for NLP. The `transformers` library is very easy to use and is a good place to start with transformers. It also allows you to dig deeper either using Google's `Tensorflow` or Facebook's `PyTorch`. For the class I recommend reading Huggingface's white paper on their `transformers` library ([ref](https://arxiv.org/abs/1910.03771))

Before class please download your BERT of choice. I will use the `distilbert-base-uncased` as it is fairly small and light on memory, but you could use the Danish one as well or one for your specific language. For a list of all models see [here](https://huggingface.co/models). You can download the BERT model using the following code:

```
>>> from transformers import AutoTokenizer, AutoModel
>>> tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
>>> model = AutoModel.from_pretrained("distilbert-base-uncased") 
>>> model.save_pretrained("your_desired_folder")
```
You then need to add your model to your google drive and make sure that you can access it using google collab.

## Google Collab
Google Collab is a way to gain free compute online. It is a pretty good deal, but is not useable if you have sensitive data. We will use this is class as I assume most people don't have a GPU standing around. 

For the class please make sure that you can:

1) Run code

2) Install Transformers

3) Load files (as you will need to download your models)


For a guide especially to the last bit check out [this site](https://colab.research.google.com/notebooks/io.ipynb#scrollTo=RWSJpsyKqHjH). I  recommend that you use google drive, which you can do using the following code:

```
from google.colab import drive
drive.mount('/content/drive')
```

---

## Materials used in Class
too be announced

## Related Material
- LSTM using Pytorch ([ref](https://pytorch.org/tutorials/beginner/nlp/sequence_models_tutorial.html))
- MNIST feed-forward Neural Net using PyTorch ([ref](https://www.youtube.com/watch?v=oPhxf2fXHkQ))
- Use preloaded word-embeddings with pyTorch ([ref](https://medium.com/@martinpella/how-to-use-pre-trained-word-embeddings-in-pytorch-71ca59249f76))
- The Annotated Transformer by Harvard ([ref](http://nlp.seas.harvard.edu/2018/04/03/attention.html))