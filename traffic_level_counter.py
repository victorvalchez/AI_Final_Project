import csv


class GetActionProbabilities:
    costN, costE, costW = 1, 1, 1
    HHH, HHL, HLH, HLL, LHH, LHL, LLH, LLL = [], [], [], [], [], [], [], []
    previous_costs = [[0], [0], [0], [0], [0], [0], [0], [0]]

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

        self.HHH.append(round((cHHHtoHHH / cHHH), 6))
        self.HHH.append(round((cHHHtoHHL / cHHH), 6))
        self.HHH.append(round((cHHHtoHLH / cHHH), 6))
        self.HHH.append(round((cHHHtoHLL / cHHH), 6))
        self.HHH.append(round((cHHHtoLHH / cHHH), 6))
        self.HHH.append(round((cHHHtoLHL / cHHH), 6))
        self.HHH.append(round((cHHHtoLLH / cHHH), 6))
        self.HHH.append(round((cHHHtoLLL / cHHH), 6))
        print("TOTAL HHH:", cHHH)
        print("------------------\n")
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
        self.get_action('N')
        print("-----HHH-----")
        print("TO HHH:", self.HHH[0])
        print("TO HHL:", self.HHH[1])
        print("TO HLH:", self.HHH[2])
        print("TO HLL:", self.HHH[3])
        print("TO LHH:", self.HHH[4])
        print("TO LHL:", self.HHH[5])
        print("TO LLH:", self.HHH[6])
        print("TO LLL:", self.HHH[7])
        print("--------------\n")
        #print("\nAction N probabilities:")
        #self.get_action('N')
        #print("\nAction W probabilities:")
        #self.get_action('W')

    def bellman_equations(self, prev_costs: list, state: str, iteration: int) -> list:
        costN = self.bellman_costN(iteration, prev_costs, state)
        costE = self.bellman_costE(iteration, prev_costs, state)
        costW = self.bellman_costW(iteration, prev_costs, state)
        min_cost = min(costN, costW, costE)
        if state == 'HHH':
            prev_costs[0].append(min_cost)
        elif state == 'HHL':
            prev_costs[1].append(min_cost)
        elif state == 'HLH':
            prev_costs[2].append(min_cost)
        elif state == 'HLL':
            prev_costs[3].append(min_cost)
        elif state == 'LHH':
            prev_costs[4].append(min_cost)
        elif state == 'LHL':
            prev_costs[5].append(min_cost)
        elif state == 'LLH':
            prev_costs[6].append(min_cost)
        else:
            prev_costs[7].append(min_cost)
        return prev_costs

    def bellman_costN(self, iteration, prev_costs, state):
        self.get_action('N')
        if state == 'HHH':
            state_probs = self.HHH
        elif state == 'HHL':
            state_probs = self.HHL
        elif state == 'HLH':
            state_probs = self.HLH
        elif state == 'HLL':
            state_probs = self.HLL
        elif state == 'LHH':
            state_probs = self.LHH
        elif state == 'LHL':
            state_probs = self.LHL
        elif state == 'LLH':
            state_probs = self.LLH
        else:
            state_probs = self.LLL
        costN = (self.costN +
                 state_probs[0] * prev_costs[0][iteration - 1] + state_probs[1] * prev_costs[1][iteration - 1] +
                 state_probs[2] * prev_costs[2][iteration - 1] + state_probs[3] * prev_costs[3][iteration - 1] +
                 state_probs[4] * prev_costs[4][iteration - 1] + state_probs[5] * prev_costs[5][iteration - 1] +
                 state_probs[6] * prev_costs[6][iteration - 1] + state_probs[7] * prev_costs[7][iteration - 1])
        if state == 'HHH':
            prev_costs[iteration][0] = costN
        elif state == 'HHL':
            prev_costs[iteration][1] = costN
        elif state == 'HLH':
            prev_costs[iteration][2] = costN
        elif state == 'HLL':
            prev_costs[iteration][3] = costN
        elif state == 'LHH':
            prev_costs[iteration][4] = costN
        elif state == 'LHL':
            prev_costs[iteration][5] = costN
        elif state == 'LLH':
            prev_costs[iteration][6] = costN
        else:
            prev_costs[iteration][7] = costN
        return costN

    def bellman_costE(self, iteration, prev_costs, state):
        self.get_action('E')
        if state == 'HHH':
            state_probs = self.HHH
        elif state == 'HHL':
            state_probs = self.HHL
        elif state == 'HLH':
            state_probs = self.HLH
        elif state == 'HLL':
            state_probs = self.HLL
        elif state == 'LHH':
            state_probs = self.LHH
        elif state == 'LHL':
            state_probs = self.LHL
        elif state == 'LLH':
            state_probs = self.LLH
        else:
            state_probs = self.LLL
        costE = (self.costE +
                 state_probs[0] * prev_costs[0][iteration - 1] + state_probs[1] * prev_costs[1][iteration - 1] +
                 state_probs[2] * prev_costs[2][iteration - 1] + state_probs[3] * prev_costs[3][iteration - 1] +
                 state_probs[4] * prev_costs[4][iteration - 1] + state_probs[5] * prev_costs[5][iteration - 1] +
                 state_probs[6] * prev_costs[6][iteration - 1] + state_probs[7] * prev_costs[7][iteration - 1])
        if state == 'HHH':
            prev_costs[iteration][0] = costE
        elif state == 'HHL':
            prev_costs[iteration][1] = costE
        elif state == 'HLH':
            prev_costs[iteration][2] = costE
        elif state == 'HLL':
            prev_costs[iteration][3] = costE
        elif state == 'LHH':
            prev_costs[iteration][4] = costE
        elif state == 'LHL':
            prev_costs[iteration][5] = costE
        elif state == 'LLH':
            prev_costs[iteration][6] = costE
        else:
            prev_costs[iteration][7] = costE
        return costE

    def bellman_costW(self, iteration, prev_costs, state):
        self.get_action('W')
        if state == 'HHH':
            state_probs = self.HHH
        elif state == 'HHL':
            state_probs = self.HHL
        elif state == 'HLH':
            state_probs = self.HLH
        elif state == 'HLL':
            state_probs = self.HLL
        elif state == 'LHH':
            state_probs = self.LHH
        elif state == 'LHL':
            state_probs = self.LHL
        elif state == 'LLH':
            state_probs = self.LLH
        else:
            state_probs = self.LLL
        costW = (self.costW +
                 state_probs[0] * prev_costs[0][iteration - 1] + state_probs[1] * prev_costs[1][iteration - 1] +
                 state_probs[2] * prev_costs[2][iteration - 1] + state_probs[3] * prev_costs[3][iteration - 1] +
                 state_probs[4] * prev_costs[4][iteration - 1] + state_probs[5] * prev_costs[5][iteration - 1] +
                 state_probs[6] * prev_costs[6][iteration - 1] + state_probs[7] * prev_costs[7][iteration - 1])
        if state == 'HHH':
            prev_costs[iteration][0] = costW
        elif state == 'HHL':
            prev_costs[iteration][1] = costW
        elif state == 'HLH':
            prev_costs[iteration][2] = costW
        elif state == 'HLL':
            prev_costs[iteration][3] = costW
        elif state == 'LHH':
            prev_costs[iteration][4] = costW
        elif state == 'LHL':
            prev_costs[iteration][5] = costW
        elif state == 'LLH':
            prev_costs[iteration][6] = costW
        else:
            prev_costs[iteration][7] = costW
        return costW


my_class = GetActionProbabilities()
my_class.print_probabilities()
"""prev_costs = my_class.bellman_equations(my_class.previous_costs, 'HHH', 1)
print(prev_costs)
for a in range(2, 10):
    prev_costs = my_class.bellman_equations(prev_costs, 'HHH', a)
    # HAY QUE PONER TODOS LOS ESTADOS CADA ITERATION DEL LOOP PORQUE SINO VA A DAR LIST INDEX OUT OF RANGE
    for i in range(8):
        if i == 0:
            print("V(HHH): ", prev_costs[i])
        elif i == 1:
            print("V(HHL): ", prev_costs[i])
        elif i == 2:
            print("V(HLH): ", prev_costs[i])
        elif i == 3:
            print("V(HLL): ", prev_costs[i])
        elif i == 4:
            print("V(LHH): ", prev_costs[i])
        elif i == 5:
            print("V(LHL): ", prev_costs[i])
        elif i == 6:
            print("V(LLH): ", prev_costs[i])
        else:
            print("V(LLL): ", prev_costs[i])"""


