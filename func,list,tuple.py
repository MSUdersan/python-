#list

playlist = [ "shape of u","naa ready","believer","tum hi ho"]
fav_foods = [ "pizza","burger","dosa","biriyani"]
recent_loc=["home","airport","work","mall"]
print(playlist)
print(fav_foods)
print(recent_loc)

#append #we can add values in list and it will add value as last
playlist.append("oo anatava")
print("after append:",playlist)

#remove
playlist.remove("believer")
print("after remove:",playlist)

#insert #based on index we can add values in list
playlist.insert(1,"kathalikathae")
print("after insert:",playlist)

#pop ##last value get deleted
playlist.pop()
print("after pop:",playlist)

#reverse using reverse we reverse the order in list
playlist.reverse()
print("after rev:",playlist)

#count is used to check num of values count
print("count",playlist.count("naa ready"))

#list slicing use slicing we choose top mid last where evere we need the value from list
print("top 2 songs :",playlist[0:2])
print("last 2songs:",playlist[-2:])

#iteration
for food in fav_foods:
    print(food)

for song in playlist:
    print("artist :",song + " by sudersan")

#check
if "dosa" in fav_foods:
    print("yes")

#update
fav_foods[2]= "shawarma"
print(fav_foods)

#mixed data type
mixed = ["san",10.20,10]
print(mixed)

#indexlist enumerate will give index position + value so for that we will create 2 var in for loop
for i,location in enumerate(recent_loc):
    print(f" location {i}:{location}")

#tuple
trip_sum = ("ubergo","chennai","airpor",450.00,"completed")
print(trip_sum)

print(trip_sum[0])
print(len(trip_sum))

#for loop in tuple
for item in trip_sum:
    print(item)

#count
print(trip_sum.count("completed"))
#index
print(trip_sum.count("airport"))

##functiom in python means the block of reuseable code

def great():
    print("wlc to function")
great()

##function with argument
def great(name):
    print(f"hello {name},welcome")
great("san")

def add(a,b):
    print(a+b)
add(1,5)

#return
def adds(a,b):
    return a + b
result = adds(1,3)
print(result)

#args
def addd(*args):
    total = 0
    for num in args:
        total += num
        #0 += 10
        # 10 += 5
        #15 +=  1
    return total
results = addd(10,5,1)
print(results)

#kwargs

def create_profile(**kwargs):
    print("user profile")
    for key , value in kwargs.items():
        print(f"{key} : {value}")
create_profile(name = "san", age = 26)
