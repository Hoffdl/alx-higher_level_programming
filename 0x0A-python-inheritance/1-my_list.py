#!/usr/bin/python3
''' Module: 1-my_list
'''


class Mylist(list):
    ''' Repressents a Mylist
    '''

    def print_sorted(self):
        '''
        prints the list, but sorted
        '''
        print(sorted(self))
