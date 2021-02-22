# ThamizhiLIP: Thamizhi Linguistic Information Processing Library
ThamizhiLIP, a python library, has the following functionalities:
- POS tagging
- Morphological analysis
- Dependency parsing

## How to use this library
1. Install **thamizhilip**: `pip/pip3 install thamizhilip`. This will install all required dependencies as well, including stanza that is used to do the POS tagging. After installing thamizhilip, you can start using it. **You need python 3.6 or higher** to install thamizhilip.
2. Import thamizhilip: `from thamizhilip import tamil` in your python enviornment / python IDLE.
3. Download required models: `tamil.downloadModels()`. This will download and store all the models and resources required for processing.
You are done, now. You can use this to do POS, Morphological, and Dependency Parsing.


## POS tagging
There are several POS tagsets available for Tamil. Thamizhilip can tag using either University POS (UPOS) tagset or Amrita POS tagset.
The following example show the **complete** example for POS tagging.

```markdown
from thamizhilip import tamil
tamil.downloadModels()

#Loading models, use either one of this:
#if you want to UPOS tag
mypos_model=tamil.loadModels("pos")
#if you want to Amrita tag
mypos_model=tamil.loadModels("pos","amrita")

#POS tag data, you can feed a word or sentence
print(tamil.posTag("your Tamil data here",mypos_model)

```

## Morphological Analysis
There are several tagsets available for morphological annotations. Thamizhilip uses its own tagset and Universal Feature inventory by Universal Dependencies (UFeat). Thamizhilip tagset is more gradular than UFeat.
The following example show the **complete** example for Morphological tagging.

```markdown
from thamizhilip import tamil
tamil.downloadModels()

#Morphological tagging, you need to feed a word at a time
#if you want to get the analysis using Thamizhilip tagset
print(tamil.morphTag("your Tamil word"))

#if you want to get the analysis using Universal Feature Set
print(tamil.morphTag("your Tamil word","ud"))

```


## Morphological Analysis
There are several tagsets available for morphological annotations. Thamizhilip uses its own tagset and Universal Feature inventory by Universal Dependencies (UFeat). Thamizhilip tagset is more gradular than UFeat.
The following example show the **complete** example for Morphological tagging.

```markdown
from thamizhilip import tamil
tamil.downloadModels()

#Morphological tagging, you need to feed a word at a time
#if you want to get the analysis using Thamizhilip tagset
print(tamil.morphTag("your Tamil word"))

#if you want to get the analysis using Universal Feature Set
print(tamil.morphTag("your Tamil word","ud"))

```

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)


For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/sarves/thamizhilip/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
