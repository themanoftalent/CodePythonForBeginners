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
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

unsorted_list = [65,35,55,75,15,85,25,45,555,3,22,67,89,12,13,17,16,13,15,17,11,18,12,14,51,13,19,167,819,112,123,2174,
646,328,533,731,193,837,623,3474,5525,23,2252,627,829,122,123,1276,3,5,7,1,8,2,4,55,3,22,67,89,12,13,17,16,13,15,17,11,18,12,14,51,13,19,167,819,112,123,2174,
645,3424,536,783,132,873,523,3444,5255,243,22235,627,829,122,123,1276,3,5,7,1,8,2,4,55,3,22,67,89,12,13,17,16,13,15,17,11,18,12,14,51,13,19,167,819,112,123,2174,
643,342,537,753,137,838,223,344,5325,233,22245,627,829,122,123,1276,3,5,7,1,8,2,4,55,3,22,67,89,12,13,17,16,13,15,17,11,18,12,14,51,13,19,167,819,112,123,2174,
642,342,553,743,163,823,123,3444,5245,223,2242,627,829,122,123,127]

print(merge_sort(unsorted_list))