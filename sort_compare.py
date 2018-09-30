#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""Sorting Algorithm Comparison"""



import timeit

import random





def creating_lists(list_lenght):

    """Creates all the lists"""  

    list=[]

    for i in range (list_lenght):

            list.append(random.randrange(0, 10000))

    return list

               



def insertion_sort(a_list):

    """Sorting the list using the insertion sort method"""

    start = timeit.timeit()

    for index in range(1, len(a_list)):

        current_value = a_list[index]

        position = index

        while position > 0 and a_list[position - 1] > current_value:

            a_list[position] = a_list[position - 1]

            position = position - 1

            a_list[position] = current_value

            

                

    end = timeit.timeit()

    

    return a_list, end-start

     

    

def shell_sort(a_list):

    """Sorting the list using the shell sort method"""

    start = timeit.timeit()

    sublist_count = len(a_list) // 2

    while sublist_count > 0:

        for start_position in range(sublist_count):

            gap_insertion_sort(a_list, start_position, sublist_count)

#        

        

        sublist_count = sublist_count // 2

    end = timeit.timeit()

    return a_list, end-start

        



def gap_insertion_sort(a_list, start, gap):

    """Defines the increments to be used in the shell sort"""

    for i in range(start + gap, len(a_list), gap):

        current_value = a_list[i]

        position = i

        while position >= gap and a_list[position - gap] >current_value:

                a_list[position] = a_list[position - gap]

                position = position - gap

        

        a_list[position] = current_value

        

        

def python_sort(a_list):

    """calls sort() on the input list"""

    start = timeit.timeit()

    new_list = a_list.sort()

    end = timeit.timeit()

    return new_list, end-start

    



if __name__ == "__main__":  

    print ("Time for a list of 500 items is: " )

    print ("    insertion sort = " + str(insertion_sort(creating_lists(500))[1]))

    print ("    shell sort = " + str(shell_sort(creating_lists(500))[1]))

    print ("    python sort = " + str(python_sort(creating_lists(500))[1]))

    print ("Time for a list of 1,000 items is: " )

    print ("    insertion sort = " + str(insertion_sort(creating_lists(1000))[1]))

    print ("    shell sort = " + str(shell_sort(creating_lists(1000))[1]))

    print ("    python sort = " + str(python_sort(creating_lists(1000))[1]))

    print ("Time for a list of 10,000 items is: " )

    print ("    insertion sort = " + str(insertion_sort(creating_lists(10000))[1]))

    print ("    shell sort = " + str(shell_sort(creating_lists(10000))[1]))

    print ("    python sort = " + str(python_sort(creating_lists(10000))[1]))


