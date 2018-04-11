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
        file = open(path, 'r')
        csv_data = list(csv.reader(file, delimiter=','))
        new_table += create_table(csv_data, line_space = sp + 2)

    print('Inserting tables into copy of ' + html_path)
    output_html = html_halves[0].rstrip(' ') + new_table + (sp * ' ') + '</article>' + html_halves[1]
    output_path = os.path.dirname(html_path) + '/output.htm'
    print('Saving result to ' + output_path)
    output_file = open(output_path, 'w')
    output_file.write(output_html)

if __main__=="__main__": insert_csv(HTML_PATH, CSV_FILES)
