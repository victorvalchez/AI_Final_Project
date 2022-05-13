import csv

probs = {'N': {'HHH': [], 'HHL': [], 'HLH': [], 'HLL': [], 'LHH': [], 'LHL': [], 'LLH': [], 'LLL': []},
             'E': {'HHH': [], 'HHL': [], 'HLH': [], 'HLL': [], 'LHH': [], 'LHL': [], 'LLH': [], 'LLL': []},
             'W': {'HHH': [], 'HHL': [], 'HLH': [], 'HLL': [], 'LHH': [], 'LHL': [], 'LLH': [], 'LLL': []}}

class GetActionProbabilities:
    # Cuanto mas alto el coste mas tarda en normalizarse
    cost_action = {'N': 20, 'E': 20, 'W': 20} # cost is 20 seconds as it says it's the time it takes to change
    probs = {'N': {'HHH': [], 'HHL': [], 'HLH': [], 'HLL': [], 'LHH': [], 'LHL': [], 'LLH': [], 'LLL': []},
             'E': {'HHH': [], 'HHL': [], 'HLH': [], 'HLL': [], 'LHH': [], 'LHL': [], 'LLH': [], 'LLL': []},
             'W': {'HHH': [], 'HHL': [], 'HLH': [], 'HLL': [], 'LHH': [], 'LHL': [], 'LLH': [], 'LLL': []}}
    states = ['HHH', 'HHL', 'HLH', 'HLL', 'LHH', 'LHL', 'LLH', 'LLL']
    # probN = {'HHH': [], 'HHL': [], 'HLH': [], 'HLL': [], 'LHH': [], 'LHL': [], 'LLH': [], 'LLL': []}
    # probE = {'HHH': [], 'HHL': [], 'HLH': [], 'HLL': [], 'LHH': [], 'LHL': [], 'LLH': [], 'LLL': []}
    previous_costs = {'HHH': [0], 'HHL': [0], 'HLH': [0], 'HLL': [0], 'LHH': [0], 'LHL': [0], 'LLH': [0], 'LLL': [0]}
    final_state_values = {'HHH': 0, 'HHL': 0, 'HLH': 0, 'HLL': 0, 'LHH': 0, 'LHL': 0, 'LLH': 0, 'LLL': 0}
    optimal_policy_dict = {'HHH': '', 'HHL': '', 'HLH': '', 'HLL': '', 'LHH': '', 'LHL': '', 'LLH': '', 'LLL': ''}

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
        probs[action]['HHH'].append(round((cHHHtoHHH / cHHH), 6))
        probs[action]['HHH'].append(round((cHHHtoHHL / cHHH), 6))
        probs[action]['HHH'].append(round((cHHHtoHLH / cHHH), 6))
        self.probs[action]['HHH'].append(round((cHHHtoHLL / cHHH), 6))
        self.probs[action]['HHH'].append(round((cHHHtoLHH / cHHH), 6))
        self.probs[action]['HHH'].append(round((cHHHtoLHL / cHHH), 6))
        self.probs[action]['HHH'].append(round((cHHHtoLLH / cHHH), 6))
        self.probs[action]['HHH'].append(round((cHHHtoLLL / cHHH), 6))

        self.probs[action]['HHL'].append(round((cHHLtoHHH / cHHL), 6))
        self.probs[action]['HHL'].append(round((cHHLtoHHL / cHHL), 6))
        self.probs[action]['HHL'].append(round((cHHLtoHLH / cHHL), 6))
        self.probs[action]['HHL'].append(round((cHHLtoHLL / cHHL), 6))
        self.probs[action]['HHL'].append(round((cHHLtoLHH / cHHL), 6))
        self.probs[action]['HHL'].append(round((cHHLtoLHL / cHHL), 6))
        self.probs[action]['HHL'].append(round((cHHLtoLLH / cHHL), 6))
        self.probs[action]['HHL'].append(round((cHHLtoLLL / cHHL), 6))

        self.probs[action]['HLH'].append(round((cHLHtoHHH / cHLH), 6))
        self.probs[action]['HLH'].append(round((cHLHtoHHL / cHLH), 6))
        self.probs[action]['HLH'].append(round((cHLHtoHLH / cHLH), 6))
        self.probs[action]['HLH'].append(round((cHLHtoHLL / cHLH), 6))
        self.probs[action]['HLH'].append(round((cHLHtoLHH / cHLH), 6))
        self.probs[action]['HLH'].append(round((cHLHtoLHL / cHLH), 6))
        self.probs[action]['HLH'].append(round((cHLHtoLLH / cHLH), 6))
        self.probs[action]['HLH'].append(round((cHLHtoLLL / cHLH), 6))

        self.probs[action]['HLL'].append(round((cHLLtoHHH / cHLL), 6))
        self.probs[action]['HLL'].append(round((cHLLtoHHL / cHLL), 6))
        self.probs[action]['HLL'].append(round((cHLLtoHLH / cHLL), 6))
        self.probs[action]['HLL'].append(round((cHLLtoHLL / cHLL), 6))
        self.probs[action]['HLL'].append(round((cHLLtoLHH / cHLL), 6))
        self.probs[action]['HLL'].append(round((cHLLtoLHL / cHLL), 6))
        self.probs[action]['HLL'].append(round((cHLLtoLLH / cHLL), 6))
        self.probs[action]['HLL'].append(round((cHLLtoLLL / cHLL), 6))

        self.probs[action]['LHH'].append(round((cLHHtoHHH / cLHH), 6))
        self.probs[action]['LHH'].append(round((cLHHtoHHL / cLHH), 6))
        self.probs[action]['LHH'].append(round((cLHHtoHLH / cLHH), 6))
        self.probs[action]['LHH'].append(round((cLHHtoHLL / cLHH), 6))
        self.probs[action]['LHH'].append(round((cLHHtoLHH / cLHH), 6))
        self.probs[action]['LHH'].append(round((cLHHtoLHL / cLHH), 6))
        self.probs[action]['LHH'].append(round((cLHHtoLLH / cLHH), 6))
        self.probs[action]['LHH'].append(round((cLHHtoLLL / cLHH), 6))

        self.probs[action]['LHL'].append(round((cLHLtoHHH / cLHL), 6))
        self.probs[action]['LHL'].append(round((cLHLtoHHL / cLHL), 6))
        self.probs[action]['LHL'].append(round((cLHLtoHLH / cLHL), 6))
        self.probs[action]['LHL'].append(round((cLHLtoHLL / cLHL), 6))
        self.probs[action]['LHL'].append(round((cLHLtoLHH / cLHL), 6))
        self.probs[action]['LHL'].append(round((cLHLtoLHL / cLHL), 6))
        self.probs[action]['LHL'].append(round((cLHLtoLLH / cLHL), 6))
        self.probs[action]['LHL'].append(round((cLHLtoLLL / cLHL), 6))

        self.probs[action]['LLH'].append(round((cLLHtoHHH / cLLH), 6))
        self.probs[action]['LLH'].append(round((cLLHtoHHL / cLLH), 6))
        self.probs[action]['LLH'].append(round((cLLHtoHLH / cLLH), 6))
        self.probs[action]['LLH'].append(round((cLLHtoHLL / cLLH), 6))
        self.probs[action]['LLH'].append(round((cLLHtoLHH / cLLH), 6))
        self.probs[action]['LLH'].append(round((cLLHtoLHL / cLLH), 6))
        self.probs[action]['LLH'].append(round((cLLHtoLLH / cLLH), 6))
        self.probs[action]['LLH'].append(round((cLLHtoLLL / cLLH), 6))

        self.probs[action]['LLL'].append(round(cLLLtoHHH, 6))
        self.probs[action]['LLL'].append(round(cLLLtoHHL, 6))
        self.probs[action]['LLL'].append(round(cLLLtoHLH, 6))
        self.probs[action]['LLL'].append(round(cLLLtoHLL, 6))
        self.probs[action]['LLL'].append(round(cLLLtoLHH, 6))
        self.probs[action]['LLL'].append(round(cLLLtoLHL, 6))
        self.probs[action]['LLL'].append(round(cLLLtoLLH, 6))
        self.probs[action]['LLL'].append(round(cLLLtoLLL, 6))

    def get_all_actions_probabilities(self):
        actions = ['N', 'E', 'W']
        for i in range(3):
            self.get_action(actions[i])

    def print_probabilities(self, action: str):
        self.get_action(action)
        print("Probabilities for action", action)
        print("-----HHH-----")
        print("TO HHH:", self.probs[action]['HHH'][0])
        print("TO HHL:", self.probs[action]['HHH'][1])
        print("TO HLH:", self.probs[action]['HHH'][2])
        print("TO HLL:", self.probs[action]['HHH'][3])
        print("TO LHH:", self.probs[action]['HHH'][4])
        print("TO LHL:", self.probs[action]['HHH'][5])
        print("TO LLH:", self.probs[action]['HHH'][6])
        print("TO LLL:", self.probs[action]['HHH'][7])
        print("-----HHL-----")
        print("TO HHH:", self.probs[action]['HHL'][0])
        print("TO HHL:", self.probs[action]['HHL'][1])
        print("TO HLH:", self.probs[action]['HHL'][2])
        print("TO HLL:", self.probs[action]['HHL'][3])
        print("TO LHH:", self.probs[action]['HHL'][4])
        print("TO LHL:", self.probs[action]['HHL'][5])
        print("TO LLH:", self.probs[action]['HHL'][6])
        print("TO LLL:", self.probs[action]['HHL'][7])
        print("-----HLH-----")
        print("TO HHH:", self.probs[action]['HLH'][0])
        print("TO HHL:", self.probs[action]['HLH'][1])
        print("TO HLH:", self.probs[action]['HLH'][2])
        print("TO HLL:", self.probs[action]['HLH'][3])
        print("TO LHH:", self.probs[action]['HLH'][4])
        print("TO LHL:", self.probs[action]['HLH'][5])
        print("TO LLH:", self.probs[action]['HLH'][6])
        print("TO LLL:", self.probs[action]['HLH'][7])
        print("-----HLL-----")
        print("TO HHH:", self.probs[action]['HLL'][0])
        print("TO HHL:", self.probs[action]['HLL'][1])
        print("TO HLH:", self.probs[action]['HLL'][2])
        print("TO HLL:", self.probs[action]['HLL'][3])
        print("TO LHH:", self.probs[action]['HLL'][4])
        print("TO LHL:", self.probs[action]['HLL'][5])
        print("TO LLH:", self.probs[action]['HLL'][6])
        print("TO LLL:", self.probs[action]['HLL'][7])
        print("-----LHH-----")
        print("TO HHH:", self.probs[action]['LHH'][0])
        print("TO HHL:", self.probs[action]['LHH'][1])
        print("TO HLH:", self.probs[action]['LHH'][2])
        print("TO HLL:", self.probs[action]['LHH'][3])
        print("TO LHH:", self.probs[action]['LHH'][4])
        print("TO LHL:", self.probs[action]['LHH'][5])
        print("TO LLH:", self.probs[action]['LHH'][6])
        print("TO LLL:", self.probs[action]['LHH'][7])
        print("-----LHL-----")
        print("TO HHH:", self.probs[action]['LHL'][0])
        print("TO HHL:", self.probs[action]['LHL'][1])
        print("TO HLH:", self.probs[action]['LHL'][2])
        print("TO HLL:", self.probs[action]['LHL'][3])
        print("TO LHH:", self.probs[action]['LHL'][4])
        print("TO LHL:", self.probs[action]['LHL'][5])
        print("TO LLH:", self.probs[action]['LHL'][6])
        print("TO LLL:", self.probs[action]['LHL'][7])
        print("-----LLH-----")
        print("TO HHH:", self.probs[action]['LLH'][0])
        print("TO HHL:", self.probs[action]['LLH'][1])
        print("TO HLH:", self.probs[action]['LLH'][2])
        print("TO HLL:", self.probs[action]['LLH'][3])
        print("TO LHH:", self.probs[action]['LLH'][4])
        print("TO LHL:", self.probs[action]['LLH'][5])
        print("TO LLH:", self.probs[action]['LLH'][6])
        print("TO LLL:", self.probs[action]['LLH'][7])
        print("-----LLL-----")
        print("TO HHH:", self.probs[action]['LLL'][0])
        print("TO HHL:", self.probs[action]['LLL'][1])
        print("TO HLH:", self.probs[action]['LLL'][2])
        print("TO HLL:", self.probs[action]['LLL'][3])
        print("TO LHH:", self.probs[action]['LLL'][4])
        print("TO LHL:", self.probs[action]['LLL'][5])
        print("TO LLH:", self.probs[action]['LLL'][6])
        print("TO LLL:", self.probs[action]['LLL'][7])
        print("\n")

    def bellman_equations(self, previous_costs_dict: dict, state, iteration: int) -> dict:
        costN = self.bellman_cost(iteration, previous_costs_dict, state, 'N')
        costE = self.bellman_cost(iteration, previous_costs_dict, state, 'E')
        costW = self.bellman_cost(iteration, previous_costs_dict, state, 'W')
        min_cost = min(costN, costW, costE)
        previous_costs_dict[state].append(min_cost)

        return previous_costs_dict

    def bellman_cost(self, iteration, prev_costs, state, action):
        self.get_action(action)
        state_probs = self.probs[action][state]
        cost = self.cost_action[action]
        for i in range(8):
            cost += state_probs[i] * prev_costs[self.states[i]][iteration-1]
        return cost

    def get_states_value(self):
        flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8 = False, False, False, False, False, False, False, False
        flag_all = False
        final_pos = 0
        ite = 1
        while not flag_all:
            for i in range(8):
                if i == 7:
                    self.previous_costs['LLL'].append(0)
                else:
                    self.previous_costs = self.bellman_equations(self.previous_costs, self.states[i], ite)
            print("\nThis is the", ite, "iteration")
            # for i in range(8):
                # print("V(" + str(states[i]) + "):", self.previous_costs[states[i]])

            if round(self.previous_costs['HHH'][ite], 6) == round(self.previous_costs['HHH'][ite - 1], 6):
                flag1 = True
            if round(self.previous_costs['HHL'][ite], 6) == round(self.previous_costs['HHL'][ite - 1], 6):
                flag2 = True
            if round(self.previous_costs['HLH'][ite], 6) == round(self.previous_costs['HLH'][ite - 1], 6):
                flag3 = True
            if round(self.previous_costs['HLL'][ite], 6) == round(self.previous_costs['HLL'][ite - 1], 6):
                flag4 = True
            if round(self.previous_costs['LHH'][ite], 6) == round(self.previous_costs['LHH'][ite - 1], 6):
                flag5 = True
            if round(self.previous_costs['LHL'][ite], 6) == round(self.previous_costs['LHL'][ite - 1], 6):
                flag6 = True
            if round(self.previous_costs['LLH'][ite], 6) == round(self.previous_costs['LLH'][ite - 1], 6):
                flag7 = True
            if round(self.previous_costs['LLL'][ite], 6) == round(self.previous_costs['LLL'][ite - 1], 6):
                flag8 = True

            if flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7 and flag8:
                flag_all = True

            if flag_all:
                final_pos = ite
                break
            ite += 1

        print("Number of iterations:", final_pos)
        for i in range(8):
            self.final_state_values[self.states[i]] = round(self.previous_costs[self.states[i]][final_pos], 6)
            print("V(" + str(self.states[i]) + "):", round(self.previous_costs[self.states[i]][final_pos], 6))

    def optimal_policy(self, final_state_vals, state):
        costN = self.optimal_cost(final_state_vals, state, 'N')
        costE = self.optimal_cost(final_state_vals, state, 'E')
        costW = self.optimal_cost(final_state_vals, state, 'W')
        min_cost = min(costN, costW, costE)
        print("Minimum cost ", state, ":", min_cost)
        if min_cost == costN:
            optimal_action = 'N'
        elif min_cost == costE:
            optimal_action = 'E'
        else:
            optimal_action = 'W'

        self.optimal_policy_dict[state] = optimal_action

        return self.optimal_policy_dict

    def optimal_cost(self, final_state_vals, state, action):
        state_probs = self.probs[action][state]
        cost = (self.cost_action[action] +
                state_probs[0] * final_state_vals['HHH'] + state_probs[1] * final_state_vals['HHL'] +
                state_probs[2] * final_state_vals['HLH'] + state_probs[3] * final_state_vals['HLL'] +
                state_probs[4] * final_state_vals['LHH'] + state_probs[5] * final_state_vals['LHL'] +
                state_probs[6] * final_state_vals['LLH'] + state_probs[7] * final_state_vals['LLL'])
        return cost


my_class = GetActionProbabilities()

my_class.get_states_value()
my_class.optimal_policy(my_class.final_state_values, 'HHH')
my_class.optimal_policy(my_class.final_state_values, 'HHL')
my_class.optimal_policy(my_class.final_state_values, 'HLH')
my_class.optimal_policy(my_class.final_state_values, 'HLL')
my_class.optimal_policy(my_class.final_state_values, 'LHH')
my_class.optimal_policy(my_class.final_state_values, 'LHL')
my_class.optimal_policy(my_class.final_state_values, 'LLH')
my_class.optimal_policy(my_class.final_state_values, 'LLL')
print(my_class.optimal_policy_dict)
# {'HHH': 'E', 'HHL': 'E', 'HLH': 'W', 'HLL': 'N', 'LHH': 'E', 'LHL': 'E', 'LLH': 'W', 'LLL': 'N'}"""
