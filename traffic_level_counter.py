import csv


class GetActionProbabilities:
    # Cuanto mas alto el coste mas tarda en normalizarse
    costN, costE, costW = 1, 1, 1
    probE = {'HHH': [], 'HHL': [], 'HLH': [], 'HLL': [], 'LHH': [], 'LHL': [], 'LLH': [], 'LLL': []}
    HHHN, HHLN, HLHN, HLLN, LHHN, LHLN, LLHN, LLLN = [], [], [], [], [], [], [], []
    HHHW, HHLW, HLHW, HLLW, LHHW, LHLW, LLHW, LLLW = [], [], [], [], [], [], [], []
    previous_costs = [[0], [0], [0], [0], [0], [0], [0], [0]]
    final_state_values = []
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

        if action == 'E':
            self.probE['HHH'].append(round((cHHHtoHHH / cHHH), 6))
            self.probE['HHH'].append(round((cHHHtoHHL / cHHH), 6))
            self.probE['HHH'].append(round((cHHHtoHLH / cHHH), 6))
            self.probE['HHH'].append(round((cHHHtoHLL / cHHH), 6))
            self.probE['HHH'].append(round((cHHHtoLHH / cHHH), 6))
            self.probE['HHH'].append(round((cHHHtoLHL / cHHH), 6))
            self.probE['HHH'].append(round((cHHHtoLLH / cHHH), 6))
            self.probE['HHH'].append(round((cHHHtoLLL / cHHH), 6))

            self.probE['HHL'].append(round((cHHLtoHHH / cHHL), 6))
            self.probE['HHL'].append(round((cHHLtoHHL / cHHL), 6))
            self.probE['HHL'].append(round((cHHLtoHLH / cHHL), 6))
            self.probE['HHL'].append(round((cHHLtoHLL / cHHL), 6))
            self.probE['HHL'].append(round((cHHLtoLHH / cHHL), 6))
            self.probE['HHL'].append(round((cHHLtoLHL / cHHL), 6))
            self.probE['HHL'].append(round((cHHLtoLLH / cHHL), 6))
            self.probE['HHL'].append(round((cHHLtoLLL / cHHL), 6))

            self.probE['HLH'].append(round((cHLHtoHHH / cHLH), 6))
            self.probE['HLH'].append(round((cHLHtoHHL / cHLH), 6))
            self.probE['HLH'].append(round((cHLHtoHLH / cHLH), 6))
            self.probE['HLH'].append(round((cHLHtoHLL / cHLH), 6))
            self.probE['HLH'].append(round((cHLHtoLHH / cHLH), 6))
            self.probE['HLH'].append(round((cHLHtoLHL / cHLH), 6))
            self.probE['HLH'].append(round((cHLHtoLLH / cHLH), 6))
            self.probE['HLH'].append(round((cHLHtoLLL / cHLH), 6))

            self.probE['HLL'].append(round((cHLLtoHHH / cHLL), 6))
            self.probE['HLL'].append(round((cHLLtoHHL / cHLL), 6))
            self.probE['HLL'].append(round((cHLLtoHLH / cHLL), 6))
            self.probE['HLL'].append(round((cHLLtoHLL / cHLL), 6))
            self.probE['HLL'].append(round((cHLLtoLHH / cHLL), 6))
            self.probE['HLL'].append(round((cHLLtoLHL / cHLL), 6))
            self.probE['HLL'].append(round((cHLLtoLLH / cHLL), 6))
            self.probE['HLL'].append(round((cHLLtoLLL / cHLL), 6))

            self.probE['LHH'].append(round((cLHHtoHHH / cLHH), 6))
            self.probE['LHH'].append(round((cLHHtoHHL / cLHH), 6))
            self.probE['LHH'].append(round((cLHHtoHLH / cLHH), 6))
            self.probE['LHH'].append(round((cLHHtoHLL / cLHH), 6))
            self.probE['LHH'].append(round((cLHHtoLHH / cLHH), 6))
            self.probE['LHH'].append(round((cLHHtoLHL / cLHH), 6))
            self.probE['LHH'].append(round((cLHHtoLLH / cLHH), 6))
            self.probE['LHH'].append(round((cLHHtoLLL / cLHH), 6))

            self.probE['LHL'].append(round((cLHLtoHHH / cLHL), 6))
            self.probE['LHL'].append(round((cLHLtoHHL / cLHL), 6))
            self.probE['LHL'].append(round((cLHLtoHLH / cLHL), 6))
            self.probE['LHL'].append(round((cLHLtoHLL / cLHL), 6))
            self.probE['LHL'].append(round((cLHLtoLHH / cLHL), 6))
            self.probE['LHL'].append(round((cLHLtoLHL / cLHL), 6))
            self.probE['LHL'].append(round((cLHLtoLLH / cLHL), 6))
            self.probE['LHL'].append(round((cLHLtoLLL / cLHL), 6))

            self.probE['LLH'].append(round((cLLHtoHHH / cLLH), 6))
            self.probE['LLH'].append(round((cLLHtoHHL / cLLH), 6))
            self.probE['LLH'].append(round((cLLHtoHLH / cLLH), 6))
            self.probE['LLH'].append(round((cLLHtoHLL / cLLH), 6))
            self.probE['LLH'].append(round((cLLHtoLHH / cLLH), 6))
            self.probE['LLH'].append(round((cLLHtoLHL / cLLH), 6))
            self.probE['LLH'].append(round((cLLHtoLLH / cLLH), 6))
            self.probE['LLH'].append(round((cLLHtoLLL / cLLH), 6))

            self.probE['LLL'].append(round(cLLLtoHHH, 6))
            self.probE['LLL'].append(round(cLLLtoHHL, 6))
            self.probE['LLL'].append(round(cLLLtoHLH, 6))
            self.probE['LLL'].append(round(cLLLtoHLL, 6))
            self.probE['LLL'].append(round(cLLLtoLHH, 6))
            self.probE['LLL'].append(round(cLLLtoLHL, 6))
            self.probE['LLL'].append(round(cLLLtoLLH, 6))
            self.probE['LLL'].append(round(cLLLtoLLL, 6))
        elif action == 'N':
            self.HHHN.append(round((cHHHtoHHH / cHHH), 6))
            self.HHHN.append(round((cHHHtoHHL / cHHH), 6))
            self.HHHN.append(round((cHHHtoHLH / cHHH), 6))
            self.HHHN.append(round((cHHHtoHLL / cHHH), 6))
            self.HHHN.append(round((cHHHtoLHH / cHHH), 6))
            self.HHHN.append(round((cHHHtoLHL / cHHH), 6))
            self.HHHN.append(round((cHHHtoLLH / cHHH), 6))
            self.HHHN.append(round((cHHHtoLLL / cHHH), 6))

            self.HHLN.append(round((cHHLtoHHH / cHHL), 6))
            self.HHLN.append(round((cHHLtoHHL / cHHL), 6))
            self.HHLN.append(round((cHHLtoHLH / cHHL), 6))
            self.HHLN.append(round((cHHLtoHLL / cHHL), 6))
            self.HHLN.append(round((cHHLtoLHH / cHHL), 6))
            self.HHLN.append(round((cHHLtoLHL / cHHL), 6))
            self.HHLN.append(round((cHHLtoLLH / cHHL), 6))
            self.HHLN.append(round((cHHLtoLLL / cHHL), 6))

            self.HLHN.append(round((cHLHtoHHH / cHLH), 6))
            self.HLHN.append(round((cHLHtoHHL / cHLH), 6))
            self.HLHN.append(round((cHLHtoHLH / cHLH), 6))
            self.HLHN.append(round((cHLHtoHLL / cHLH), 6))
            self.HLHN.append(round((cHLHtoLHH / cHLH), 6))
            self.HLHN.append(round((cHLHtoLHL / cHLH), 6))
            self.HLHN.append(round((cHLHtoLLH / cHLH), 6))
            self.HLHN.append(round((cHLHtoLLL / cHLH), 6))

            self.HLLN.append(round((cHLLtoHHH / cHLL), 6))
            self.HLLN.append(round((cHLLtoHHL / cHLL), 6))
            self.HLLN.append(round((cHLLtoHLH / cHLL), 6))
            self.HLLN.append(round((cHLLtoHLL / cHLL), 6))
            self.HLLN.append(round((cHLLtoLHH / cHLL), 6))
            self.HLLN.append(round((cHLLtoLHL / cHLL), 6))
            self.HLLN.append(round((cHLLtoLLH / cHLL), 6))
            self.HLLN.append(round((cHLLtoLLL / cHLL), 6))

            self.LHHN.append(round((cLHHtoHHH / cLHH), 6))
            self.LHHN.append(round((cLHHtoHHL / cLHH), 6))
            self.LHHN.append(round((cLHHtoHLH / cLHH), 6))
            self.LHHN.append(round((cLHHtoHLL / cLHH), 6))
            self.LHHN.append(round((cLHHtoLHH / cLHH), 6))
            self.LHHN.append(round((cLHHtoLHL / cLHH), 6))
            self.LHHN.append(round((cLHHtoLLH / cLHH), 6))
            self.LHHN.append(round((cLHHtoLLL / cLHH), 6))

            self.LHLN.append(round((cLHLtoHHH / cLHL), 6))
            self.LHLN.append(round((cLHLtoHHL / cLHL), 6))
            self.LHLN.append(round((cLHLtoHLH / cLHL), 6))
            self.LHLN.append(round((cLHLtoHLL / cLHL), 6))
            self.LHLN.append(round((cLHLtoLHH / cLHL), 6))
            self.LHLN.append(round((cLHLtoLHL / cLHL), 6))
            self.LHLN.append(round((cLHLtoLLH / cLHL), 6))
            self.LHLN.append(round((cLHLtoLLL / cLHL), 6))

            self.LLHN.append(round((cLLHtoHHH / cLLH), 6))
            self.LLHN.append(round((cLLHtoHHL / cLLH), 6))
            self.LLHN.append(round((cLLHtoHLH / cLLH), 6))
            self.LLHN.append(round((cLLHtoHLL / cLLH), 6))
            self.LLHN.append(round((cLLHtoLHH / cLLH), 6))
            self.LLHN.append(round((cLLHtoLHL / cLLH), 6))
            self.LLHN.append(round((cLLHtoLLH / cLLH), 6))
            self.LLHN.append(round((cLLHtoLLL / cLLH), 6))

            self.LLLN.append(round(cLLLtoHHH, 6))
            self.LLLN.append(round(cLLLtoHHL, 6))
            self.LLLN.append(round(cLLLtoHLH, 6))
            self.LLLN.append(round(cLLLtoHLL, 6))
            self.LLLN.append(round(cLLLtoLHH, 6))
            self.LLLN.append(round(cLLLtoLHL, 6))
            self.LLLN.append(round(cLLLtoLLH, 6))
            self.LLLN.append(round(cLLLtoLLL, 6))
        else:
            self.HHHW.append(round((cHHHtoHHH / cHHH), 6))
            self.HHHW.append(round((cHHHtoHHL / cHHH), 6))
            self.HHHW.append(round((cHHHtoHLH / cHHH), 6))
            self.HHHW.append(round((cHHHtoHLL / cHHH), 6))
            self.HHHW.append(round((cHHHtoLHH / cHHH), 6))
            self.HHHW.append(round((cHHHtoLHL / cHHH), 6))
            self.HHHW.append(round((cHHHtoLLH / cHHH), 6))
            self.HHHW.append(round((cHHHtoLLL / cHHH), 6))

            self.HHLW.append(round((cHHLtoHHH / cHHL), 6))
            self.HHLW.append(round((cHHLtoHHL / cHHL), 6))
            self.HHLW.append(round((cHHLtoHLH / cHHL), 6))
            self.HHLW.append(round((cHHLtoHLL / cHHL), 6))
            self.HHLW.append(round((cHHLtoLHH / cHHL), 6))
            self.HHLW.append(round((cHHLtoLHL / cHHL), 6))
            self.HHLW.append(round((cHHLtoLLH / cHHL), 6))
            self.HHLW.append(round((cHHLtoLLL / cHHL), 6))

            self.HLHW.append(round((cHLHtoHHH / cHLH), 6))
            self.HLHW.append(round((cHLHtoHHL / cHLH), 6))
            self.HLHW.append(round((cHLHtoHLH / cHLH), 6))
            self.HLHW.append(round((cHLHtoHLL / cHLH), 6))
            self.HLHW.append(round((cHLHtoLHH / cHLH), 6))
            self.HLHW.append(round((cHLHtoLHL / cHLH), 6))
            self.HLHW.append(round((cHLHtoLLH / cHLH), 6))
            self.HLHW.append(round((cHLHtoLLL / cHLH), 6))

            self.HLLW.append(round((cHLLtoHHH / cHLL), 6))
            self.HLLW.append(round((cHLLtoHHL / cHLL), 6))
            self.HLLW.append(round((cHLLtoHLH / cHLL), 6))
            self.HLLW.append(round((cHLLtoHLL / cHLL), 6))
            self.HLLW.append(round((cHLLtoLHH / cHLL), 6))
            self.HLLW.append(round((cHLLtoLHL / cHLL), 6))
            self.HLLW.append(round((cHLLtoLLH / cHLL), 6))
            self.HLLW.append(round((cHLLtoLLL / cHLL), 6))

            self.LHHW.append(round((cLHHtoHHH / cLHH), 6))
            self.LHHW.append(round((cLHHtoHHL / cLHH), 6))
            self.LHHW.append(round((cLHHtoHLH / cLHH), 6))
            self.LHHW.append(round((cLHHtoHLL / cLHH), 6))
            self.LHHW.append(round((cLHHtoLHH / cLHH), 6))
            self.LHHW.append(round((cLHHtoLHL / cLHH), 6))
            self.LHHW.append(round((cLHHtoLLH / cLHH), 6))
            self.LHHW.append(round((cLHHtoLLL / cLHH), 6))

            self.LHLW.append(round((cLHLtoHHH / cLHL), 6))
            self.LHLW.append(round((cLHLtoHHL / cLHL), 6))
            self.LHLW.append(round((cLHLtoHLH / cLHL), 6))
            self.LHLW.append(round((cLHLtoHLL / cLHL), 6))
            self.LHLW.append(round((cLHLtoLHH / cLHL), 6))
            self.LHLW.append(round((cLHLtoLHL / cLHL), 6))
            self.LHLW.append(round((cLHLtoLLH / cLHL), 6))
            self.LHLW.append(round((cLHLtoLLL / cLHL), 6))

            self.LLHW.append(round((cLLHtoHHH / cLLH), 6))
            self.LLHW.append(round((cLLHtoHHL / cLLH), 6))
            self.LLHW.append(round((cLLHtoHLH / cLLH), 6))
            self.LLHW.append(round((cLLHtoHLL / cLLH), 6))
            self.LLHW.append(round((cLLHtoLHH / cLLH), 6))
            self.LLHW.append(round((cLLHtoLHL / cLLH), 6))
            self.LLHW.append(round((cLLHtoLLH / cLLH), 6))
            self.LLHW.append(round((cLLHtoLLL / cLLH), 6))

            self.LLLW.append(round(cLLLtoHHH, 6))
            self.LLLW.append(round(cLLLtoHHL, 6))
            self.LLLW.append(round(cLLLtoHLH, 6))
            self.LLLW.append(round(cLLLtoHLL, 6))
            self.LLLW.append(round(cLLLtoLHH, 6))
            self.LLLW.append(round(cLLLtoLHL, 6))
            self.LLLW.append(round(cLLLtoLLH, 6))
            self.LLLW.append(round(cLLLtoLLL, 6))

    def print_probabilities(self, action: str):
        if action == 'E':
            print("\nAction E probabilities:")
            self.get_action('E')
            print("-----HHH-----")
            print("TO HHH:", self.probE['HHH'][0])
            print("TO HHL:", self.probE['HHH'][1])
            print("TO HLH:", self.probE['HHH'][2])
            print("TO HLL:", self.probE['HHH'][3])
            print("TO LHH:", self.probE['HHH'][4])
            print("TO LHL:", self.probE['HHH'][5])
            print("TO LLH:", self.probE['HHH'][6])
            print("TO LLL:", self.probE['HHH'][7])
            print("-----HHL-----")
            print("TO HHH:", self.probE['HHL'][0])
            print("TO HHL:", self.probE['HHL'][1])
            print("TO HLH:", self.probE['HHL'][2])
            print("TO HLL:", self.probE['HHL'][3])
            print("TO LHH:", self.probE['HHL'][4])
            print("TO LHL:", self.probE['HHL'][5])
            print("TO LLH:", self.probE['HHL'][6])
            print("TO LLL:", self.probE['HHL'][7])
            print("-----HLH-----")
            print("TO HHH:", self.probE['HLH'][0])
            print("TO HHL:", self.probE['HLH'][1])
            print("TO HLH:", self.probE['HLH'][2])
            print("TO HLL:", self.probE['HLH'][3])
            print("TO LHH:", self.probE['HLH'][4])
            print("TO LHL:", self.probE['HLH'][5])
            print("TO LLH:", self.probE['HLH'][6])
            print("TO LLL:", self.probE['HLH'][7])
            print("-----HLL-----")
            print("TO HHH:", self.probE['HLL'][0])
            print("TO HHL:", self.probE['HLL'][1])
            print("TO HLH:", self.probE['HLL'][2])
            print("TO HLL:", self.probE['HLL'][3])
            print("TO LHH:", self.probE['HLL'][4])
            print("TO LHL:", self.probE['HLL'][5])
            print("TO LLH:", self.probE['HLL'][6])
            print("TO LLL:", self.probE['HLL'][7])
            print("-----LHH-----")
            print("TO HHH:", self.probE['LHH'][0])
            print("TO HHL:", self.probE['LHH'][1])
            print("TO HLH:", self.probE['LHH'][2])
            print("TO HLL:", self.probE['LHH'][3])
            print("TO LHH:", self.probE['LHH'][4])
            print("TO LHL:", self.probE['LHH'][5])
            print("TO LLH:", self.probE['LHH'][6])
            print("TO LLL:", self.probE['LHH'][7])
            print("-----LHL-----")
            print("TO HHH:", self.probE['LHL'][0])
            print("TO HHL:", self.probE['LHL'][1])
            print("TO HLH:", self.probE['LHL'][2])
            print("TO HLL:", self.probE['LHL'][3])
            print("TO LHH:", self.probE['LHL'][4])
            print("TO LHL:", self.probE['LHL'][5])
            print("TO LLH:", self.probE['LHL'][6])
            print("TO LLL:", self.probE['LHL'][7])
            print("-----LLH-----")
            print("TO HHH:", self.probE['LLH'][0])
            print("TO HHL:", self.probE['LLH'][1])
            print("TO HLH:", self.probE['LLH'][2])
            print("TO HLL:", self.probE['LLH'][3])
            print("TO LHH:", self.probE['LLH'][4])
            print("TO LHL:", self.probE['LLH'][5])
            print("TO LLH:", self.probE['LLH'][6])
            print("TO LLL:", self.probE['LLH'][7])
            print("-----LLL-----")
            print("TO HHH:", self.probE['LLL'][0])
            print("TO HHL:", self.probE['LLL'][1])
            print("TO HLH:", self.probE['LLL'][2])
            print("TO HLL:", self.probE['LLL'][3])
            print("TO LHH:", self.probE['LLL'][4])
            print("TO LHL:", self.probE['LLL'][5])
            print("TO LLH:", self.probE['LLL'][6])
            print("TO LLL:", self.probE['LLL'][7])

        elif action == 'N':
            print("\nAction N probabilities:")
            self.get_action('N')
            print("-----HHH-----")
            print("TO HHH:", self.HHHN[0])
            print("TO HHL:", self.HHHN[1])
            print("TO HLH:", self.HHHN[2])
            print("TO HLL:", self.HHHN[3])
            print("TO LHH:", self.HHHN[4])
            print("TO LHL:", self.HHHN[5])
            print("TO LLH:", self.HHHN[6])
            print("TO LLL:", self.HHHN[7])
            print("-----HHL-----")
            print("TO HHH:", self.HHLN[0])
            print("TO HHL:", self.HHLN[1])
            print("TO HLH:", self.HHLN[2])
            print("TO HLL:", self.HHLN[3])
            print("TO LHH:", self.HHLN[4])
            print("TO LHL:", self.HHLN[5])
            print("TO LLH:", self.HHLN[6])
            print("TO LLL:", self.HHLN[7])
            print("-----HLH-----")
            print("TO HHH:", self.HLHN[0])
            print("TO HHL:", self.HLHN[1])
            print("TO HLH:", self.HLHN[2])
            print("TO HLL:", self.HLHN[3])
            print("TO LHH:", self.HLHN[4])
            print("TO LHL:", self.HLHN[5])
            print("TO LLH:", self.HLHN[6])
            print("TO LLL:", self.HLHN[7])
            print("-----HLL-----")
            print("TO HHH:", self.HLLN[0])
            print("TO HHL:", self.HLLN[1])
            print("TO HLH:", self.HLLN[2])
            print("TO HLL:", self.HLLN[3])
            print("TO LHH:", self.HLLN[4])
            print("TO LHL:", self.HLLN[5])
            print("TO LLH:", self.HLLN[6])
            print("TO LLL:", self.HLLN[7])
            print("-----LHH-----")
            print("TO HHH:", self.LHHN[0])
            print("TO HHL:", self.LHHN[1])
            print("TO HLH:", self.LHHN[2])
            print("TO HLL:", self.LHHN[3])
            print("TO LHH:", self.LHHN[4])
            print("TO LHL:", self.LHHN[5])
            print("TO LLH:", self.LHHN[6])
            print("TO LLL:", self.LHHN[7])
            print("-----LHL-----")
            print("TO HHH:", self.LHLN[0])
            print("TO HHL:", self.LHLN[1])
            print("TO HLH:", self.LHLN[2])
            print("TO HLL:", self.LHLN[3])
            print("TO LHH:", self.LHLN[4])
            print("TO LHL:", self.LHLN[5])
            print("TO LLH:", self.LHLN[6])
            print("TO LLL:", self.LHLN[7])
            print("-----LLH-----")
            print("TO HHH:", self.LLHN[0])
            print("TO HHL:", self.LLHN[1])
            print("TO HLH:", self.LLHN[2])
            print("TO HLL:", self.LLHN[3])
            print("TO LHH:", self.LLHN[4])
            print("TO LHL:", self.LLHN[5])
            print("TO LLH:", self.LLHN[6])
            print("TO LLL:", self.LLHN[7])
            print("-----LLL-----")
            print("TO HHH:", self.LLLN[0])
            print("TO HHL:", self.LLLN[1])
            print("TO HLH:", self.LLLN[2])
            print("TO HLL:", self.LLLN[3])
            print("TO LHH:", self.LLLN[4])
            print("TO LHL:", self.LLLN[5])
            print("TO LLH:", self.LLLN[6])
            print("TO LLL:", self.LLLN[7])

        else:
            print("\nAction W probabilities:")
            self.get_action('W')
            print("-----HHH-----")
            print("TO HHH:", self.HHHW[0])
            print("TO HHL:", self.HHHW[1])
            print("TO HLH:", self.HHHW[2])
            print("TO HLL:", self.HHHW[3])
            print("TO LHH:", self.HHHW[4])
            print("TO LHL:", self.HHHW[5])
            print("TO LLH:", self.HHHW[6])
            print("TO LLL:", self.HHHW[7])
            print("-----HHL-----")
            print("TO HHH:", self.HHLW[0])
            print("TO HHL:", self.HHLW[1])
            print("TO HLH:", self.HHLW[2])
            print("TO HLL:", self.HHLW[3])
            print("TO LHH:", self.HHLW[4])
            print("TO LHL:", self.HHLW[5])
            print("TO LLH:", self.HHLW[6])
            print("TO LLL:", self.HHLW[7])
            print("-----HLH-----")
            print("TO HHH:", self.HLHW[0])
            print("TO HHL:", self.HLHW[1])
            print("TO HLH:", self.HLHW[2])
            print("TO HLL:", self.HLHW[3])
            print("TO LHH:", self.HLHW[4])
            print("TO LHL:", self.HLHW[5])
            print("TO LLH:", self.HLHW[6])
            print("TO LLL:", self.HLHW[7])
            print("-----HLL-----")
            print("TO HHH:", self.HLLW[0])
            print("TO HHL:", self.HLLW[1])
            print("TO HLH:", self.HLLW[2])
            print("TO HLL:", self.HLLW[3])
            print("TO LHH:", self.HLLW[4])
            print("TO LHL:", self.HLLW[5])
            print("TO LLH:", self.HLLW[6])
            print("TO LLL:", self.HLLW[7])
            print("-----LHH-----")
            print("TO HHH:", self.LHHW[0])
            print("TO HHL:", self.LHHW[1])
            print("TO HLH:", self.LHHW[2])
            print("TO HLL:", self.LHHW[3])
            print("TO LHH:", self.LHHW[4])
            print("TO LHL:", self.LHHW[5])
            print("TO LLH:", self.LHHW[6])
            print("TO LLL:", self.LHHW[7])
            print("-----LHL-----")
            print("TO HHH:", self.LHLW[0])
            print("TO HHL:", self.LHLW[1])
            print("TO HLH:", self.LHLW[2])
            print("TO HLL:", self.LHLW[3])
            print("TO LHH:", self.LHLW[4])
            print("TO LHL:", self.LHLW[5])
            print("TO LLH:", self.LHLW[6])
            print("TO LLL:", self.LHLW[7])
            print("-----LLH-----")
            print("TO HHH:", self.LLHW[0])
            print("TO HHL:", self.LLHW[1])
            print("TO HLH:", self.LLHW[2])
            print("TO HLL:", self.LLHW[3])
            print("TO LHH:", self.LLHW[4])
            print("TO LHL:", self.LLHW[5])
            print("TO LLH:", self.LLHW[6])
            print("TO LLL:", self.LLHW[7])
            print("-----LLL-----")
            print("TO HHH:", self.LLLW[0])
            print("TO HHL:", self.LLLW[1])
            print("TO HLH:", self.LLLW[2])
            print("TO HLL:", self.LLLW[3])
            print("TO LHH:", self.LLLW[4])
            print("TO LHL:", self.LLLW[5])
            print("TO LLH:", self.LLLW[6])
            print("TO LLL:", self.LLLW[7])

    def bellman_equations(self, previous_costs_list: list, state: str, iteration: int) -> list:
        costN = self.bellman_costN(iteration, previous_costs_list, state)
        costE = self.bellman_costE(iteration, previous_costs_list, state)
        costW = self.bellman_costW(iteration, previous_costs_list, state)
        min_cost = round(min(costN, costW, costE), 6)
        if state == 'HHH':
            previous_costs_list[0].append(min_cost)
        elif state == 'HHL':
            previous_costs_list[1].append(min_cost)
        elif state == 'HLH':
            previous_costs_list[2].append(min_cost)
        elif state == 'HLL':
            previous_costs_list[3].append(min_cost)
        elif state == 'LHH':
            previous_costs_list[4].append(min_cost)
        elif state == 'LHL':
            previous_costs_list[5].append(min_cost)
        elif state == 'LLH':
            previous_costs_list[6].append(min_cost)
        else:
            previous_costs_list[7].append(min_cost)
        return previous_costs_list

    def bellman_costN(self, iteration, prev_costs, state):
        self.get_action('N')
        if state == 'HHH':
            state_probs = self.HHHN
        elif state == 'HHL':
            state_probs = self.HHLN
        elif state == 'HLH':
            state_probs = self.HLHN
        elif state == 'HLL':
            state_probs = self.HLLN
        elif state == 'LHH':
            state_probs = self.LHHN
        elif state == 'LHL':
            state_probs = self.LHLN
        elif state == 'LLH':
            state_probs = self.LLHN
        else:
            state_probs = self.LLLN
        costN = (self.costN +
                 state_probs[0] * prev_costs[0][iteration - 1] + state_probs[1] * prev_costs[1][iteration - 1] +
                 state_probs[2] * prev_costs[2][iteration - 1] + state_probs[3] * prev_costs[3][iteration - 1] +
                 state_probs[4] * prev_costs[4][iteration - 1] + state_probs[5] * prev_costs[5][iteration - 1] +
                 state_probs[6] * prev_costs[6][iteration - 1] + state_probs[7] * prev_costs[7][iteration - 1])
        return costN

    def bellman_costE(self, iteration, prev_costs, state):
        self.get_action('E')
        if state == 'HHH':
            state_probs = self.probE['HHH']
        elif state == 'HHL':
            state_probs = self.probE['HHL']
        elif state == 'HLH':
            state_probs = self.probE['HLH']
        elif state == 'HLL':
            state_probs = self.probE['HLL']
        elif state == 'LHH':
            state_probs = self.probE['LHH']
        elif state == 'LHL':
            state_probs = self.probE['LHL']
        elif state == 'LLH':
            state_probs = self.probE['LLH']
        else:
            state_probs = self.probE['LLL']
        costE = (self.costE +
                 state_probs[0] * prev_costs[0][iteration - 1] + state_probs[1] * prev_costs[1][iteration - 1] +
                 state_probs[2] * prev_costs[2][iteration - 1] + state_probs[3] * prev_costs[3][iteration - 1] +
                 state_probs[4] * prev_costs[4][iteration - 1] + state_probs[5] * prev_costs[5][iteration - 1] +
                 state_probs[6] * prev_costs[6][iteration - 1] + state_probs[7] * prev_costs[7][iteration - 1])
        return costE

    def bellman_costW(self, iteration, prev_costs, state):
        self.get_action('W')
        if state == 'HHH':
            state_probs = self.HHHW
        elif state == 'HHL':
            state_probs = self.HHLW
        elif state == 'HLH':
            state_probs = self.HLHW
        elif state == 'HLL':
            state_probs = self.HLLW
        elif state == 'LHH':
            state_probs = self.LHHW
        elif state == 'LHL':
            state_probs = self.LHLW
        elif state == 'LLH':
            state_probs = self.LLHW
        else:
            state_probs = self.LLLW
        costW = (self.costW +
                 state_probs[0] * prev_costs[0][iteration - 1] + state_probs[1] * prev_costs[1][iteration - 1] +
                 state_probs[2] * prev_costs[2][iteration - 1] + state_probs[3] * prev_costs[3][iteration - 1] +
                 state_probs[4] * prev_costs[4][iteration - 1] + state_probs[5] * prev_costs[5][iteration - 1] +
                 state_probs[6] * prev_costs[6][iteration - 1] + state_probs[7] * prev_costs[7][iteration - 1])
        return costW

    def get_states_value(self):
        flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8 = False, False, False, False, False, False, False, False
        flag_all = False
        final_pos = 0

        for a in range(1, 1000):
            self.previous_costs = self.bellman_equations(self.previous_costs, 'HHH', a)
            self.previous_costs = self.bellman_equations(self.previous_costs, 'HHL', a)
            self.previous_costs = self.bellman_equations(self.previous_costs, 'HLH', a)
            self.previous_costs = self.bellman_equations(self.previous_costs, 'HLL', a)
            self.previous_costs = self.bellman_equations(self.previous_costs, 'LHH', a)
            self.previous_costs = self.bellman_equations(self.previous_costs, 'LHL', a)
            self.previous_costs = self.bellman_equations(self.previous_costs, 'LLH', a)
            self.previous_costs[7].append(0)
            print("\nThis is the", a, "iteration")
            for i in range(8):
                if i == 0:
                    print("V(HHH): ", self.previous_costs[i])
                elif i == 1:
                    print("V(HHL): ", self.previous_costs[i])
                elif i == 2:
                    print("V(HLH): ", self.previous_costs[i])
                elif i == 3:
                    print("V(HLL): ", self.previous_costs[i])
                elif i == 4:
                    print("V(LHH): ", self.previous_costs[i])
                elif i == 5:
                    print("V(LHL): ", self.previous_costs[i])
                elif i == 6:
                    print("V(LLH): ", self.previous_costs[i])
                else:
                    print("V(LLL): ", self.previous_costs[i])

            if self.previous_costs[0][a] == self.previous_costs[0][a - 1]:
                flag1 = True
            if self.previous_costs[1][a] == self.previous_costs[1][a - 1]:
                flag2 = True
            if self.previous_costs[2][a] == self.previous_costs[2][a - 1]:
                flag3 = True
            if self.previous_costs[3][a] == self.previous_costs[3][a - 1]:
                flag4 = True
            if self.previous_costs[4][a] == self.previous_costs[4][a - 1]:
                flag5 = True
            if self.previous_costs[5][a] == self.previous_costs[5][a - 1]:
                flag6 = True
            if self.previous_costs[6][a] == self.previous_costs[6][a - 1]:
                flag7 = True
            if self.previous_costs[7][a] == self.previous_costs[7][a - 1]:
                flag8 = True

            if flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7 and flag8:
                flag_all = True

            if flag_all:
                final_pos = a
                break

        print("Number of iterations:", final_pos)
        for i in range(8):
            if i == 0:
                self.final_state_values.append(self.previous_costs[i][final_pos])
                print("V(HHH): ", self.previous_costs[i][final_pos])
            elif i == 1:
                self.final_state_values.append(self.previous_costs[i][final_pos])
                print("V(HHL): ", self.previous_costs[i][final_pos])
            elif i == 2:
                self.final_state_values.append(self.previous_costs[i][final_pos])
                print("V(HLH): ", self.previous_costs[i][final_pos])
            elif i == 3:
                self.final_state_values.append(self.previous_costs[i][final_pos])
                print("V(HLL): ", self.previous_costs[i][final_pos])
            elif i == 4:
                self.final_state_values.append(self.previous_costs[i][final_pos])
                print("V(LHH): ", self.previous_costs[i][final_pos])
            elif i == 5:
                self.final_state_values.append(self.previous_costs[i][final_pos])
                print("V(LHL): ", self.previous_costs[i][final_pos])
            elif i == 6:
                self.final_state_values.append(self.previous_costs[i][final_pos])
                print("V(LLH): ", self.previous_costs[i][final_pos])
            else:
                self.final_state_values.append(self.previous_costs[i][final_pos])
                print("V(LLL): ", self.previous_costs[i][final_pos])

    def optimal_policy(self, final_state_vals, state):
        costN = self.optimalN(final_state_vals, state)
        costE = self.optimalE(final_state_vals, state)
        costW = self.optimalW(final_state_vals, state)
        print(costN, costE, costW)
        min_cost = min(costN, costW, costE)
        print(min_cost)
        optimal_action = ''
        if min_cost == costN:
            optimal_action = 'N'
        elif min_cost == costE:
            optimal_action = 'E'
        else:
            optimal_action = 'W'

        if state == 'HHH':
            self.optimal_policy_dict['HHH'] = optimal_action
        elif state == 'HHL':
            self.optimal_policy_dict['HHL'] = optimal_action
        elif state == 'HLH':
            self.optimal_policy_dict['HLH'] = optimal_action
        elif state == 'HLL':
            self.optimal_policy_dict['HLL'] = optimal_action
        elif state == 'LHH':
            self.optimal_policy_dict['LHH'] = optimal_action
        elif state == 'LHL':
            self.optimal_policy_dict['LHL'] = optimal_action
        elif state == 'LLH':
            self.optimal_policy_dict['LLH'] = optimal_action
        else:
            self.optimal_policy_dict['LLL'] = optimal_action
        return self.optimal_policy_dict

    def optimalN(self, final_state_vals, state):
        if state == 'HHH':
            state_probs = self.HHHN
        elif state == 'HHL':
            state_probs = self.HHLN
        elif state == 'HLH':
            state_probs = self.HLHN
        elif state == 'HLL':
            state_probs = self.HLLN
        elif state == 'LHH':
            state_probs = self.LHHN
        elif state == 'LHL':
            state_probs = self.LHLN
        elif state == 'LLH':
            state_probs = self.LLHN
        else:
            state_probs = self.LLLN
        costN = (self.costN +
                 state_probs[0] * final_state_vals[0] + state_probs[1] * final_state_vals[1] +
                 state_probs[2] * final_state_vals[2] + state_probs[3] * final_state_vals[3] +
                 state_probs[4] * final_state_vals[4] + state_probs[5] * final_state_vals[5] +
                 state_probs[6] * final_state_vals[6] + state_probs[7] * final_state_vals[7])
        return costN

    def optimalE(self, final_state_vals, state):
        if state == 'HHH':
            state_probs = self.probE['HHH']
        elif state == 'HHL':
            state_probs = self.probE['HHL']
        elif state == 'HLH':
            state_probs = self.probE['HLH']
        elif state == 'HLL':
            state_probs = self.probE['HLL']
        elif state == 'LHH':
            state_probs = self.probE['LHH']
        elif state == 'LHL':
            state_probs = self.probE['LHL']
        elif state == 'LLH':
            state_probs = self.probE['LLH']
        else:
            state_probs = self.probE['LLL']
        costE = (self.costE +
                 state_probs[0] * final_state_vals[0] + state_probs[1] * final_state_vals[1] +
                 state_probs[2] * final_state_vals[2] + state_probs[3] * final_state_vals[3] +
                 state_probs[4] * final_state_vals[4] + state_probs[5] * final_state_vals[5] +
                 state_probs[6] * final_state_vals[6] + state_probs[7] * final_state_vals[7])
        return costE

    def optimalW(self, final_state_vals, state):
        if state == 'HHH':
            state_probs = self.HHHW
        elif state == 'HHL':
            state_probs = self.HHLW
        elif state == 'HLH':
            state_probs = self.HLHW
        elif state == 'HLL':
            state_probs = self.HLLW
        elif state == 'LHH':
            state_probs = self.LHHW
        elif state == 'LHL':
            state_probs = self.LHLW
        elif state == 'LLH':
            state_probs = self.LLHW
        else:
            state_probs = self.LLLW
        costW = (self.costW +
                 state_probs[0] * final_state_vals[0] + state_probs[1] * final_state_vals[1] +
                 state_probs[2] * final_state_vals[2] + state_probs[3] * final_state_vals[3] +
                 state_probs[4] * final_state_vals[4] + state_probs[5] * final_state_vals[5] +
                 state_probs[6] * final_state_vals[6] + state_probs[7] * final_state_vals[7])
        return costW


my_class = GetActionProbabilities()
my_class.print_probabilities('E')
print(my_class.probE)
"""my_class.get_states_value()
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
