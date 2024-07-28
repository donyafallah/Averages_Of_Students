import csv
from statistics import mean
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name , 'r') as f :
        reader = csv.reader(f)
        rows = list(reader)
    with open(output_file_name , 'w' , newline='') as k :
        writer = csv.writer(k)
        for row in rows :
            name = row[0]
            list_grades = list()
            for grade in row[1:] :
                list_grades.append(float(grade))
            writer.writerow([name , mean(list_grades)])

def calculate_sorted_averages(input_file_name, output_file_name):  
    dictionary = OrderedDict()          
    with open(input_file_name , 'r') as f :
        reader = csv.reader(f)
        rows = list(reader)
    with open(output_file_name , 'w' , newline='') as k :
        writer = csv.writer(k)
        for row in rows :
            name = row[0]
            list_grades = list()
            for grade in row[1:] :
                list_grades.append(float(grade))
            dictionary[name] = mean(list_grades)
            sorted_dictionary = OrderedDict(sorted(dictionary.items() , key= lambda item : (item[1] , item[0])))
            list_keys = list(sorted_dictionary.keys())
            list_values = list(sorted_dictionary.values())
        for i in range(0 , len(list_keys)) :
            writer.writerow([list_keys[i] , sorted_dictionary[list_keys[i]]])    


def calculate_three_best(input_file_name, output_file_name):
    dictionary = OrderedDict()
    with open(input_file_name , 'r') as f :
        reader = csv.reader(f)
        rows = list(reader)
    with open(output_file_name , 'w' , newline='') as k :
        writer = csv.writer(k)
        for row in rows :
            name = row[0]    
            list_grades = []
            for grade in row[1:] :
                list_grades.append(float(grade))
            dictionary[name] = mean(list_grades)    
            sorted_dictionary = OrderedDict(sorted(dictionary.items() , key= lambda item : (-item[1] ,item[0])))
            list_keys = list(sorted_dictionary.keys())
            list_values = list(sorted_dictionary.values())
        for i in range (3) :
            writer.writerow([ list_keys[i] , sorted_dictionary[list_keys[i]]])


if __name__ == "__main__" :   
    input_file = "grades.csv"
    calculate_averages( input_file , "averages.csv")
    calculate_sorted_averages( input_file , "sorted_averages.csv")
    calculate_three_best( input_file , "three_best_avrages")