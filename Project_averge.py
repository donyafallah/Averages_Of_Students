import csv
from statistics import mean

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

if __name__ == "__main__" :   
    input_file = "grades.csv"
    calculate_averages( input_file , "averages.csv")