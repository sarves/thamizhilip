
##Copyright [2021] K.Sarveswaran (iamsarves@gmail.com)
##
##Licensed under the Apache License, Version 2.0 (the "License");
##you may not use this file except in compliance with the License.
##You may obtain a copy of the License at
##
##    http://www.apache.org/licenses/LICENSE-2.0
##
##Unless required by applicable law or agreed to in writing, software
##distributed under the License is distributed on an "AS IS" BASIS,
##WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##See the License for the specific language governing permissions and
##limitations under the License.
##
##
import stanza
import sys
import subprocess
import os
import json
import datetime
from urllib.request import urlopen
from zipfile import ZipFile
from pathlib import Path
import tqdm

#dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = str(Path.home())+"/thamizhi-models"

def downloadModels():

        path = str(Path.home())+"/thamizhi-models"
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed, may be you have already downloaded Thamizhi Models" % path)

        my_file = Path(path+"/tempfile.zip")
        if my_file.is_file():
                print("Models exist")
        else:
                zipurl = 'http://nlp-tools.uom.lk/thamizhi-models/thamizhi_models.zip'
                zipresp = urlopen(zipurl)
                tempzip = open(path+"/tempfile.zip", "wb")
                tempzip.write(zipresp.read())
                tempzip.close()
                zf = ZipFile(path+"/tempfile.zip")
                zf.extractall(path)
                zf.close()

def printUDLabel(find_ud_labels):
        label_list=[]
        lfile=open(dir_path+"/fsts/label-list","r")
        for line in lfile:
                label_list.append(line.strip())
        lfile.close()

        ud_labels=[]
        counter=0
        for x in range(len(find_ud_labels)):
                for y in range(len(label_list)):
                        if label_list[y].split(":")[0][1:]== find_ud_labels[x]:
                                if label_list[y].split(":")[1] != "_" :
                                        for z in label_list[y].split(":")[1].split("|"):
                                                ud_labels.append(z)
        ud_labels.sort()
        return "|".join(ud_labels)
        
def isEnglish(text):
        try:
                text.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
                return 0
        else:
                return 1

def loadModels(*arg):
        if len(arg)==0 or (len(arg)==1 and (arg[0]=="parsing" or arg[0]=="dependency")):
                config = {
                'processors': 'tokenize,pos,mwt,lemma,depparse',
                'lang': 'ta',
                'tokenize_model_path': dir_path+'/thamizhi_tokenizer.pt',
                'pos_model_path': dir_path+'/thamizhi_pos.pt',
                'mwt_model_path': dir_path+'/thamizhi_mwt.pt',
                'pos_pretrain_path': dir_path+'/ta_pretrain.pt',
                'lemma_model_path': dir_path+'/thamizhi_lemma.pt',
                'depparse_model_path': dir_path+'/thamizhi_depparse.pt'
                }
        elif len(arg)==1:
                if arg[0]=="pos" or arg[0]=="POS":
                        config = {
                        'processors': 'tokenize,pos',
                        'lang': 'ta',
                        'tokenize_model_path': dir_path+'/thamizhi_tokenizer.pt',
                        'pos_pretrain_path': dir_path+'/ta_pretrain.pt',
                        'pos_model_path': dir_path+'/thamizhi_pos.pt'
                        }

        elif len(arg)==2:
                if (arg[0]=="pos" or arg[0]=="POS") and (arg[1]=="amrita" or arg[1]=="AMRITA"):
                        config = {
                        'processors': 'tokenize,pos',
                        'lang': 'ta',
                        'tokenize_model_path': dir_path+'/thamizhi_tokenizer.pt',
                        'pos_pretrain_path': dir_path+'/ta_pretrain.pt',
                        'pos_model_path': dir_path+'/thamizhi_pos_amrita.pt'
                        }

        return stanza.Pipeline(**config)



def posTag(text,model):
        doc = model(text+ " .")
        postagged=""
        for sent in doc.sentences :
                for word in sent.words :
                        postagged=postagged+word.text+"|"+word.upos+"\n"
        return postagged


def find_morphemes(word):
        #reading fsts, fsts in fst_list has to be placed in a priority order in which look up should happen
        #this needs to be passed to the function using which morphemes are extracted
        fsts=[]
        f1=open(dir_path+"/fsts/fst-list","r")
        for line in f1:
                fsts.append(line.strip())
        f1.close()
        analyses=[]
        for fst in fsts:
                p1 = subprocess.Popen(["echo", word], stdout=subprocess.PIPE)
                file_name=dir_path+"/fsts/"+fst
                #print(file_name)
                p2 = subprocess.Popen(['flookup',file_name], stdin=p1.stdout, stdout=subprocess.PIPE)
                p1.stdout.close()
                output,err = p2.communicate()
                #print(output.decode("utf-8"))

                #1st analysis is broken by new line to tackle cases with multiple analysis
                #then analysis with one output is handled
                #1st each line is broken by tab to find lemma and analysis
                #then those are store in a list and returned back to main

                lines=output.decode("utf-8").strip().split("\n")
                if len(lines) > 1:
                        #print(line)
                        for line in lines:
                                analysis=line.split()
                                if len(analysis) > 1:
                                        if "?" in output.decode("utf-8"):
                                                results=0
                                        else:
                                                #print(analysis[1].strip().split("+"))
                                                analyses.append(analysis[1].strip().split("+"))
                                else:
                                        return 0
                #this is to handle cases with one output, 1st each line is broken by tab to
                #find lemma and analysis
                #then those are store in a list and returned back to main
                else:
                        analysis=output.decode("utf-8").split()
                        if len(analysis) > 1:
                                if "?" in output.decode("utf-8"):
                                        results=0
                                else:
                                        #print(analysis[1].strip().split("+"))
                                        analyses.append(analysis[1].strip().split("+"))
                                        #print(analyses)
                        else:
                                return 0
                        
        #print(analyses)
        if analyses :
                return analyses
        else:
                return 0

def guess_morphemes(word):
        gussers=[]
        f1=open(dir_path+"/fsts/guesser-list","r")
        for line in f1:
                gussers.append(line.strip())
        f1.close()
        
        analyses=[]
        for fst in gussers:
                p1 = subprocess.Popen(["echo", word], stdout=subprocess.PIPE)
                file_name=dir_path+"/fsts/"+fst
                p2 = subprocess.Popen(["flookup", file_name], stdin=p1.stdout, stdout=subprocess.PIPE)
                p1.stdout.close()
                output,err = p2.communicate()
                #1st analysis is broken by new line to tackle cases with multiple analysis
                #then analysis with one output is handled
                #1st each line is broken by tab to find lemma and analysis
                #then those are store in a list and returned back to main

                lines=output.decode("utf-8").strip().split("\n")
                if len(lines) > 1:
                        for line in lines:
                                analysis=line.split("	")
                                if len(analysis) > 1:
                                        if "?" in output.decode("utf-8"):
                                                results=0
                                        else:
                                                #print(analysis[1].strip().split("+"))
                                                analyses.append(analysis[1].strip().split("+"))
                                else:
                                        return 0

                #this is to handle cases with one output, 1st each line is broken by tab to
                #find lemma and analysis
                #then those are store in a list and returned back to main
                analysis=output.decode("utf-8").split("	")
                if len(analysis) > 1:
                        if "?" in output.decode("utf-8"):
                                results=0
                        else:
                                #print(analysis[1].strip().split("+"))
                                analyses.append(analysis[1].strip().split("+"))
                else:
                        return 0
        if analyses :
                return analyses
        else:
                return 0


def morphTag(*arg):
        punct_dict = """{".":"period",",":"comma",";":"semi-colon",":":"colon","-":"hyphen","(":"open-bracket",")":"close-bracket"}"""
        punct_json = json.loads(punct_dict)
        annotype=""
        word=arg[0].strip()
        if len(arg)==2:
                annotype=arg[1]
        analysis=[]
        if word in punct_json:
                analysis.append(word+":"+punct_json[word])
        elif word.isnumeric() :
                analysis.append(word+":NUM")
        elif isEnglish(word) == 1 :
                analysis.append(word+":English Text")
        else:
                interim_analyses = find_morphemes(word)
                #print(interim_analyses)
                if interim_analyses != 0 :
                        for each_analysis in interim_analyses:
                                lemma=""
                                lables=""
                                pos=""                                                
                                counter=0
                                for analysis_output in each_analysis:
                                        if counter==0:
                                                lemma=analysis_output
                                        elif counter==1:
                                                pos=analysis_output
                                        else:
                                                lables=lables+","+analysis_output
                                        counter=counter+1
                        if annotype=="ud":
                                analysis.append(word+"|"+printUDLabel(list(set(lables.split(",")))))
                        else:
                                analysis.append(word+'|'.join(list(set(lables.split(",")))))
                
                else:
                        gusses = guess_morphemes(word)
                        if gusses != 0 :
                                for each_guess in gusses:
                                        counter=0
                                        lemma=""
                                        lables=""
                                        pos=""
                                        for analysis_output in each_guess:
                                                if counter==0:
                                                        lemma=analysis_output
                                                elif counter==1:
                                                        pos=analysis_output
                                                else:
                                                        lables=lables+","+analysis_output
                                                counter=counter+1
                                analysis.append(word+"/"+printUDLabel(list(set(lables.split(",")))))
                        else:
                                analysis.append(word+":Unknown")
                                                
        return "\n".join(analysis)


def depTag(data_input,nlp):
        doc = nlp(data_input+ " .")
        taggeddata=data_input+"\n"
        for sent in doc.sentences :
                for word in sent.words :
                        taggeddata=taggeddata+str(word.id)+ "|" + word.upos + "|" + str(word.deprel)+ "|" + str(word.head) + "\n"
        return taggeddata


#downloadModels()
#print(posTag("தமிழ்",loadModels("pos","amrita")))
#print(depTag("அவன் புத்தகத்தை வாங்கினான்",loadModels()))
#print(morphTag("வருகிறான்","ud"))

