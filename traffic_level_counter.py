import csv


class GetActionProbabilities:
    @staticmethod
    def read_csv(file):
        new_list = []
        with open(file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                new_list.append(row[0].split(';'))  # Esto crea una lista de lo que hay en cada fila (le pongo que esta
                # separado por ; para que cada vez que vea ; añada un nuevo elemento a la fila
        return new_list

    def get_action_GN(self): #2935
        new_list = self.read_csv("data/Data_no_header.csv")
        countN = 0

        cHHHtoHHH = 0
        cHHHtoHHL = 0
        cHHHtoHLH = 0
        cHHHtoHLL = 0
        cHHHtoLHH = 0
        cHHHtoLHL = 0
        cHHHtoLLH = 0
        cHHHtoLLL = 0
        cHHH = 0

        cHHLtoHHH = 0
        cHHLtoHHL = 0
        cHHLtoHLH = 0
        cHHLtoHLL = 0
        cHHLtoLHH = 0
        cHHLtoLHL = 0
        cHHLtoLLH = 0
        cHHLtoLLL = 0
        cHHL = 0

        cHLHtoHHH = 0
        cHLHtoHHL = 0
        cHLHtoHLH = 0
        cHLHtoHLL = 0
        cHLHtoLHH = 0
        cHLHtoLHL = 0
        cHLHtoLLH = 0
        cHLHtoLLL = 0
        cHLH = 0

        cHLLtoHHH = 0
        cHLLtoHHL = 0
        cHLLtoHLH = 0
        cHLLtoHLL = 0
        cHLLtoLHH = 0
        cHLLtoLHL = 0
        cHLLtoLLH = 0
        cHLLtoLLL = 0
        cHLL = 0

        cLHHtoHHH = 0
        cLHHtoHHL = 0
        cLHHtoHLH = 0
        cLHHtoHLL = 0
        cLHHtoLHH = 0
        cLHHtoLHL = 0
        cLHHtoLLH = 0
        cLHHtoLLL = 0
        cLHH = 0

        cLHLtoHHH = 0
        cLHLtoHHL = 0
        cLHLtoHLH = 0
        cLHLtoHLL = 0
        cLHLtoLHH = 0
        cLHLtoLHL = 0
        cLHLtoLLH = 0
        cLHLtoLLL = 0
        cLHL = 0

        cLLHtoHHH = 0
        cLLHtoHHL = 0
        cLLHtoHLH = 0
        cLLHtoHLL = 0
        cLLHtoLHH = 0
        cLLHtoLHL = 0
        cLLHtoLLH = 0
        cLLHtoLLL = 0
        cLLH = 0

        cLLLtoHHH = 0
        cLLLtoHHL = 0
        cLLLtoHLH = 0
        cLLLtoHLL = 0
        cLLLtoLHH = 0
        cLLLtoLHL = 0
        cLLLtoLLH = 0
        cLLLtoLLL = 0
        cLLL = 0

        for row in new_list:
            if row[3] == 'N':
                if row[0] == 'High' and row[1] == 'High' and row[2] == 'High':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cHHHtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cHHHtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cHHHtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cHHHtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cHHHtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cHHHtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cHHHtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cHHHtoLLL += 1
                    cHHH += 1

                if row[0] == 'High' and row[1] == 'High' and row[2] == 'Low':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cHHLtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cHHLtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cHHLtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cHHLtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cHHLtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cHHLtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cHHLtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cHHLtoLLL += 1
                    cHHL += 1

                if row[0] == 'High' and row[1] == 'Low' and row[2] == 'High':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cHLHtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cHLHtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cHLHtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cHLHtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cHLHtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cHLHtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cHLHtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cHLHtoLLL += 1
                    cHLH += 1

                if row[0] == 'High' and row[1] == 'Low' and row[2] == 'Low':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cHLLtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cHLLtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cHLLtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cHLLtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cHLLtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cHLLtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cHLLtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cHLLtoLLL += 1
                    cHLL += 1

                if row[0] == 'Low' and row[1] == 'High' and row[2] == 'High':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cLHHtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cLHHtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cLHHtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cLHHtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cLHHtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cLHHtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cLHHtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cLHHtoLLL += 1
                    cLHH += 1

                if row[0] == 'Low' and row[1] == 'High' and row[2] == 'Low':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cLHLtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cLHLtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cLHLtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cLHLtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cLHLtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cLHLtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cLHLtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cLHLtoLLL += 1
                    cLHL += 1

                if row[0] == 'Low' and row[1] == 'Low' and row[2] == 'High':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cLLHtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cLLHtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cLLHtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cLLHtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cLLHtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cLLHtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cLLHtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cLLHtoLLL += 1
                    cLLH += 1

                if row[0] == 'Low' and row[1] == 'Low' and row[2] == 'Low':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cLLLtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cLLLtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cLLLtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cLLLtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cLLLtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cLLLtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cLLLtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cLLLtoLLL += 1
                    cLLL += 1

                countN += 1

        print("-----HHH-----")
        print("TO HHH:", cHHHtoHHH)
        print("TO HHL:", cHHHtoHHL)
        print("TO HLH:", cHHHtoHLH)
        print("TO HLL:", cHHHtoHLL)
        print("TO LHH:", cHHHtoLHH)
        print("TO LHL:", cHHHtoLHL)
        print("TO LLH:", cHHHtoLLH)
        print("TO LLL:", cHHHtoLLL)
        print("TOTAL HHH:", cHHH)
        print("---------------------------\n")
        print("-----HHL-----")
        print("TO HHH:", cHHLtoHHH)
        print("TO HHL:", cHHLtoHHL)
        print("TO HLH:", cHHLtoHLH)
        print("TO HLL:", cHHLtoHLL)
        print("TO LHH:", cHHLtoLHH)
        print("TO LHL:", cHHLtoLHL)
        print("TO LLH:", cHHLtoLLH)
        print("TO LLL:", cHHLtoLLL)
        print("TOTAL HHL:", cHHL)
        print("--------------------------\n")
        print("-----HLH-----")
        print("TO HHH:", cHLHtoHHH)
        print("TO HHL:", cHLHtoHHL)
        print("TO HLH:", cHLHtoHLH)
        print("TO HLL:", cHLHtoHLL)
        print("TO LHH:", cHLHtoLHH)
        print("TO LHL:", cHLHtoLHL)
        print("TO LLH:", cHLHtoLLH)
        print("TO LLL:", cHLHtoLLL)
        print("TOTAL HLH:", cHLH)
        print("-----------------------------\n")
        print("-----HLL-----")
        print("TO HHH:", cHLLtoHHH)
        print("TO HHL:", cHLLtoHHL)
        print("TO HLH:", cHLLtoHLH)
        print("TO HLL:", cHLLtoHLL)
        print("TO LHH:", cHLLtoLHH)
        print("TO LHL:", cHLLtoLHL)
        print("TO LLH:", cHLLtoLLH)
        print("TO LLL:", cHLLtoLLL)
        print("TOTAL HLL:", cHLL)
        print("-----------------------------\n")
        print("-----LHH-----")
        print("TO HHH:", cLHHtoHHH)
        print("TO HHL:", cLHHtoHHL)
        print("TO HLH:", cLHHtoHLH)
        print("TO HLL:", cLHHtoHLL)
        print("TO LHH:", cLHHtoLHH)
        print("TO LHL:", cLHHtoLHL)
        print("TO LLH:", cLHHtoLLH)
        print("TO LLL:", cLHHtoLLL)
        print("TOTAL LHH:", cLHH)
        print("-----------------------------\n")
        print("-----LHL-----")
        print("TO HHH:", cLHLtoHHH)
        print("TO HHL:", cLHLtoHHL)
        print("TO HLH:", cLHLtoHLH)
        print("TO HLL:", cLHLtoHLL)
        print("TO LHH:", cLHLtoLHH)
        print("TO LHL:", cLHLtoLHL)
        print("TO LLH:", cLHLtoLLH)
        print("TO LLL:", cLHLtoLLL)
        print("TOTAL LHL:", cLHL)
        print("-----------------------------\n")
        print("-----LLH-----")
        print("TO HHH:", cLLHtoHHH)
        print("TO HHL:", cLLHtoHHL)
        print("TO HLH:", cLLHtoHLH)
        print("TO HLL:", cLLHtoHLL)
        print("TO LHH:", cLLHtoLHH)
        print("TO LHL:", cLLHtoLHL)
        print("TO LLH:", cLLHtoLLH)
        print("TO LLL:", cLLHtoLLL)
        print("TOTAL LLH:", cLLH)
        print("-----------------------------\n")
        print("-----LLL-----")
        print("TO HHH:", cLLLtoHHH)
        print("TO HHL:", cLLLtoHHL)
        print("TO HLH:", cLLLtoHLH)
        print("TO HLL:", cLLLtoHLL)
        print("TO LHH:", cLLLtoLHH)
        print("TO LHL:", cLLLtoLHL)
        print("TO LLH:", cLLLtoLLH)
        print("TO LLL:", cLLLtoLLL)
        print("TOTAL LLL:", cLLL)
        print("------------------------------\n")
        print("-----Check total for each-----")
        totalN = 0
        for row in new_list:
            if row[3] == 'N':
                totalN += 1
        print("Total for north: ", totalN)
        totalE = 0
        for row in new_list:
            if row[3] == 'N':
                totalE += 1
        print("Total for east: ", totalE)
        totalW = 0
        for row in new_list:
            if row[3] == 'N':
                totalW += 1
        print("Total for west: ", totalW)
        print("------------------------------\n")
        print("Total # where N is applied", countN)
        print("------------------------------\n")

    def get_action_GE(self): #TOTAL 2903
        new_list = self.read_csv("data/Data_no_header.csv")
        countE = 0

        cHHHtoHHH = 0
        cHHHtoHHL = 0
        cHHHtoHLH = 0
        cHHHtoHLL = 0
        cHHHtoLHH = 0
        cHHHtoLHL = 0
        cHHHtoLLH = 0
        cHHHtoLLL = 0
        cHHH = 0

        cHHLtoHHH = 0
        cHHLtoHHL = 0
        cHHLtoHLH = 0
        cHHLtoHLL = 0
        cHHLtoLHH = 0
        cHHLtoLHL = 0
        cHHLtoLLH = 0
        cHHLtoLLL = 0
        cHHL = 0

        cHLHtoHHH = 0
        cHLHtoHHL = 0
        cHLHtoHLH = 0
        cHLHtoHLL = 0
        cHLHtoLHH = 0
        cHLHtoLHL = 0
        cHLHtoLLH = 0
        cHLHtoLLL = 0
        cHLH = 0

        cHLLtoHHH = 0
        cHLLtoHHL = 0
        cHLLtoHLH = 0
        cHLLtoHLL = 0
        cHLLtoLHH = 0
        cHLLtoLHL = 0
        cHLLtoLLH = 0
        cHLLtoLLL = 0
        cHLL = 0

        cLHHtoHHH = 0
        cLHHtoHHL = 0
        cLHHtoHLH = 0
        cLHHtoHLL = 0
        cLHHtoLHH = 0
        cLHHtoLHL = 0
        cLHHtoLLH = 0
        cLHHtoLLL = 0
        cLHH = 0

        cLHLtoHHH = 0
        cLHLtoHHL = 0
        cLHLtoHLH = 0
        cLHLtoHLL = 0
        cLHLtoLHH = 0
        cLHLtoLHL = 0
        cLHLtoLLH = 0
        cLHLtoLLL = 0
        cLHL = 0

        cLLHtoHHH = 0
        cLLHtoHHL = 0
        cLLHtoHLH = 0
        cLLHtoHLL = 0
        cLLHtoLHH = 0
        cLLHtoLHL = 0
        cLLHtoLLH = 0
        cLLHtoLLL = 0
        cLLH = 0

        cLLLtoHHH = 0
        cLLLtoHHL = 0
        cLLLtoHLH = 0
        cLLLtoHLL = 0
        cLLLtoLHH = 0
        cLLLtoLHL = 0
        cLLLtoLLH = 0
        cLLLtoLLL = 0
        cLLL = 0

        for row in new_list:
            if row[3] == 'E':
                if row[0] == 'High' and row[1] == 'High' and row[2] == 'High':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cHHHtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cHHHtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cHHHtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cHHHtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cHHHtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cHHHtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cHHHtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cHHHtoLLL += 1
                    cHHH += 1

                if row[0] == 'High' and row[1] == 'High' and row[2] == 'Low':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cHHLtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cHHLtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cHHLtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cHHLtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cHHLtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cHHLtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cHHLtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cHHLtoLLL += 1
                    cHHL += 1

                if row[0] == 'High' and row[1] == 'Low' and row[2] == 'High':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cHLHtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cHLHtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cHLHtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cHLHtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cHLHtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cHLHtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cHLHtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cHLHtoLLL += 1
                    cHLH += 1

                if row[0] == 'High' and row[1] == 'Low' and row[2] == 'Low':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cHLLtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cHLLtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cHLLtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cHLLtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cHLLtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cHLLtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cHLLtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cHLLtoLLL += 1
                    cHLL += 1

                if row[0] == 'Low' and row[1] == 'High' and row[2] == 'High':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cLHHtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cLHHtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cLHHtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cLHHtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cLHHtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cLHHtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cLHHtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cLHHtoLLL += 1
                    cLHH += 1

                if row[0] == 'Low' and row[1] == 'High' and row[2] == 'Low':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cLHLtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cLHLtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cLHLtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cLHLtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cLHLtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cLHLtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cLHLtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cLHLtoLLL += 1
                    cLHL += 1

                if row[0] == 'Low' and row[1] == 'Low' and row[2] == 'High':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cLLHtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cLLHtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cLLHtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cLLHtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cLLHtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cLLHtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cLLHtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cLLHtoLLL += 1
                    cLLH += 1

                if row[0] == 'Low' and row[1] == 'Low' and row[2] == 'Low':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cLLLtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cLLLtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cLLLtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cLLLtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cLLLtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cLLLtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cLLLtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cLLLtoLLL += 1
                    cLLL += 1

                countE += 1

        print("-----HHH-----")
        print("TO HHH:", cHHHtoHHH)
        print("TO HHL:", cHHHtoHHL)
        print("TO HLH:", cHHHtoHLH)
        print("TO HLL:", cHHHtoHLL)
        print("TO LHH:", cHHHtoLHH)
        print("TO LHL:", cHHHtoLHL)
        print("TO LLH:", cHHHtoLLH)
        print("TO LLL:", cHHHtoLLL)
        print("TOTAL HHH:", cHHH)
        print("---------------------------\n")
        print("-----HHL-----")
        print("TO HHH:", cHHLtoHHH)
        print("TO HHL:", cHHLtoHHL)
        print("TO HLH:", cHHLtoHLH)
        print("TO HLL:", cHHLtoHLL)
        print("TO LHH:", cHHLtoLHH)
        print("TO LHL:", cHHLtoLHL)
        print("TO LLH:", cHHLtoLLH)
        print("TO LLL:", cHHLtoLLL)
        print("TOTAL HHL:", cHHL)
        print("--------------------------\n")
        print("-----HLH-----")
        print("TO HHH:", cHLHtoHHH)
        print("TO HHL:", cHLHtoHHL)
        print("TO HLH:", cHLHtoHLH)
        print("TO HLL:", cHLHtoHLL)
        print("TO LHH:", cHLHtoLHH)
        print("TO LHL:", cHLHtoLHL)
        print("TO LLH:", cHLHtoLLH)
        print("TO LLL:", cHLHtoLLL)
        print("TOTAL HLH:", cHLH)
        print("-----------------------------\n")
        print("-----HLL-----")
        print("TO HHH:", cHLLtoHHH)
        print("TO HHL:", cHLLtoHHL)
        print("TO HLH:", cHLLtoHLH)
        print("TO HLL:", cHLLtoHLL)
        print("TO LHH:", cHLLtoLHH)
        print("TO LHL:", cHLLtoLHL)
        print("TO LLH:", cHLLtoLLH)
        print("TO LLL:", cHLLtoLLL)
        print("TOTAL HLL:", cHLL)
        print("-----------------------------\n")
        print("-----LHH-----")
        print("TO HHH:", cLHHtoHHH)
        print("TO HHL:", cLHHtoHHL)
        print("TO HLH:", cLHHtoHLH)
        print("TO HLL:", cLHHtoHLL)
        print("TO LHH:", cLHHtoLHH)
        print("TO LHL:", cLHHtoLHL)
        print("TO LLH:", cLHHtoLLH)
        print("TO LLL:", cLHHtoLLL)
        print("TOTAL LHH:", cLHH)
        print("-----------------------------\n")
        print("-----LHL-----")
        print("TO HHH:", cLHLtoHHH)
        print("TO HHL:", cLHLtoHHL)
        print("TO HLH:", cLHLtoHLH)
        print("TO HLL:", cLHLtoHLL)
        print("TO LHH:", cLHLtoLHH)
        print("TO LHL:", cLHLtoLHL)
        print("TO LLH:", cLHLtoLLH)
        print("TO LLL:", cLHLtoLLL)
        print("TOTAL LHL:", cLHL)
        print("-----------------------------\n")
        print("-----LLH-----")
        print("TO HHH:", cLLHtoHHH)
        print("TO HHL:", cLLHtoHHL)
        print("TO HLH:", cLLHtoHLH)
        print("TO HLL:", cLLHtoHLL)
        print("TO LHH:", cLLHtoLHH)
        print("TO LHL:", cLLHtoLHL)
        print("TO LLH:", cLLHtoLLH)
        print("TO LLL:", cLLHtoLLL)
        print("TOTAL LLH:", cLLH)
        print("-----------------------------\n")
        print("-----LLL-----")
        print("TO HHH:", cLLLtoHHH)
        print("TO HHL:", cLLLtoHHL)
        print("TO HLH:", cLLLtoHLH)
        print("TO HLL:", cLLLtoHLL)
        print("TO LHH:", cLLLtoLHH)
        print("TO LHL:", cLLLtoLHL)
        print("TO LLH:", cLLLtoLLH)
        print("TO LLL:", cLLLtoLLL)
        print("TOTAL LLL:", cLLL)
        print("------------------------------\n")
        print("-----Check total for each-----")
        totalN = 0
        for row in new_list:
            if row[3] == 'E':
                totalN += 1
        print("Total for north: ", totalN)
        totalE = 0
        for row in new_list:
            if row[3] == 'E':
                totalE += 1
        print("Total for east: ", totalE)
        totalW = 0
        for row in new_list:
            if row[3] == 'E':
                totalW += 1
        print("Total for west: ", totalW)
        print("------------------------------\n")
        print("Total # where E is applied", countE)
        print("------------------------------\n")

    def get_action_GW(self): #2947
        new_list = self.read_csv("data/Data_no_header.csv")
        countW = 0

        cHHHtoHHH = 0
        cHHHtoHHL = 0
        cHHHtoHLH = 0
        cHHHtoHLL = 0
        cHHHtoLHH = 0
        cHHHtoLHL = 0
        cHHHtoLLH = 0
        cHHHtoLLL = 0
        cHHH = 0

        cHHLtoHHH = 0
        cHHLtoHHL = 0
        cHHLtoHLH = 0
        cHHLtoHLL = 0
        cHHLtoLHH = 0
        cHHLtoLHL = 0
        cHHLtoLLH = 0
        cHHLtoLLL = 0
        cHHL = 0

        cHLHtoHHH = 0
        cHLHtoHHL = 0
        cHLHtoHLH = 0
        cHLHtoHLL = 0
        cHLHtoLHH = 0
        cHLHtoLHL = 0
        cHLHtoLLH = 0
        cHLHtoLLL = 0
        cHLH = 0

        cHLLtoHHH = 0
        cHLLtoHHL = 0
        cHLLtoHLH = 0
        cHLLtoHLL = 0
        cHLLtoLHH = 0
        cHLLtoLHL = 0
        cHLLtoLLH = 0
        cHLLtoLLL = 0
        cHLL = 0

        cLHHtoHHH = 0
        cLHHtoHHL = 0
        cLHHtoHLH = 0
        cLHHtoHLL = 0
        cLHHtoLHH = 0
        cLHHtoLHL = 0
        cLHHtoLLH = 0
        cLHHtoLLL = 0
        cLHH = 0

        cLHLtoHHH = 0
        cLHLtoHHL = 0
        cLHLtoHLH = 0
        cLHLtoHLL = 0
        cLHLtoLHH = 0
        cLHLtoLHL = 0
        cLHLtoLLH = 0
        cLHLtoLLL = 0
        cLHL = 0

        cLLHtoHHH = 0
        cLLHtoHHL = 0
        cLLHtoHLH = 0
        cLLHtoHLL = 0
        cLLHtoLHH = 0
        cLLHtoLHL = 0
        cLLHtoLLH = 0
        cLLHtoLLL = 0
        cLLH = 0

        cLLLtoHHH = 0
        cLLLtoHHL = 0
        cLLLtoHLH = 0
        cLLLtoHLL = 0
        cLLLtoLHH = 0
        cLLLtoLHL = 0
        cLLLtoLLH = 0
        cLLLtoLLL = 0
        cLLL = 0

        for row in new_list:
            if row[3] == 'W':
                if row[0] == 'High' and row[1] == 'High' and row[2] == 'High':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cHHHtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cHHHtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cHHHtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cHHHtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cHHHtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cHHHtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cHHHtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cHHHtoLLL += 1
                    cHHH += 1

                if row[0] == 'High' and row[1] == 'High' and row[2] == 'Low':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cHHLtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cHHLtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cHHLtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cHHLtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cHHLtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cHHLtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cHHLtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cHHLtoLLL += 1
                    cHHL += 1

                if row[0] == 'High' and row[1] == 'Low' and row[2] == 'High':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cHLHtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cHLHtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cHLHtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cHLHtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cHLHtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cHLHtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cHLHtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cHLHtoLLL += 1
                    cHLH += 1

                if row[0] == 'High' and row[1] == 'Low' and row[2] == 'Low':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cHLLtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cHLLtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cHLLtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cHLLtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cHLLtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cHLLtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cHLLtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cHLLtoLLL += 1
                    cHLL += 1

                if row[0] == 'Low' and row[1] == 'High' and row[2] == 'High':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cLHHtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cLHHtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cLHHtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cLHHtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cLHHtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cLHHtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cLHHtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cLHHtoLLL += 1
                    cLHH += 1

                if row[0] == 'Low' and row[1] == 'High' and row[2] == 'Low':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cLHLtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cLHLtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cLHLtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cLHLtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cLHLtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cLHLtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cLHLtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cLHLtoLLL += 1
                    cLHL += 1

                if row[0] == 'Low' and row[1] == 'Low' and row[2] == 'High':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cLLHtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cLLHtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cLLHtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cLLHtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cLLHtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cLLHtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cLLHtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cLLHtoLLL += 1
                    cLLH += 1

                if row[0] == 'Low' and row[1] == 'Low' and row[2] == 'Low':
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'High':
                        cLLLtoHHH += 1
                    if row[4] == 'High' and row[5] == 'High' and row[6] == 'Low':
                        cLLLtoHHL += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'High':
                        cLLLtoHLH += 1
                    if row[4] == 'High' and row[5] == 'Low' and row[6] == 'Low':
                        cLLLtoHLL += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'High':
                        cLLLtoLHH += 1
                    if row[4] == 'Low' and row[5] == 'High' and row[6] == 'Low':
                        cLLLtoLHL += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'High':
                        cLLLtoLLH += 1
                    if row[4] == 'Low' and row[5] == 'Low' and row[6] == 'Low':
                        cLLLtoLLL += 1
                    cLLL += 1

                countW += 1

        print("-----HHH-----")
        print("TO HHH:", cHHHtoHHH)
        print("TO HHL:", cHHHtoHHL)
        print("TO HLH:", cHHHtoHLH)
        print("TO HLL:", cHHHtoHLL)
        print("TO LHH:", cHHHtoLHH)
        print("TO LHL:", cHHHtoLHL)
        print("TO LLH:", cHHHtoLLH)
        print("TO LLL:", cHHHtoLLL)
        print("TOTAL HHH:", cHHH)
        print("---------------------------\n")
        print("-----HHL-----")
        print("TO HHH:", cHHLtoHHH)
        print("TO HHL:", cHHLtoHHL)
        print("TO HLH:", cHHLtoHLH)
        print("TO HLL:", cHHLtoHLL)
        print("TO LHH:", cHHLtoLHH)
        print("TO LHL:", cHHLtoLHL)
        print("TO LLH:", cHHLtoLLH)
        print("TO LLL:", cHHLtoLLL)
        print("TOTAL HHL:", cHHL)
        print("--------------------------\n")
        print("-----HLH-----")
        print("TO HHH:", cHLHtoHHH)
        print("TO HHL:", cHLHtoHHL)
        print("TO HLH:", cHLHtoHLH)
        print("TO HLL:", cHLHtoHLL)
        print("TO LHH:", cHLHtoLHH)
        print("TO LHL:", cHLHtoLHL)
        print("TO LLH:", cHLHtoLLH)
        print("TO LLL:", cHLHtoLLL)
        print("TOTAL HLH:", cHLH)
        print("-----------------------------\n")
        print("-----HLL-----")
        print("TO HHH:", cHLLtoHHH)
        print("TO HHL:", cHLLtoHHL)
        print("TO HLH:", cHLLtoHLH)
        print("TO HLL:", cHLLtoHLL)
        print("TO LHH:", cHLLtoLHH)
        print("TO LHL:", cHLLtoLHL)
        print("TO LLH:", cHLLtoLLH)
        print("TO LLL:", cHLLtoLLL)
        print("TOTAL HLL:", cHLL)
        print("-----------------------------\n")
        print("-----LHH-----")
        print("TO HHH:", cLHHtoHHH)
        print("TO HHL:", cLHHtoHHL)
        print("TO HLH:", cLHHtoHLH)
        print("TO HLL:", cLHHtoHLL)
        print("TO LHH:", cLHHtoLHH)
        print("TO LHL:", cLHHtoLHL)
        print("TO LLH:", cLHHtoLLH)
        print("TO LLL:", cLHHtoLLL)
        print("TOTAL LHH:", cLHH)
        print("-----------------------------\n")
        print("-----LHL-----")
        print("TO HHH:", cLHLtoHHH)
        print("TO HHL:", cLHLtoHHL)
        print("TO HLH:", cLHLtoHLH)
        print("TO HLL:", cLHLtoHLL)
        print("TO LHH:", cLHLtoLHH)
        print("TO LHL:", cLHLtoLHL)
        print("TO LLH:", cLHLtoLLH)
        print("TO LLL:", cLHLtoLLL)
        print("TOTAL LHL:", cLHL)
        print("-----------------------------\n")
        print("-----LLH-----")
        print("TO HHH:", cLLHtoHHH)
        print("TO HHL:", cLLHtoHHL)
        print("TO HLH:", cLLHtoHLH)
        print("TO HLL:", cLLHtoHLL)
        print("TO LHH:", cLLHtoLHH)
        print("TO LHL:", cLLHtoLHL)
        print("TO LLH:", cLLHtoLLH)
        print("TO LLL:", cLLHtoLLL)
        print("TOTAL LLH:", cLLH)
        print("-----------------------------\n")
        print("-----LLL-----")
        print("TO HHH:", cLLLtoHHH)
        print("TO HHL:", cLLLtoHHL)
        print("TO HLH:", cLLLtoHLH)
        print("TO HLL:", cLLLtoHLL)
        print("TO LHH:", cLLLtoLHH)
        print("TO LHL:", cLLLtoLHL)
        print("TO LLH:", cLLLtoLLH)
        print("TO LLL:", cLLLtoLLL)
        print("TOTAL LLL:", cLLL)
        print("------------------------------\n")
        print("-----Check total for each-----")
        totalN = 0
        for row in new_list:
            if row[3] == 'W':
                totalN += 1
        print("Total for north: ", totalN)
        totalE = 0
        for row in new_list:
            if row[3] == 'W':
                totalE += 1
        print("Total for east: ", totalE)
        totalW = 0
        for row in new_list:
            if row[3] == 'W':
                totalW += 1
        print("Total for west: ", totalW)
        print("------------------------------\n")
        print("Total # where W is applied", countW)
        print("------------------------------\n")

    def print_probabilities(self):
        print("\nAction E probabilities:")
        self.get_action_GE()
        print("\nAction N probabilities:")
        self.get_action_GN()
        print("\nAction W probabilities:")
        self.get_action_GW()


GetActionProbabilities().print_probabilities()
