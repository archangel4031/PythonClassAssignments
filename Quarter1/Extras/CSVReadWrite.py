fpath = "../Extras/sample.csv"

fileObject = open(fpath, "r")

data =list()
obj = ""
for line in fileObject.readlines():
    for char in line:
        obj = obj + char
        if(obj[-1] == ","):
            obj.split(",")
    print("obj", obj)
    data.append(obj)
    # print("data",data)
    obj = ""

# for item in data:
#     print(data)