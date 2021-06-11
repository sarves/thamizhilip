# ThamizhiLIP: Thamizhi Linguistic Information Processing Library
ThamizhiLIP, a python library, has the following functionalities:
- POS tagging
- Morphological analysis
- Dependency parsing

All these have been developed on top of various tools and resources, including Stanza and foma. I have used both rule-based and deep learning approaches to create models that are used in thamizhilip. 

## How to use this library
1. Install **thamizhilip** using pip: ```pip/pip3 install thamizhilip``` This will install all required dependencies, including stanza, which used to do the POS tagging and dependency parsing. After installing thamizhilip, you can start using it. **You need python 3.6 or higher** to install thamizhilip.
2. Import thamizhilip to your python environment / python IDLE : ```from thamizhilip import tamil```
3. Download required models: ```tamil.downloadModels()``` This will download and store all the models and resources required for processing in your HOME directory.

You are done! You can use this to do POS and Morphological tagging, and Dependency Parsing.


## POS tagging
There are several POS tagsets available for Tamil. Thamizhilip uses both [University POS (UPOS)](https://universaldependencies.org/u/pos/) tagset and Amrita POS tagset. Therefore, you can get the tagging done using either tagset.

The following example shows a **complete** example for POS tagging.

```markdown
from thamizhilip import tamil
tamil.downloadModels()

#Loading models, use either one of this:
#if you want to UPOS tag
mypos_model=tamil.loadModels("pos")
#or
#if you want to Amrita tag
mypos_model=tamil.loadModels("pos","amrita")

#POS tag data, you can feed a word or sentence
print(tamil.posTag("your Tamil data here",mypos_model)

```

## Morphological Analysis
There are several tagsets available for morphological annotations. Thamizhilip uses its own tagset and [Universal Feature inventory](https://universaldependencies.org/u/feat/index.html) by Universal Dependencies (UFeat). Thamizhilip tagset is more granular than UFeat.
The following example shows a **complete** example for Morphological tagging.

```markdown
from thamizhilip import tamil
tamil.downloadModels()

#Morphological tagging, you need to feed a word at a time
#if you want to get the analysis using Thamizhilip tagset
print(tamil.morphTag("your Tamil word"))

#if you want to get the analysis using Universal Feature Set
print(tamil.morphTag("your Tamil word","ud"))

```

## Dependency Parsing
ThamizhiLIP can parse a given sentence using Universal Dependency annotation scheme. 
The following example shows a **complete** example.

```markdown
from thamizhilip import tamil
tamil.downloadModels()

#In order to use the dependency parser, you always need to load various models. 
depModel=tamil.loadModels()

#Then you can load them as shown below, 
#when parsing a sentence. Need to feed one sentence at a time. 
print(tamil.depTag("கண்ணன் அந்தப் புத்தகத்தைப் செய்தான்",depModel))

#for instance,
#>>> print(tamil.depTag("கண்ணன் அந்தப் புத்தகத்தை செய்தான்",depModels))
#would give you the following output:
#கண்ணன் அந்தப் புத்தகத்தைப் செய்தான்
#1|PROPN|nsubj|4
#2|DET|det|3
#3|NOUN|obj|4
#4|VERB|root|0
#5|PUNCT|punct|4

#As shown in the output above, output will have 4 columns. 
#1st column is a serial number
#2nd column UPOS
#3rd column [Dependency type](https://universaldependencies.org/u/dep/all.html)
#4th column depended word or token (its serial number is given)
 
```

### Tamil Word validator
Apart from POS, Morph, and Dependency tagging, you can use the following script to see whether a given word is a Tamil word. Basically, this script verify the structure of a word against the word formation rules given a well-known Tamil grammar text called Nannool.
https://github.com/sarves/thamizhi-preprocessor/

### Cite
If you use this tool, please cite us:
- Sarveswaran, K., Dias, G., and Butt, M. (2021). Thamizhimorph: A morphological parser for the Tamil language. Machine Translation, 35(1):37–70.
- Sarveswaran, K. and Dias, G. (2020). Thamizhiudp: A dependency parser for Tamil. In Proceedings of the 17th International Conference on Natural Language Processing, pages 200–207, Indian Institute of Technology Patna, India. NLP Association of India.
- Sarveswaran, K., Dias, G., and Butt, M. (2019). Using meta-morph rules to develop morphological analysers: A case study concerning Tamil. In Proceedings of the 14th International Conference on Finite-State Methods and Natural Language Processing, pages 76–86, Dresden, Germany. Association for Computational Linguistics.
- Sarveswaran, K., Dias, G., & Butt, M. (2018). ThamizhiFST: A Morphological Analyser and Generator for Tamil Verbs. In Proceedings of the 3rd International Conference on Information Technology Research (ICITR) (pp. 1-6). IEEE.

### Future work
A lot to be done, this is just a beginning. 
You can expect the following improvements in very near future:
- Improvement of learning models (currently, POS and Morph shows more than90% accuracy, and Dependency parser shows only 60%)
- Adding lemmatisation feature
- Adding contextual morphological analysis 
- Adding a preprocessors for various tasks, like normalisation etc.
- Nannool (நன்னூல்) based word validator (I have converted Nannool rules to python coding)

### For more information
You can find more information about these tools via the following sites:
- http://nlp-tools.uom.lk/thamizhi-pos/
- http://nlp-tools.uom.lk/thamizhi-morph
- http://nlp-tools.uom.lk/thamizhi-udp

### Acknowledgment
I would like to express my appreciation to my supervisors Prof. Gihan Dias, and Prof. Miriam Butt for all their guidance. Further, I am thankful to the National Language Processing Centre, University of Moratuwa, Sri Lanka for providing all the facilities to build the current version of ThamizhiLIP. 

In addition, I would also like to mention that this research was supported by the Accelerating Higher Education Expansion and Development (AHEAD) Operation of the Ministry of Higher Education, Sri Lanka funded by the World Bank, and also supported by the DAAD (German Academic Exchange Office)

### Contact and support
Do you have any problems? Just reach me out! - @sarves
Also feel free to fork and improve ThamizhiLIP. Also send me your valuable feedback so that I can improve this lib. 
This is released under Apache 2.0.

