ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#replace "tata!" with "World"
ft_list = ft_list[:1]
ft_list.append("World")

# alternatively:
#ft_list[1] = "World"

#replace "toto!" with "Austria"
#tuple does not have a .append() or .remove() method
temp = list(ft_tuple)
temp = temp[:1]
temp.append("Austria")
ft_tuple = tuple(temp)

#replace "tutu!" with "Vienna"
ft_set.discard("tutu!")
ft_set.add("Vienna")
sorted(ft_set)

#replace "titi!" with "42Vienna"
ft_dict["Hello"] = "42vienna"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)