import csv


class GetActionProbabilities:
    costN, costE, costW = 0, 0, 0
    HHH, HHL, HLH, HLL, LHH, LHL, LLH, LLL = [], [], [], [], [], [], [], []



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
        # From state HHH
        cHHHtoHHH, cHHHtoHHL, cHHHtoHLH, cHHHtoHLL, cHHHtoLHH, cHHHtoLHL, cHHHtoLLH, cHHHtoLLL \
            = 0, 0, 0, 0, 0, 0, 0, 0
        cHHH = 0
        # From state HHL
        cHHLtoHHH, cHHLtoHHL, cHHLtoHLH, cHHLtoHLL, cHHLtoLHH, cHHLtoLHL, cHHLtoLLH, cHHLtoLLL \
            = 0, 0, 0, 0, 0, 0, 0, 0
        cHHL = 0
        # From state HHL
        cHLHtoHHH, cHLHtoHHL, cHLHtoHLH, cHLHtoHLL, cHLHtoLHH, cHLHtoLHL, cHLHtoLLH, cHLHtoLLL \
            = 0, 0, 0, 0, 0, 0, 0, 0
        cHLH = 0
        # From state HLL
        cHLLtoHHH, cHLLtoHHL, cHLLtoHLH, cHLLtoHLL, cHLLtoLHH, cHLLtoLHL, cHLLtoLLH, cHLLtoLLL \
            = 0, 0, 0, 0, 0, 0, 0, 0
        cHLL = 0
        # From state LHH
        cLHHtoHHH, cLHHtoHHL, cLHHtoHLH, cLHHtoHLL, cLHHtoLHH, cLHHtoLHL, cLHHtoLLH, cLHHtoLLL \
            = 0, 0, 0, 0, 0, 0, 0, 0
        cLHH = 0
        # From state LHL
        cLHLtoHHH, cLHLtoHHL, cLHLtoHLH, cLHLtoHLL, cLHLtoLHH, cLHLtoLHL, cLHLtoLLH, cLHLtoLLL \
            = 0, 0, 0, 0, 0, 0, 0, 0
        cLHL = 0
        # From state LLH
        cLLHtoHHH, cLLHtoHHL, cLLHtoHLH, cLLHtoHLL, cLLHtoLHH, cLLHtoLHL, cLLHtoLLH, cLLHtoLLL \
            = 0, 0, 0, 0, 0, 0, 0, 0
        cLLH = 0
        # From state LLL
        cLLLtoHHH, cLLLtoHHL, cLLLtoHLH, cLLLtoHLL, cLLLtoLHH, cLLLtoLHL, cLLLtoLLH, cLLLtoLLL \
            = 0, 0, 0, 0, 0, 0, 0, 0
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

        print("-----HHH-----")
        print("TO HHH:", round((cHHHtoHHH / cHHH), 6))
        self.HHH.append(round((cHHHtoHHH / cHHH), 6))

        print("TO HHL:", round((cHHHtoHHL / cHHH), 6))
        self.HHH.append(round((cHHHtoHHL / cHHH), 6))

        print("TO HLH:", round((cHHHtoHLH / cHHH), 6))
        self.HHH.append(round((cHHHtoHLH / cHHH), 6))

        print("TO HLL:", round((cHHHtoHLL / cHHH), 6))
        self.HHH.append(round((cHHHtoHLL / cHHH), 6))

        print("TO LHH:", round((cHHHtoLHH / cHHH), 6))
        self.HHH.append(round((cHHHtoLHH / cHHH), 6))

        print("TO LHL:", round((cHHHtoLHL / cHHH), 6))
        self.HHH.append(round((cHHHtoLHL / cHHH), 6))

        print("TO LLH:", round((cHHHtoLLH / cHHH), 6))
        self.HHH.append(round((cHHHtoLLH / cHHH), 6))

        print("TO LLL:", round((cHHHtoLLL / cHHH), 6))
        self.HHH.append(round((cHHHtoLLL / cHHH), 6))
        print("TOTAL HHH:", cHHH)
        print("---------------------------\n")
        print("-----HHL-----")
        print("TO HHH:", round((cHHLtoHHH / cHHL), 6))
        print("TO HHL:", round((cHHLtoHHL / cHHL), 6))
        print("TO HLH:", round((cHHLtoHLH / cHHL), 6))
        print("TO HLL:", round((cHHLtoHLL / cHHL), 6))
        print("TO LHH:", round((cHHLtoLHH / cHHL), 6))
        print("TO LHL:", round((cHHLtoLHL / cHHL), 6))
        print("TO LLH:", round((cHHLtoLLH / cHHL), 6))
        print("TO LLL:", round((cHHLtoLLL / cHHL), 6))
        print("TOTAL HHL:", cHHL)
        print("--------------------------\n")
        print("-----HLH-----")
        print("TO HHH:", round((cHLHtoHHH / cHLH), 6))
        print("TO HHL:", round((cHLHtoHHL / cHLH), 6))
        print("TO HLH:", round((cHLHtoHLH / cHLH), 6))
        print("TO HLL:", round((cHLHtoHLL / cHLH), 6))
        print("TO LHH:", round((cHLHtoLHH / cHLH), 6))
        print("TO LHL:", round((cHLHtoLHL / cHLH), 6))
        print("TO LLH:", round((cHLHtoLLH / cHLH), 6))
        print("TO LLL:", round((cHLHtoLLL / cHLH), 6))
        print("TOTAL HLH:", cHLH)
        print("-----------------------------\n")
        print("-----HLL-----")
        print("TO HHH:", round((cHLLtoHHH / cHLL), 6))
        print("TO HHL:", round((cHLLtoHHL / cHLL), 6))
        print("TO HLH:", round((cHLLtoHLH / cHLL), 6))
        print("TO HLL:", round((cHLLtoHLL / cHLL), 6))
        print("TO LHH:", round((cHLLtoLHH / cHLL), 6))
        print("TO LHL:", round((cHLLtoLHL / cHLL), 6))
        print("TO LLH:", round((cHLLtoLLH / cHLL), 6))
        print("TO LLL:", round((cHLLtoLLL / cHLL), 6))
        print("TOTAL HLL:", cHLL)
        print("-----------------------------\n")
        print("-----LHH-----")
        print("TO HHH:", round((cLHHtoHHH / cLHH), 6))
        print("TO HHL:", round((cLHHtoHHL / cLHH), 6))
        print("TO HLH:", round((cLHHtoHLH / cLHH), 6))
        print("TO HLL:", round((cLHHtoHLL / cLHH), 6))
        print("TO LHH:", round((cLHHtoLHH / cLHH), 6))
        print("TO LHL:", round((cLHHtoLHL / cLHH), 6))
        print("TO LLH:", round((cLHHtoLLH / cLHH), 6))
        print("TO LLL:", round((cLHHtoLLL / cLHH), 6))
        print("TOTAL LHH:", cLHH)
        print("-----------------------------\n")
        print("-----LHL-----")
        print("TO HHH:", round((cLHLtoHHH / cLHL), 6))
        print("TO HHL:", round((cLHLtoHHL / cLHL), 6))
        print("TO HLH:", round((cLHLtoHLH / cLHL), 6))
        print("TO HLL:", round((cLHLtoHLL / cLHL), 6))
        print("TO LHH:", round((cLHLtoLHH / cLHL), 6))
        print("TO LHL:", round((cLHLtoLHL / cLHL), 6))
        print("TO LLH:", round((cLHLtoLLH / cLHL), 6))
        print("TO LLL:", round((cLHLtoLLL / cLHL), 6))
        print("TOTAL LHL:", cLHL)
        print("-----------------------------\n")
        print("-----LLH-----")
        print("TO HHH:", round((cLLHtoHHH / cLLH), 6))
        print("TO HHL:", round((cLLHtoHHL / cLLH), 6))
        print("TO HLH:", round((cLLHtoHLH / cLLH), 6))
        print("TO HLL:", round((cLLHtoHLL / cLLH), 6))
        print("TO LHH:", round((cLLHtoLHH / cLLH), 6))
        print("TO LHL:", round((cLLHtoLHL / cLLH), 6))
        print("TO LLH:", round((cLLHtoLLH / cLLH), 6))
        print("TO LLL:", round((cLLHtoLLL / cLLH), 6))
        print("TOTAL LLH:", cLLH)
        print("-----------------------------\n")
        print("-----LLL-----")
        print("TO HHH:", round(cLLLtoHHH, 6))
        print("TO HHL:", round(cLLLtoHHL, 6))
        print("TO HLH:", round(cLLLtoHLH, 6))
        print("TO HLL:", round(cLLLtoHLL, 6))
        print("TO LHH:", round(cLLLtoLHH, 6))
        print("TO LHL:", round(cLLLtoLHL, 6))
        print("TO LLH:", round(cLLLtoLLH, 6))
        print("TO LLL:", round(cLLLtoLLL, 6))
        print("TOTAL LLL:", cLLL)
        print("------------------------------\n")

    def print_probabilities(self):
        print("\nAction E probabilities:")
        self.get_action('E')
        print("\nAction N probabilities:")
        self.get_action('N')
        print("\nAction W probabilities:")
        self.get_action('W')

    def bellman_equations(self, state_probs: list, prev_costs: list, state: str) -> list:
        cost = min(self.costN + state_probs[0]*prev_costHHH +state_probs[1]*)
        if state == 'HHH':
            prev_costs[0] == cost
        elif state == 'HHL':
            prev_costs[1] == cost
        elif state == 'HLH':
            prev_costs[2] == cost
        elif state == 'HLL':
            prev_costs[3] == cost
        elif state == 'LHH':
            prev_costs[4] == cost
        elif state == 'LHL':
            prev_costs[5] == cost
        elif state == 'LLH':
            prev_costs[6] == cost
        else:
            prev_costs[7] == cost
        return cost


GetActionProbabilities().print_probabilities()
