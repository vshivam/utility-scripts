import os
filenames = os.listdir("E:\\Resu\\")
for i in filenames:
(filepath,filename)= os.path.split(i)
#print filename
uscore_pos = filename.find("_")
city_name = filename[:uscore_pos]
folder_loc=os.path.join("E:\\Resu\\",city_name)
folder_loc = folder_loc+"\\"
if not os.path.isdir(folder_loc):
os.mkdir(folder_loc)

for i in filenames:
if (os.path.isfile("E:\\Resu\\"+i)==1):
(filepath,filename)= os.path.split(i)
print filename
uscore_pos = filename.find("_")
city_name = filename[:uscore_pos]
folder_loc=os.path.join("E:\\Resu\\",city_name)
print folder_loc
folder_loc = folder_loc+"\\"
old_loc ="E:\\Resu\\"+filename
print old_loc +" old"
new_loc = folder_loc+filename
print new_loc + " new"
os.rename(old_loc,new_loc)