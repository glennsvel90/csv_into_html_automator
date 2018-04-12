import os
import csv


HTML_PATH = './programs/graphic-design.htm'
CSV_FILES = ('./_assets/first_semester.csv',
                './assets/second_semester.csv')

SP_INC = 2

def create_row(row_data, **kwargs):

    # have leading spaces
    sp = ' ' * kwargs.get('line_space', 0)
    output = sp + '<tr>\n'
    # increase the numer of leading spaces
    sp += SP_INC * ' '

    if kwargs.get('is_header', False):
        # row_data is a list of string elements in the row
        for item in row_data:
            output += sp + '<th>' + item + '</th>\n'
    else:
        # look at the first column of the row and separate the course number form the name
        # and make the course number bold
        first_col = row_data[0].split(' ', 1)
        output += sp + '<td><strong>' + first_col[0] + '</strong>' + first_col[1] + '</td>\n'
        for item in row_data[1:]:
            output += sp + '<td>' + item + '</td>\n'

    sp = sp[:-SP_INC]
    return output + sp + '</tr>\n'


def create_table(csv_data, **kwargs):
    """ helper function to generate table tags by using a list of list dealing with
    csv data as one of its arguements """
    border = str(kwargs.get('border', 0))
    cellspacing = str(kwargs.get('cellspacing', 0))
    cellpadding = str(kwargs.get('cellpadding', 0))
    # have leading spaces
    sp = ' ' * kwargs.get('line_space', 0)
    output = sp + '<table border="' + border + '" cellspacing"' + cellspacing + '" cellpadding"' + cellpadding + '">\n'
    sp += SP_INC * ' '
    # make the first row a header
    output += create_row(csv_data[0], line_space = len(sp), is_header = True)
    # make the remaining row no header, just regular data
    for row_data in csv_data[1:]:
        output += create_row(row_data, line_space = len(sp))
    sp = sp[:-SP_INC]
    return output + sp + '</table>\n'


def insert_csv(html_path, csv_paths):
    """ reads CSV files; generates html tables from the data  and insert tables into the webpage and saves
    the new webpage to output.htm """
    html_origin = open(html_path)
    # read returns a string of the html. This string is cut in half where we should insert the
    # table. html_halves is a list of two strings.
    html_halves = html_origin.read().split('</article>')
    # find out the number of spaces before the article tag
    sp = (len(html_halves[0] - len(html_halves[0].rstrip(' ')))

    new_table = ''
    for path in csv_paths:
        print('Building table from' + path)
        file = open(path, 'r')
        # create a list of lists with the outer row the list of rows that was turned into a list from a generator.
        # The inner list is the lisf of row specific elements
        # The inner list is created by creating a list of strings by splitting the row elements by the comma.
        # Thus there are 2 elements in the inner list(the name of the course and the number of credits)
        csv_data = list(csv.reader(file, delimiter=','))
        #return a string, which consists of html elements
        new_table += create_table(csv_data, line_space = sp + 2)

    print('Inserting tables into copy of ' + html_path)
    output_html = html_halves[0].rstrip(' ') + new_table + (sp * ' ') + '</article>' + html_halves[1]
    output_path = os.path.dirname(html_path) + '/output.htm'
    print('Saving result to ' + output_path)
    output_file = open(output_path, 'w')
    output_file.write(output_html)

if __main__=="__main__": insert_csv(HTML_PATH, CSV_FILES)
