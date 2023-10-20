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
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20,65,35,55,75,15,85,25,45,555,3,22,67,89,12,13,17,16,13,15,17,11,18,12,14,51,13,19,167,819,112,123,2174,
646,328,533,731,193,837,623,3474,5525,23,2252,627,829,122,123,1276,3,5,7,1,8,2,4,55,3,22,67,89,12,13,17,16,13,15,17,11,18,12,14,51,13,19,167,819,112,123,2174,
645,3424,536,783,132,873,523,3444,5255,243,22235,627,829,122,123,1276,3,5,7,1,8,2,4,55,3,22,67,89,12,13,17,16,13,15,17,11,18,12,14,51,13,19,167,819,112,123,2174,
643,342,537,753,137,838,223,344,5325,233,22245,627,829,122,123,1276,3,5,7,1,8,2,4,55,3,22,67,89,12,13,17,16,13,15,17,11,18,12,14,51,13,19,167,819,112,123,2174,
642,342,553,743,163,823,123,3444,5245,223,2242,627,829,122,123,127]
mergeSort(alist)
print(alist)