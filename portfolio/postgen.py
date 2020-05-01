#!/usr/bin/python

'''
This is a scalped and reassembled version of a better Jekyll thingie someone cooler than I made.
I've pulled out all the functions I don't need and mucked around with other things in what is hopefully a non-destructive way.
'''

# Import Statements
import argparse
import datetime
import subprocess
import os.path
import sys

DEFAULT_EXT = 'md'

def main():
    # parse the arguments
    parser = argparse.ArgumentParser(description='Create a new Jekyll post.')
    parser.add_argument('title', help='the title of the post wrapped in quotes.')
    parser.add_argument('-d', '--date', help='specify the post date in the format YYYY-MM-DD, otherwise today is the default date.')
    parser.add_argument('-n', '--name', help='specify the name of the post file instead of the automatically generated one. It is a best practice for the words to be separated by hyphens. Also note that the given name will be prepended with the date so as to conform to Jekyll naming requirements.')
    args = parser.parse_args()

    title = args.title
    # exchange spaces for dashes
    dash_title = ''
    if args.name:
        dash_title = args.name.replace(' ','-')
    else:
        dash_title = title.replace(' ','-')

    # clean up any special characters from the dash-title
    temp_title = ''
    for char in dash_title:
        if char.isalnum() or char == '-':
            temp_title += char
    dash_title = temp_title

    date = None
    if args.date:
        date = args.date
    else:
        # use today's date
        today = datetime.datetime.now()
        year = str(today.year)
        month = str(today.month)
        if len(month) == 1:
            month = '0' + month
        #month = today.month > 9 ? str(today.month) : '0' + str(today.month)
        day = str(today.day)
        if len(day) == 1:
            day = '0' + day
        #day = today.day > 9 ? str(today.day) : '0' + str(today.day)
        date = "-".join([year,month,day])

    #filename = '%s-%s.%s', date, title, DEFAULT_EXT
    filename = date + '-' + dash_title + '.' + DEFAULT_EXT

    # check if the desired file already exists
    if os.path.exists(filename):
        # file already exists, abort the program
        print (filename + ' already exists.')
        print ('Jekyll post NOT created.')
        sys.exit(1)
    
    # try writing yaml to the post file
    try:
        f = open(filename, 'w')

        # write yaml to file
        try:
            f.write('---\n')
            f.write('layout: portfolio\n')
            f.write('title: ' + title + '\n')
            f.write('---\n\n')
        finally:
            f.close()
    except IOError:
        print ('Issue writing to Jekyll post file.')
    # print confirmation statement
    print ('New Jekyll post "' + title + '" has been created -- ' + filename)

if __name__ == '__main__':
    main()