from setuptools import setup, find_packages

VERSION = '0.1.2' 
DESCRIPTION = "ThamizhiLIP"
LONG_DESCRIPTION = "Thamizhi Linguistic Information Processing Tools for Tamil Language Processing"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="thamizhilip", 
        version=0.11,
        author="Kengatharaiyer Sarveswaran",
        author_email="<iamsarves@gmail.com>",
        description="ThamizhiLIP",
        long_description="Thamizhi Linguistic Information Processing Tools for Tamil Language Processing",
        packages=find_packages(),
        license="Apache License, Version 2.0",
        install_requires=["stanza"], 
        keywords=['Thamizhi', 'Tamil', 'Tamil NLP'],
        python_requires='>=3.6',
        classifiers= [
		"Programming Language :: Python :: 3",
        	"License :: OSI Approved :: Apache Software License",
		"Operating System :: OS Independent",
        ]
)
