#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Search Algorithm Comparison"""


import random
import timeit


def main():
    """prints how long each function takes, on average"""       
    search_averages=creating_lists(500,100)
    print ("----results for 100 lists of 500 items----")
    print ("Sequential Search took %10.7f seconds to run, on average" % (search_averages[0]) )
    print ("ordered sequential search took %10.7f seconds to run, on average" % (search_averages[1]) )
    print ("binary search iterative took %10.7f seconds to run, on average" % (search_averages[2]) )
    print ("binary search recursive took %10.7f seconds to run, on average" % (search_averages[3]) )
    search_averages=creating_lists(1000,100)
    print ("----results for 100 lists of 1,000 items----")
    print ("Sequential Search took %10.7f seconds to run, on average" % (search_averages[0]) )
    print ("ordered sequential search took %10.7f seconds to run, on average" % (search_averages[1]) )
    print ("binary search iterative took %10.7f seconds to run, on average" % (search_averages[2]) )
    print ("binary search recursive took %10.7f seconds to run, on average" % (search_averages[3]) )
    search_averages=creating_lists(10000,100)
    print ("----results for 100 lists of 10,000 items----")
    print ("Sequential Search took %10.7f seconds to run, on average" % (search_averages[0]) )
    print ("ordered sequential search took %10.7f seconds to run, on average" % (search_averages[1]) )
    print ("binary search iterative took %10.7f seconds to run, on average" % (search_averages[2]) )
    print ("binary search recursive took %10.7f seconds to run, on average" % (search_averages[3]) )
    
def creating_lists(list_lenght,total_lists):
    """Creates all the lists"""
    sum_time1 = 0
    sum_time2 = 0
    sum_time3 = 0
    sum_time4 = 0
    for i in range(total_lists):     
        lists=[]
        for i in range (list_lenght):
                lists.append(random.randrange(0, 10000))
   
        sum_time1 =+ sequential_search(lists,-1)[1]
        sum_time2 =+ ordered_sequential_search(lists,-1)[1]
        lists.sort()
        sum_time3 =+ binary_search_iterative(lists,-1)[1]
        start = timeit.timeit()
        recursive_results=binary_search_recursive(lists,-1)
        end = timeit.timeit()
        sum_time4 =+ (end-start)
       
    return sum_time1/total_lists, sum_time2/total_lists, sum_time3/total_lists, sum_time4/total_lists

        
#SEQUENTIAL_SEARCH sum_time1
def sequential_search(a_list, item):
    start = timeit.timeit()
    pos = 0
    found = False
        
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
            
    end = timeit.timeit()
     
                     
    return found, end-start


#ORDERED SEQUENTIAL SEARCH sum_time2
def ordered_sequential_search(a_list,item):
    start = timeit.timeit()
    pos = 0
    found = False
    stop = False
    
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else: 
            if a_list[pos] > item:
                stop = True
    else:
            pos = pos+1
    end = timeit.timeit()
     
                     
    return found, end-start
       

#BINARY SEARCH ITERATIVE sum_time3
def binary_search_iterative(a_list, item):
    start = timeit.timeit()
    first = 0
    last = len(a_list) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        elif item < a_list[midpoint]:
                last = midpoint - 1
        else:
            first = midpoint + 1
            
    end = timeit.timeit()
     
                     
    return found, end-start


#BINARY SEARCH RECURSIVE sum_time4
def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


if __name__ == "__main__":
    main()
