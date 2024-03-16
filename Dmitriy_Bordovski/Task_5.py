line = "it_step_course"
temp = line.split('_')

# joining result
res = temp[0] + ''.join(ele.title() for ele in temp[1:])

# printing result
print(str(res))