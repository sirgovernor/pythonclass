#list in python
myclassmate=["Erick", "Joan", "Michal","Victor","S"
                                                "olo"] #boxbracket for list
myclassmate[0]="Silvia"
myclassmate.append("Daniel")
myclassmate.insert(2, "Mercy")
myclassmate.sort()
print(type(myclassmate))
print(myclassmate)
print("my name is "+myclassmate[1])

#tuple
myfavfriuts=("Mangoes","Bananas","Apples","Pineapples","Oranges","apple")
mynumbers=[3,7,9,2,0]
mynumbers.sort()
print(myfavfriuts)
print(myfavfriuts[0])
print(mynumbers)

#sets data stracture (its unorganised)
myfavcars={"Toyata","Mercedes","Prado","Hilux","BMW"}
myfavcars.add("BMX")
print(myfavcars)

#dictonarys in python
magari={
    "name":"toyota",
    "model":"premium",
    "manufactur":"fsdgs0",
    "year":"2022"
}
print(magari)
print(magari["year"])