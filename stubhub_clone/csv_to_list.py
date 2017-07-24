import csv
with open("performer_file.csv",'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)


for x in your_list:
    name = x[0]
    print name, 
    category = x[1]
    print category,
    popularity = x[2]
    print popularity,
    thumbnail = x[3]
    print thumbnail
    Performer.objects.create(name=name,category=category,popularity=popularity,thumbnail=thumbnail)
