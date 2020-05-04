# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:05:39 2020

@author: sankalp
"""

import wikipedia as wiki
import os
a = True
while (a):
    topic = input("ENTER TOPIC TO SEARCH IN WIKIPEDIA: ")
    topic_ls = wiki.search(topic)
    for i in range(len(topic_ls)):
        print("{} {}".format(i+1,topic_ls[i]))
    try:
        choice = int(input("ENTER CHOICE NUMBER (1-10) : "))
    except:
        print("ENTER NUMBER")
    page = wiki.page(topic_ls[choice-1])
    
    title = page.title
    source = page.url
    summary = page.summary
    content = page.content
    links = page.links
    
    fname = topic_ls[choice-1]
    fname += ".txt"
    with open(fname,"a",encoding = "utf-8") as f:
        f.write("===={}====\n\n".format(title))
        f.write("====source : {}====\n\n".format(source))
        f.write("====SUMMARY====\n\n")
        f.write(summary)
        f.write("====CONTENT====\n\n")
        f.write(content)
        f.write("====LINKS====\n\n")
        f.write("\n".join(links))
    print("Your file is ready")
    
    os.startfile(fname)
    choice2 = input("WANT TO RUN THE FILE AGAIN : (y/n) ")
    if choice2.lower() == 'n':
        a=False









