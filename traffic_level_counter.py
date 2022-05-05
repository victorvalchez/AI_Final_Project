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

    def get_action(self, action: str):  # 2935
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
            if row[3] == action:
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
        print("TO HHH:", cHHHtoHHH / cHHH)
        print("TO HHL:", cHHHtoHHL / cHHH)
        print("TO HLH:", cHHHtoHLH / cHHH)
        print("TO HLL:", cHHHtoHLL / cHHH)
        print("TO LHH:", cHHHtoLHH / cHHH)
        print("TO LHL:", cHHHtoLHL / cHHH)
        print("TO LLH:", cHHHtoLLH / cHHH)
        print("TO LLL:", cHHHtoLLL / cHHH)
        print("TOTAL HHH:", cHHH)
        print("---------------------------\n")
        print("-----HHL-----")
        print("TO HHH:", cHHLtoHHH / cHHL)
        print("TO HHL:", cHHLtoHHL / cHHL)
        print("TO HLH:", cHHLtoHLH / cHHL)
        print("TO HLL:", cHHLtoHLL / cHHL)
        print("TO LHH:", cHHLtoLHH / cHHL)
        print("TO LHL:", cHHLtoLHL / cHHL)
        print("TO LLH:", cHHLtoLLH / cHHL)
        print("TO LLL:", cHHLtoLLL / cHHL)
        print("TOTAL HHL:", cHHL)
        print("--------------------------\n")
        print("-----HLH-----")
        print("TO HHH:", cHLHtoHHH / cHLH)
        print("TO HHL:", cHLHtoHHL / cHLH)
        print("TO HLH:", cHLHtoHLH / cHLH)
        print("TO HLL:", cHLHtoHLL / cHLH)
        print("TO LHH:", cHLHtoLHH / cHLH)
        print("TO LHL:", cHLHtoLHL / cHLH)
        print("TO LLH:", cHLHtoLLH / cHLH)
        print("TO LLL:", cHLHtoLLL / cHLH)
        print("TOTAL HLH:", cHLH)
        print("-----------------------------\n")
        print("-----HLL-----")
        print("TO HHH:", cHLLtoHHH / cHLL)
        print("TO HHL:", cHLLtoHHL / cHLL)
        print("TO HLH:", cHLLtoHLH / cHLL)
        print("TO HLL:", cHLLtoHLL / cHLL)
        print("TO LHH:", cHLLtoLHH / cHLL)
        print("TO LHL:", cHLLtoLHL / cHLL)
        print("TO LLH:", cHLLtoLLH / cHLL)
        print("TO LLL:", cHLLtoLLL / cHLL)
        print("TOTAL HLL:", cHLL)
        print("-----------------------------\n")
        print("-----LHH-----")
        print("TO HHH:", cLHHtoHHH / cLHH)
        print("TO HHL:", cLHHtoHHL / cLHH)
        print("TO HLH:", cLHHtoHLH / cLHH)
        print("TO HLL:", cLHHtoHLL / cLHH)
        print("TO LHH:", cLHHtoLHH / cLHH)
        print("TO LHL:", cLHHtoLHL / cLHH)
        print("TO LLH:", cLHHtoLLH / cLHH)
        print("TO LLL:", cLHHtoLLL / cLHH)
        print("TOTAL LHH:", cLHH)
        print("-----------------------------\n")
        print("-----LHL-----")
        print("TO HHH:", cLHLtoHHH / cLHL)
        print("TO HHL:", cLHLtoHHL / cLHL)
        print("TO HLH:", cLHLtoHLH / cLHL)
        print("TO HLL:", cLHLtoHLL / cLHL)
        print("TO LHH:", cLHLtoLHH / cLHL)
        print("TO LHL:", cLHLtoLHL / cLHL)
        print("TO LLH:", cLHLtoLLH / cLHL)
        print("TO LLL:", cLHLtoLLL / cLHL)
        print("TOTAL LHL:", cLHL)
        print("-----------------------------\n")
        print("-----LLH-----")
        print("TO HHH:", cLLHtoHHH / cLLH)
        print("TO HHL:", cLLHtoHHL / cLLH)
        print("TO HLH:", cLLHtoHLH / cLLH)
        print("TO HLL:", cLLHtoHLL / cLLH)
        print("TO LHH:", cLLHtoLHH / cLLH)
        print("TO LHL:", cLLHtoLHL / cLLH)
        print("TO LLH:", cLLHtoLLH / cLLH)
        print("TO LLL:", cLLHtoLLL / cLLH)
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

    def print_probabilities(self):
        print("\nAction E probabilities:")
        self.get_action('E')
        print("\nAction N probabilities:")
        self.get_action('N')
        print("\nAction W probabilities:")
        self.get_action('W')


GetActionProbabilities().print_probabilities()
