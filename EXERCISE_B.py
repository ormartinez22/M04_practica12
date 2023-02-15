def bookStore():
    import json
    """
    
    """
    data1 = {"book":[{"title":"Elif","cover":"Air","year":"2000","pages":"625"}]}
    data2 = {"book":[{"title":"Murat","cover":"Earth","year":"1982","pages":"982"}]}
    data3 = {"book":[{"title":"BKim","cover":"Water","year":"2012","pages":"514"}]}
    data4 = {"book":[{"title":"souls","cover":"Fire","year":"1999","pages":"418"}]}

#
#output of data1
    print(json.dumps(data1))
#output of data1    
    print(json.dumps(data2))
#output of data1    
    print(json.dumps(data3))
#output of data1    
    print(json.dumps(data4))

#showing the results in jason forat to the console
#output of data1
    print(json.dumps(data1,indent=2))
#output of data1    
    print(json.dumps(data2,indent=2))
#output of data1    
    print(json.dumps(data3,indent=2))
#output of data1    
    print(json.dumps(data4,indent=2))    
#now calling the function bookStore() here:
bookStore()    