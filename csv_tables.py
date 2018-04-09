import os
import csv



def insert_csv(html_path, csv_paths):
    html_origin = open(html_path)
    html_halves = html_origin.read().split('</article>')
    # find out the number of spaces before the article tag
    sp = (len(html_halves[0] - len(html_halves[0].rstrip(' ')))

    new_table = ''
    for path in csv_paths:
        print('Building table from' + path)




























if __main__=="__main__": insert_csv(HTML_PATH, CSV_FILES)
