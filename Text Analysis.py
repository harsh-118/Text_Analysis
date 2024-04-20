import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
# import re
import string
nltk.download('punkt')

data=pd.read_excel("Output Data Structure.xlsx")
print(data['URL'][0])
for link in range (100):
    
    url=f"{data['URL'][link]}"

    #Get the html
    r=requests.get(url)  #request is module
    soup=BeautifulSoup(r.content, "html.parser")
    tex=soup.get_text()
    
    
    blocklist = ['title','p','ol','li']
    
    
    text_elements = [t for t in soup.find_all(text=True) if t.parent.name in blocklist]
    
    
    s="".join(text_elements)
    u=s.split('.')
    u.pop(-1)
    u.pop(-1)
    u.pop(-1)
    file1=".".join(u)
    
    #total_word=file1.split(" ")
    total_sent=nltk.sent_tokenize(file1)
    
    if len(file1)==0:
        
    
        data["POSITIVE SCORE"][link]=0
        data['NEGATIVE SCORE'][link]=0
        data['POLARITY SCORE'][link]=0
        data['SUBJECTIVITY SCORE'][link]=0
        data['AVG SENTENCE LENGTH'][link]=0
        data['PERCENTAGE OF COMPLEX WORDS'][link]=0
        data['FOG INDEX'][link]=0
        data['AVG NUMBER OF WORDS PER SENTENCE'][link]=0
        data['COMPLEX WORD COUNT'][link]=0
        data['WORD COUNT'][link]=0
        data['SYLLABLE PER WORD'][link]=0
        data['PERSONAL PRONOUNS'][link]=0
        data['AVG WORD LENGTH'][link]=0
        
    else:
        
        g=open("StopWords_Geographic.txt","r")
        h=open("StopWords_Names.txt","r")
        i=open("StopWords_Auditor.txt","r")
        j=open("StopWords_Currencies.txt","r")
        k=open("StopWords_DatesandNumbers.txt","r")
        l=open("StopWords_Generic.txt","r")
        m=open("StopWords_GenericLong.txt","r")
        
        gh=g.read()
        hi=h.read()
        ij=i.read()
        jk=j.read()
        kl=k.read()
        lm=l.read()
        mn=m.read()
        
        gh=nltk.word_tokenize(gh)
        hi=nltk.word_tokenize(hi)
        ij=nltk.word_tokenize(ij)
        jk=nltk.word_tokenize(jk)
        kl=nltk.word_tokenize(kl)
        lm=nltk.word_tokenize(lm)
        mn=nltk.word_tokenize(mn)
        
        stop_words=gh+hi+ij+jk+kl+lm+mn
        
        clear_file=[]
        ff=nltk.word_tokenize(file1)
        for x in ff:
            if x not in stop_words:
                clear_file.append(x)
                
        l=["<",">","?","`","~","!","@","#","$","%","^","’","&","*","(",")","_","+","|",',','.','-','=',':','.',';',"'","/",'''"''']    
        if x in clear_file:
            clear_file.remove(x)
            
        import string        
        punc_sign=string.punctuation
           
        for x in clear_file:
             if x in punc_sign:
              clear_file.remove(x)         
        
        '''
        Positive Word
        '''
        
        dict={"positive":[],"negative":[]}
        po=open("positive-words.txt","r")
        po=po.read()
        po=nltk.word_tokenize(po)
        
        
        for x in po:
            if x not in stop_words:
                dict["positive"].append(x)
                
        
        positive_c=[]
        for x in dict['positive']:
            if x in clear_file:
                positive_c.append(x)
                
        positive_count=len(positive_c)        
                
        '''
        Negative Word
        '''
        
        ng=open("negative-words.txt","r")
        ng=ng.read()
        ng=nltk.word_tokenize(ng)
        
        for x in ng:
            if x not in stop_words:
                dict["negative"].append(x)
                
        negative_c=[]
        for x in dict['negative']:
            if x in clear_file:
                negative_c.append(x)        
        negative_count=len(negative_c)   
        
        '''
        Polarity Score
        '''
        
        Polarity_Score=(positive_count-negative_count)/((positive_count+negative_count)
                                                        +0.000001)
        
        
        '''
        Total Word
        '''
        total_word=len(clear_file)
        
        
        '''
        Total Sentence
        '''
        total_sentence=nltk.sent_tokenize(file1)
        
        
        '''
        Total Word Count
        '''
        
        word_count=len(clear_file)  #total clear word
        
        '''
        Subjectivity Score
        '''
        
        subjectivity_score = (positive_count+negative_count)/((word_count) +0.000001)     
         
        '''
        Average Word Length
        '''
            
        avg_sen_len=(total_word)/len(total_sentence)
        
        '''
        Personal Pronounce
        '''
        
        # text="Rising IT cities and its impact on the economy, environment, infrastructure, and city life by the year 2040. - Blackcoffer Insights We have seen a huge development and dependence of people on technology in recent years. We have also seen the development of AI and ChatGPT in recent years. So it is a normal thing that we will become fully dependent on technology by 2040. Information technology will be a major power for all the developing nations. As a member of a developing nation, India is rapidly growing its IT base. It has also grown some IT cities which will be the major control centres for Information technology by 2040.Noida in Uttar Pradesh near New Delhi is an emerging IT sector now. Many large companies like Google, Microsoft, IBM, Infosys and others have set up their companies here. Noida has a market base of billions of dollars and is doing a great job of boosting the national economy. The establishment of so many software companies has made Noida an information technology hub.Gurgaon in Haryana is also an emerging IT hub. Many large companies like Google, Microsoft, IBM, Infosys and others have set up their companies here. Gurgaon has a market base of billions of dollars and is doing a great job of boosting the national economy.Bengaluru is called as the IT hub of India. It is also a smart city. Many large companies like Google, Microsoft, IBM, Infosys and others have set up their companies here. Bengaluru has a market base of billions of dollars and is doing a great job of boosting the national economy.Kolkata in West Bengal is an emerging major IT hub. The new Kolkata i.e. Saltlake Sector  5, New town, Rajarhat area of Kolkata is a major IT hub. The government is giving the software companies land at almost free of cost to set up the companies there. Many large companies like Google, Microsoft, IBM, Infosys and others have set up their companies here. Kolkata has a market base of billions of dollars and is doing a great job of boosting the national economy.There is a huge impact of the rising IT cities on our economy. Some of the effects are-The rising IT cities will greatly help to boost our economy. These will create a huge demand for raw materials. The products when ready will be a huge demand for the people too.– Supply means the fulfilment of demand. In a large and highly populous country like India, there is always a demand for finished products. If more IT cities do not develop, the companies cannot fulfil the needs and desires of the people of a populous country like India. As IT cities develop, more IT companies will come, which will supply more and more finished IT products to our people. is a place where different economic agents like buyers and sellers interact with one another. In a populous country like India, there is a huge market. As IT cities will grow, more and more IT companies will come from across the world and more will the competition in the market increase. This will help consumers as they will get more and more differentiated products and the market will also run smoothly. A competitive market is always good and healthy. We can safely assume that our oligopoly market will surely tend to reach a perfectly competitive market by the year 2040.As the market increases, more revenue will be generated. Now at present, the IT revenue of India is 245 million dollars, 19 million dollars more than the financial year 2022. If IT cities grow, then more companies will invest which leads to an increase in the IT market which in turn generates more revenue in India. We can expect that the IT revenue of India will cross or nearly tend to reach 10 billion dollars by 2040.The rising IT cities will create a huge impact on the environment, the maximum of which will be harmful effects. The impact of rising IT cities on the environment is-There will be cutting of trees in huge numbers to make the building of the IT companies which will cause great harm to the environment. The cutting of trees on a large scale will also cause mass degradation of forests.The IT companies will generate more carbon footprint in the atmosphere. South Asian countries including India are known for their lower carbon footprint. But if the IT sector grows this way then we will also be at the same pace of generation of carbon footprint by 2040.The cell phone and mobile towers by the telecom companies caused the death of birds which caused a great imbalance in the ecosystem. The number of sparrows has been reduced due to this phenomenon. If this goes on we can see the extinction of many bird species by 2040.There are many contributions of the IT cities on infrastructure.  They are-The rising IT cities need an excellent transport system for the supply of raw materials and delivery of the finished products into the market. So the transportation system develops in that area. So we have an excellent transport system by 2040.public transport system:- There is a need for a public transport system in the IT cities. As the IT cities are a source of employment and a huge population reside in these areas, there is an adequate need for public transport systems like buses, taxis etc. We hope that it will be improved by 2040.As a huge number of people reside in the IT cities there is a need for adequate water supply to fulfil the needs of people as well as for industries. This will help us to find many new methods of water supply and conservation by 2040.Electric supply is the lifeline of the sector. Without an electric supply, no machines will run and not even the IT cities will flourish. If the IT cities flourish this way, we going to have an excellent electric supply by 2040.As a large number of people reside in IT cities, there is a need for proper health infrastructure and healthcare facilities for the people. So with the growth of IT cities, our healthcare system will also improve by 2040.Education is the primary key or core of any nation. There must be proper education and training centres in those IT cities to fulfil the people’s demands.  So with the growth of IT cities, the education system will also develop by 2040. Our education is also going to be skill-oriented.With the growth of IT cities, more people will get jobs and will earn more. So the purchasing power of the people will increase. People will lead a better lifestyle. They will buy things of good brand value. The tastes and preferences of people will also change. The human development index is going to increase. People will buy good quality food and good quality cars. So the food, automobile and many other industries are going to increase. So there will be a huge impact on city life by 2040"
        # match=re.findall("I|we|my|ours|us",text)
        # a=match.count("I")
        # b=match.count("we")
        # c=match.count("my")
        # d=match.count("ours")
        # e=match.count("us")
        # personal_pronouns=a+b+c+d+e
        b=[]
        s=['I','we','my','ours','us']
        for x in ff:
            if x in s:
               b.append(x)
               
        personal_pronoun=len(b)       
         
          
        
        '''
        Total Character
        '''
        char=[]
        for x in clear_file:
            char.append(len(x))
            
        rec={'characters_length':char}   
        bb=pd.DataFrame(rec)
        total_characters=bb['characters_length'].sum()
        
        
        
        
        
        
        '''
        Average Word Length
        '''
        
        Average_word_len=(total_characters)/(total_word)
        
        '''
        Complex Word
        '''
        
        #vowel=['a','e','i','o','u','A','E','I','O','U']
        # for x in clear_file:
        #         if x in vowel:
        #                 new.append(x)
                  
        complex_count=[]
        for x in clear_file:
            if x.count('a')+x.count('e')+x.count('i')+x.count('o')+x.count('u')+x.count('A')+x.count('E')+x.count('I')+x.count('O')+x.count('U')>=3:
                complex_count.append(x)
                
        for x in complex_count:
            if x[-2:]=="ed" or x[-2:]=="es":
                   complex_count.remove(x)        
        
        total_complex_word=len(complex_count)
                    
        per_complex_word=len(complex_count)/len(clear_file)      
        
        '''
        Syllable Word
        '''
        syllable_word=[]
        for x in clear_file:
            if x.count('a')+x.count('e')+x.count('i')+x.count('o')+x.count('u')+x.count('A')+x.count('E')+x.count('I')+x.count('O')+x.count('U'):
                syllable_word.append(x)
                
        for x in syllable_word:
            if x[-2:]=="ed" or x[-2:]=="es":
                   syllable_word.remove(x)        
        
        total_syllable_word=len(syllable_word)   
                
        
        '''
        Fog Index
        '''
        Fog_index=0.4*(avg_sen_len+per_complex_word)    
    
                
            

        data["POSITIVE SCORE"][link]=positive_count
        data['NEGATIVE SCORE'][link]=negative_count
        data['POLARITY SCORE'][link]=Polarity_Score
        data['SUBJECTIVITY SCORE'][link]=subjectivity_score
        data['AVG SENTENCE LENGTH'][link]=avg_sen_len
        data['PERCENTAGE OF COMPLEX WORDS'][link]=per_complex_word
        data['FOG INDEX'][link]=Fog_index
        data['AVG NUMBER OF WORDS PER SENTENCE'][link]=avg_sen_len
        data['COMPLEX WORD COUNT'][link]=total_complex_word
        data['WORD COUNT'][link]=word_count
        data['SYLLABLE PER WORD'][link]=total_syllable_word
        data['PERSONAL PRONOUNS'][link]=personal_pronoun
        data['AVG WORD LENGTH'][link]=Average_word_len
         
    
