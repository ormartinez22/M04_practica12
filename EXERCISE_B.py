#creating a function for our data as bookStore:
def bookStore():
#Now importing the json    
    import json
    """
    we are giving json to have a file with book 
    as the key and its child along with values
    """
#  creating json and values  
    data1 = {"book":[{"title":"Elif","cover":"Air","year":"2000","pages":"625"}]}
    data2 = {"book":[{"title":"Murat","cover":"Earth","year":"1982","pages":"982"}]}
    data3 = {"book":[{"title":"BKim","cover":"Water","year":"2012","pages":"514"}]}
    data4 = {"book":[{"title":"souls","cover":"Fire","year":"1999","pages":"418"}]}

#output of the 1st function of json
#output of data1
    print(json.dumps(data1))
#output of data2    
    print(json.dumps(data2))
#output of data3    
    print(json.dumps(data3))
#output of data4    
    print(json.dumps(data4))

#showing the results in jason forat to the console
#output of data1
    print(json.dumps(data1,indent=2))
#output of data2    
    print(json.dumps(data2,indent=2))
#output of data3    
    print(json.dumps(data3,indent=2))
#output of data4    
    print(json.dumps(data4,indent=2))    
#now calling the function bookStore() here:
bookStore()    