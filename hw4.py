import county_demographics
import build_data
import data
import os

#task 1
# putting it together
# load data
# print entries number
#take command line arg
#then operation
#one operation per line, components separated by :
# then error handling - no file &
# malformed lines(line num, skip and cont.) but blank is good

#display
def display(counties:list[data.CountyDemographics]):
    print(len(counties)," records loaded")

#operations
def population_total(counties:list[data.CountyDemographics]):
    totalPop = 0.0
    for i in counties:
        totalPop = totalPop + i.population['2014 Population']
    return totalPop

def population_field(field:str,subField:str,counties:list[data.CountyDemographics]):
    subPop = 0.0
    fieldPop = 0.0
    for i in counties:
        percent = i.field[subField]
        subPop = percent/100 * i.population
        fieldPop = fieldPop + subPop
    return fieldPop

def percent_field(field:str,subField:str,counties:list[data.CountyDemographics]):
    percent = population_field(field,subField,counties)/ population_total(counties)
    return percent

def filter_state(st:str,counties:list[data.CountyDemographics]):
    filtered =[]
    for i in counties:
        if st == counties[i].state:
            filtered.append(i)
    return len(filtered)

def filter_greater(field:str,num:float,counties:list[data.CountyDemographics]):
    filtered = []
    for i in counties:
        if i.field[1] > num:
            filtered.append(i)
    return len(filtered)

def filter_less(field:str,num:float,counties:list[data.CountyDemographics]):
    filtered = []
    for i in counties:
        if i.field[1] < num:
            filtered.append(i)
    return len(filtered)

#main function
def operations(counties:list[data.CountyDemographics]):
    display(counties)
    try:
        #iterating through the files in the 'inputs' directory
        for file_name in os.listdir('inputs'):
            filePath = os.path.join('inputs',file_name)
            with open(filePath,'r') as file:
                lineNum = 0
                for l in file:
                    lineNum += 1
                    line = l.strip()
                    args = line.split(":")

                    # skip blank lines
                    if not line:
                        continue
                    if len(args) > 1:
                        subFields = args[1].split(".")
                    elif args[0] == "population-total":
                        if len(args) > 1: # error handling - too many arguments
                            print("Error: malformed line on line ",l+1)
                        else: #run the operation function
                            print ("2014 population: ",population_total(counties))
                    elif args[0] == "population":
                        if len(args) > 2: # error handling - too many arguments
                            print("Error: malformed line on line ",l+1)
                        else:
                            field = args[1]
                            subField = subFields[1]
                            print ("2014 ",field,": ",population_field(field,subField,counties))
                    elif args[0] == "percent":
                        if len(args) > 2: # error handling - too many arguments
                            print("Error: malformed line on line", l+1)
                        else:
                            field = args[1]
                            subField = subFields[1]
                            print("2014 ",field,"percentage: ",percent_field(field,subField,counties))
                    elif args[0] == "filter-state":
                        if len(args) > 2: # error handling - too many arguments
                            print("Error: malformed line on line", l+1)
                        else:
                            st = args[1]
                            print("Filter: state == ",st," ",filter_state(st,counties)," entries")
                    elif args[0] == "filter-gt":
                        if len(args) > 3: # error handling - too many arguments
                            print("Error: malformed line on line", l+1)
                        else:
                            field = args[1]
                            num = float(args[2])
                            print("Filter: ", field, "> ", num, filter_greater(field, num, counties), ' entries')
                    elif args[0] == "filter-lt":
                        if len(args) > 3: # error handling - too many arguments
                            print("Error: malformed line on line", l+1)
                        else:
                            field = args[1]
                            num = float(args[2])
                            print("Filter: ",field,"< ", num,filter_less(field,num,counties),' entries')
    except FileNotFoundError:
        print ("Error: no file found")


if __name__ == '__main__':
    operations(build_data.get_data())


#not graded but
# write tests for operations
# don't test reading and printing operations


# deliverables
# display - within operations and for errors
# operations
# error handling


