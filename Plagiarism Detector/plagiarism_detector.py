#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:44:03 2022

@author: alishanpremani
"""

#A common problem in academic settings is plagiarism
#detection. Fortunately, software can make this pretty easy!
#
#In this problem, you'll be given two files with text in
#them. Write a function called check_plagiarism with two
#parameters, each representing a filename. The function
#should find if there are any instances of 5 or more
#consecutive words appearing in both files. If there are,
#return the longest such string of words (in terms of number
#of words, not length of the string). If there are not,
#return the boolean False.
#
#For simplicity, the files will be lower-case text and spaces
#only: there will be no punctuation, upper-case text, or
#line breaks.
#
#We've given you three files to experiment with. file_1.txt
#and file_2.txt share a series of 5 words: we would expect
#check_plagiarism("file_1.txt", "file_2.txt") to return the
#string "if i go crazy then". file_1.txt and file_3.txt
#share two series of 5 words, and one series of 11 words:
#we would expect check_plagiarism("file_1.txt", "file_3.txt")
#to return the string "i left my body lying somewhere in the
#sands of time". file_2.txt and file_3.txt do not share any
#text, so we would expect check_plagiarism("file_2.txt",
#"file_3.txt") to return the boolean False.
#
#Be careful: there are a lot of ways to do this problem, but
#some would be massively time- or memory-intensive. If you
#get a MemoryError, it means that your solution requires
#storing too much in memory for the code to ever run to
#completion. If you get a message that says "KILLED", it
#means your solution takes too long to run.

def check_plagiarism(file1,file2):
    f1 = open(file1,'r')
    f2 = open(file2,'r')
    
    text1 = f1.read().split()
    text2 = f2.read().split()
    
    #print(text1)
    #print(text2)
    
    winSize = 5
    ind1 = []
    ind2 = []
    for i1 in range(len(text1)-winSize):
        win1 = text1[i1:i1+winSize]
        for i2 in range(len(text2)-winSize):
            win2 = text2[i2:i2+winSize]
            if win1 == win2:
                ind1.append(i1)
                ind2.append(i2)
    
    f1.close()
    f2.close()
    #print(ind1)
    #print(ind2)
    
    longestList = ['1', '1', '1']
    list1 = ['1', '1', '1']
    j = 1
    
    for val,i in enumerate(ind1):
        
        if list1[j:] == text1[i:i+4]:
            list1.append(text1[i+4])
            j += 1
            
            if len(list1) > len(longestList):
                longestList = list1
        else:
            list1 = text1[i:i+5]
            if len(longestList) < 5:
                longestList = list1
            j = 1        
    
    if len(longestList) < 5:
        return False
    else:
        return(' '.join(longestList))
        
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#if i go crazy then
#i left my body lying somewhere in the sands of time
#False
print(check_plagiarism("file_1.txt", "file_2.txt"))
print(check_plagiarism("file_1.txt", "file_3.txt"))
print(check_plagiarism("file_2.txt", "file_3.txt"))




