##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################

import re

#Clean up the following tweet so that it contains only the user’s message.
# That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.

texted_doc = '''
#man Good advice! RT @TheNextWeb: What I would do differently if I 
was learning to code today  http://t.co/lbwej0pxOd cc: @garybernhardt #rstats  
'''

#tweet=input("Enter a text randomly: ")



def clean_tweet(text):
    text = re.sub('http\S+\s*', '', text)  # remove URLs
    text = re.sub('RT|cc', '', text)  # remove RT and cc
    text = re.sub('#\S+', '', text)  # remove hashtags
    text = re.sub('@\S+', '', text)  # remove mentions
    text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', text)  # remove punctuations
    text = re.sub('\s+', ' ', text)  # remove extra whitespace
    return text

print(clean_tweet(texted_doc))


#desired_output = 'Good advice What I would do differently if I was learning to code today'