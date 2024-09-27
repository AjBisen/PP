dec={
    102 : 'ajju',
    103 : "rupesh",
    'durection' : '4 months'
 }
# print(dec)
print(id(dec))

print(type(dec))

print(dec.items())

print(dec.keys())

print=(dec.get("ajju"))


dec[102]="ajju123"
print(dec[102])


# # dec.update({"222" : "name"})

# # print(dec)
# # print(dec[102])


# #    nested dec.

thisdict = {
  "brand": "Ford",
  "electric": False,
  "stu" : {
      123 : "rrr",
      234 : "kkk"
  }
}

print(thisdict)
print(thisdict["stu"])

print(thisdict["brand"])



# loop
for n in dec :
    print(n)
    print(dec[n])
     
