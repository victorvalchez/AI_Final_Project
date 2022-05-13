file = open("../data/Data_no_header.csv", "r")
# read content of file to string
data = file.read()

# get number of occurrences of the substring N in the string
occurrences_n = data.count("N")
print('Number of occurrences of the action GREEN N :', occurrences_n)  # 2935

# get number of occurrences of the substring E in the string
occurrences_e = data.count("E")
print('Number of occurrences of the action GREEN E :', occurrences_e)  # 2903

# get number of occurrences of the substring W in the string
occurrences_w = data.count("W")
print('Number of occurrences of the action GREEN W :', occurrences_w)  # 2947

sum = occurrences_w + occurrences_e + occurrences_n
print(sum)
