#Nesting is possible inside a dict, we can have a list or Dict insside a dict

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

travel_log = {
    "France" : ['Paris','Fountainbleau','Lille'],
    "Germany" : ["Koeln", "Hamburg"]
}

#print(travel_log["France"][2])

nested_list = ["A","B",["C","D"]]

#print(nested_list[2][1])

travel_log = {
    "France" : {
        "num_times_visited" : 8,
        "cities visited" : ["Paris", "Lille","Fountainebleau"],

    },
    "Germany" : {
        "num_times_visited" : 4,
        "cities visited" : ["Koeln", "Hamburg"],

    }   
    
 
}

print(travel_log["Germany"]["cities visited"][1])
