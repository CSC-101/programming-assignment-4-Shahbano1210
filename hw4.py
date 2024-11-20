import county_demographics
import build_data
import data

#task 1

#operations
def population_total(counties:list[data.county_demographics])->float:
    totalPop = 0.0
    for i in counties:
        totalPop = totalPop + i.population['2014 Population']
    print ("2014 population: ",totalPop)

def population_field(field:str,counties:list[data.county_demographics]):
    subPop = 0.0
    fieldPop = 0.0
    for i in counties:
        percent = build_data.get_data(i.field)
        subPop = percent/100 * i.population
        fieldPop = fieldPop + subPop
    print ("2014 ",field,": ",fieldPop)

def percent_field(field:str,counties:list[data.county_demographics]):
    #percent of total pop that is sub
    percent = population_field(field) / population_total(counties)
    print("2014 ",field,"percentage: ",percent)

def filter_state(st:str,counties:list[data.county_demographics]):
    filtered =[]
    for i in counties:
        if st == counties[i].state:
            filtered.append(i)
    print("Filter: state == ",st,len(filtered)," entries")

def filter_greater(field:str,num:float,counties:list[data.county_demographics]):
    filtered = []
    for i in counties:
        if i.field[1] > num:
            filtered.append(i)
    print("Filter: ",field,"> ", num,len(filtered),' entries')

def filter_greater(field:str,num:float,counties:list[data.county_demographics]):
    filtered = []
    for i in counties:
        if i.field[1] < num:
            filtered.append(i)
    print("Filter: ",field,"< ", num,len(filtered),' entries')


# putting it together
# load data
# print(#number of entries))
#3xecute operations and print where appropriate
#one operation per line, components separated by :
#float only numbers

#errors
# LINE IS valid if blank
# if line is malformed (missing field of data cant be converted), print an error message to the terminal
# that states line number and continue processing

#not graded but
# write tests for operations
# don't test reading and printing operations


# deliverables
# display
# operations
# error handling


