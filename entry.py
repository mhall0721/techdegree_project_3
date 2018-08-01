import csv
import re
import datetime
import os


class Entry():

    FILE = 'work_log.csv'

    def add_entry_to_file(self, *args):
        '''Entries are added to .csv file line by line.'''

        with open(self.FILE, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=' ',
                                    lineterminator='\n')
            csv_writer.writerow(args)

    def search_by_date(self, date):
        '''Search runs through entries to match by date.'''
        matches = {}
        with open(self.FILE, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=' ',
                                    lineterminator='\n')
            for line_num, line in enumerate(csv_reader):
                if line:
                    if line[0] == date:
                        matches[line_num] = line

        return matches

    def exact_search(self, entry):
        '''Search runs through entries for exact match.'''
        matches = {}
        with open(self.FILE, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=' ',
                                    lineterminator='\n')
            for line_num, line in enumerate(csv_reader):
                if line == entry:
                    matches[line_num] = line

        return matches

    def regex_search(self, pattern):
        '''Search runs through entries to match by regex pattern.'''
        matches = {}
        with open(self.FILE, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=' ',
                                    lineterminator='\n')
            for line_num, line in enumerate(csv_reader):
                if re.search(pattern, line[1]) or re.search(pattern, line[3]):
                    matches[line_num] = line
        return matches

    def search_by_time_spent(self, time):
        '''Search runs through entries to match by time spent.'''
        matches = {}
        with open(self.FILE, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=' ',
                                    lineterminator='\n')
            for line_num, line in enumerate(csv_reader):
                if line:
                    if line[2] == time:
                        matches[line_num] = line

        return matches

    def edit_file(self, action, n, entry):
        lines = {}
        '''The lines of the file are read into a dictionary.'''
        with open(self.FILE, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=' ',
                                    lineterminator='\n')

            for line_num, line in enumerate(csv_reader):
                if line_num == n:
                    if action == 'edit':  
                        lines[n] = entry
                    if action == 'delete':  
                        continue
                else:
                    lines[line_num] = line

        with open(self.FILE, 'w') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=' ',
                                    lineterminator='\n')
            for num, line in lines.items():
                csv_writer.writerow(lines[num])
            