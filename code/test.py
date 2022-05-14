from optimal_policy import GetOptimalPolicy

my_class = GetOptimalPolicy()
my_list = my_class.read_csv("./data/Data_no_header.csv")
cHHH, cHHL, cHLH, cHLL, cLHH, cLHL, cLLH = 0, 0, 0, 0, 0, 0, 0

for row in my_list:
    # HHH
    if row[0] == 'High' and row[1] == 'High' and row[2] == 'High':
        cHHH += 1

    # HHL
    if row[0] == 'High' and row[1] == 'High' and row[2] == 'Low':
        cHHL += 1

    # HLH
    if row[0] == 'High' and row[1] == 'Low' and row[2] == 'High':
        cHLH += 1

    # HLL
    if row[0] == 'High' and row[1] == 'Low' and row[2] == 'Low':
        cHLL += 1

    # LHH
    if row[0] == 'Low' and row[1] == 'High' and row[2] == 'High':
        cLHH += 1

    # LHL
    if row[0] == 'Low' and row[1] == 'High' and row[2] == 'Low':
        cLHL += 1

    # LLH
    if row[0] == 'Low' and row[1] == 'Low' and row[2] == 'High':
        cLLH += 1

print(cHHH, cHHL, cHLH, cHLL, cLHH, cLHL, cLLH)