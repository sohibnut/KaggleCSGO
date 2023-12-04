from UseNeural import UseThisShit

keys = {0:"counter terrorists",
        1:"terrorists"}

test_data_file = open("csgo.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()
tj = 0

for x in test_data_list[:10000]:
    x = x.split(',')
    javob = x[11]
    if javob == 'CT':
        javob = 0
    else:
        javob = 1    
    print(keys[javob])
    query = UseThisShit(x[:11])
    print(keys[query])
    print("____________________")
    if javob==query:
        tj += 1

print(tj/1000.0)        
