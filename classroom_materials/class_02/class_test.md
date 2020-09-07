# Class 2: Preprocessing, Counts, and Collocations 


### TL:DR
 - Required:
   - Download the Danish and English model for Stanza prior to class
   - Make sure you have joined the Element forum (Matrix)
   - Make sure you have everything set up from [class 1](classroom_materials/class_01/class_01.md)
 - Required if not familiar with these: 
   - GitHub:
     - Watch the Youtube series: [Using GitHub with Visual Studio Code](https://www.youtube.com/watch?v=3Tn58KQvWtU&list=PLpPVLI0A0OkLBWbcctmGxxF6VHWSQw1hi)
     - Set up a GitHub with your studygroup and discover/resolve any issues you might have
   - Live Share
     - Watch video: [Live Share with Visual Studio Code](https://www.youtube.com/watch?v=8Ck2QhMxAYg)
     - Set up a live share session with your studygroup and discover/resolve any issues you might have
 - Recommended: 
   - Read the paper on [stanza](https://arxiv.org/abs/2003.07082) (6 pages)
   - Look into regular expressions. For example [this 5 minute video](https://www.youtube.com/watch?v=UQQsYXa1EHs) or [this 6 minute read](https://medium.com/better-programming/introduction-to-regex-8c18abdd4f70)
   - Set up a [linter](https://code.visualstudio.com/docs/python/linting), i.e. code spell-checker for VS code. I use flake8 but you can use any.

---

## Plan for Class

In this class and the following we will build a `Text` class in Python which contains a which will be able to extract a variety of feautures from text. These include:
- sentence segmentation
- tokenization
- n-grams
- Token frequencies
- Outputting to dataframe
- Lemmatization *using Stanza*
- Part-of-Speech (POS) *tagging using Stanza*
- Named Entity Recognition (NER) *using regular expressions*

The class will also introduce some introduction to the module `os` for navigating your operating system.


---

## Download models for Stanza
Before class you should have downloaded the Danish and English model for Stanford's NLP library Stanza. If you don't have stanza installed see [class 1](classroom_materials/class_01/class_01.md).

For a guide on downloading stanza models follow these step for a bit more control (or if you have any issues) see their online [guide](https://stanfordnlp.github.io/stanza/download_models.html):
- Open your python editor of choice
- Run the following:

```Python
import stanza
stanza.download('en')
stanza.download('da')
```
