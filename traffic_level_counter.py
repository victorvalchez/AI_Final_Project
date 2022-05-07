import csv


class GetActionProbabilities:
    # Cuanto mas alto el coste mas tarda en normalizarse
    costN, costE, costW = 1, 1, 1
    HHHE, HHLE, HLHE, HLLE, LHHE, LHLE, LLHE, LLLE = [], [], [], [], [], [], [], []
    HHHN, HHLN, HLHN, HLLN, LHHN, LHLN, LLHN, LLLN = [], [], [], [], [], [], [], []
    HHHW, HHLW, HLHW, HLLW, LHHW, LHLW, LLHW, LLLW = [], [], [], [], [], [], [], []
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

        if action == 'E':
            self.HHHE.append(round((cHHHtoHHH / cHHH), 6))
            self.HHHE.append(round((cHHHtoHHL / cHHH), 6))
            self.HHHE.append(round((cHHHtoHLH / cHHH), 6))
            self.HHHE.append(round((cHHHtoHLL / cHHH), 6))
            self.HHHE.append(round((cHHHtoLHH / cHHH), 6))
            self.HHHE.append(round((cHHHtoLHL / cHHH), 6))
            self.HHHE.append(round((cHHHtoLLH / cHHH), 6))
            self.HHHE.append(round((cHHHtoLLL / cHHH), 6))

            self.HHLE.append(round((cHHLtoHHH / cHHL), 6))
            self.HHLE.append(round((cHHLtoHHL / cHHL), 6))
            self.HHLE.append(round((cHHLtoHLH / cHHL), 6))
            self.HHLE.append(round((cHHLtoHLL / cHHL), 6))
            self.HHLE.append(round((cHHLtoLHH / cHHL), 6))
            self.HHLE.append(round((cHHLtoLHL / cHHL), 6))
            self.HHLE.append(round((cHHLtoLLH / cHHL), 6))
            self.HHLE.append(round((cHHLtoLLL / cHHL), 6))

            self.HLHE.append(round((cHLHtoHHH / cHLH), 6))
            self.HLHE.append(round((cHLHtoHHL / cHLH), 6))
            self.HLHE.append(round((cHLHtoHLH / cHLH), 6))
            self.HLHE.append(round((cHLHtoHLL / cHLH), 6))
            self.HLHE.append(round((cHLHtoLHH / cHLH), 6))
            self.HLHE.append(round((cHLHtoLHL / cHLH), 6))
            self.HLHE.append(round((cHLHtoLLH / cHLH), 6))
            self.HLHE.append(round((cHLHtoLLL / cHLH), 6))

            self.HLLE.append(round((cHLLtoHHH / cHLL), 6))
            self.HLLE.append(round((cHLLtoHHL / cHLL), 6))
            self.HLLE.append(round((cHLLtoHLH / cHLL), 6))
            self.HLLE.append(round((cHLLtoHLL / cHLL), 6))
            self.HLLE.append(round((cHLLtoLHH / cHLL), 6))
            self.HLLE.append(round((cHLLtoLHL / cHLL), 6))
            self.HLLE.append(round((cHLLtoLLH / cHLL), 6))
            self.HLLE.append(round((cHLLtoLLL / cHLL), 6))

            self.LHHE.append(round((cLHHtoHHH / cLHH), 6))
            self.LHHE.append(round((cLHHtoHHL / cLHH), 6))
            self.LHHE.append(round((cLHHtoHLH / cLHH), 6))
            self.LHHE.append(round((cLHHtoHLL / cLHH), 6))
            self.LHHE.append(round((cLHHtoLHH / cLHH), 6))
            self.LHHE.append(round((cLHHtoLHL / cLHH), 6))
            self.LHHE.append(round((cLHHtoLLH / cLHH), 6))
            self.LHHE.append(round((cLHHtoLLL / cLHH), 6))

            self.LHLE.append(round((cLHLtoHHH / cLHL), 6))
            self.LHLE.append(round((cLHLtoHHL / cLHL), 6))
            self.LHLE.append(round((cLHLtoHLH / cLHL), 6))
            self.LHLE.append(round((cLHLtoHLL / cLHL), 6))
            self.LHLE.append(round((cLHLtoLHH / cLHL), 6))
            self.LHLE.append(round((cLHLtoLHL / cLHL), 6))
            self.LHLE.append(round((cLHLtoLLH / cLHL), 6))
            self.LHLE.append(round((cLHLtoLLL / cLHL), 6))

            self.LLHE.append(round((cLLHtoHHH / cLLH), 6))
            self.LLHE.append(round((cLLHtoHHL / cLLH), 6))
            self.LLHE.append(round((cLLHtoHLH / cLLH), 6))
            self.LLHE.append(round((cLLHtoHLL / cLLH), 6))
            self.LLHE.append(round((cLLHtoLHH / cLLH), 6))
            self.LLHE.append(round((cLLHtoLHL / cLLH), 6))
            self.LLHE.append(round((cLLHtoLLH / cLLH), 6))
            self.LLHE.append(round((cLLHtoLLL / cLLH), 6))

            self.LLLE.append(round(cLLLtoHHH, 6))
            self.LLLE.append(round(cLLLtoHHL, 6))
            self.LLLE.append(round(cLLLtoHLH, 6))
            self.LLLE.append(round(cLLLtoHLL, 6))
            self.LLLE.append(round(cLLLtoLHH, 6))
            self.LLLE.append(round(cLLLtoLHL, 6))
            self.LLLE.append(round(cLLLtoLLH, 6))
            self.LLLE.append(round(cLLLtoLLL, 6))
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
            print("TO HHH:", self.HHHE[0])
            print("TO HHL:", self.HHHE[1])
            print("TO HLH:", self.HHHE[2])
            print("TO HLL:", self.HHHE[3])
            print("TO LHH:", self.HHHE[4])
            print("TO LHL:", self.HHHE[5])
            print("TO LLH:", self.HHHE[6])
            print("TO LLL:", self.HHHE[7])
            print("-----HHL-----")
            print("TO HHH:", self.HHLE[0])
            print("TO HHL:", self.HHLE[1])
            print("TO HLH:", self.HHLE[2])
            print("TO HLL:", self.HHLE[3])
            print("TO LHH:", self.HHLE[4])
            print("TO LHL:", self.HHLE[5])
            print("TO LLH:", self.HHLE[6])
            print("TO LLL:", self.HHLE[7])
            print("-----HLH-----")
            print("TO HHH:", self.HLHE[0])
            print("TO HHL:", self.HLHE[1])
            print("TO HLH:", self.HLHE[2])
            print("TO HLL:", self.HLHE[3])
            print("TO LHH:", self.HLHE[4])
            print("TO LHL:", self.HLHE[5])
            print("TO LLH:", self.HLHE[6])
            print("TO LLL:", self.HLHE[7])
            print("-----HLL-----")
            print("TO HHH:", self.HLLE[0])
            print("TO HHL:", self.HLLE[1])
            print("TO HLH:", self.HLLE[2])
            print("TO HLL:", self.HLLE[3])
            print("TO LHH:", self.HLLE[4])
            print("TO LHL:", self.HLLE[5])
            print("TO LLH:", self.HLLE[6])
            print("TO LLL:", self.HLLE[7])
            print("-----LHH-----")
            print("TO HHH:", self.LHHE[0])
            print("TO HHL:", self.LHHE[1])
            print("TO HLH:", self.LHHE[2])
            print("TO HLL:", self.LHHE[3])
            print("TO LHH:", self.LHHE[4])
            print("TO LHL:", self.LHHE[5])
            print("TO LLH:", self.LHHE[6])
            print("TO LLL:", self.LHHE[7])
            print("-----LHL-----")
            print("TO HHH:", self.LHLE[0])
            print("TO HHL:", self.LHLE[1])
            print("TO HLH:", self.LHLE[2])
            print("TO HLL:", self.LHLE[3])
            print("TO LHH:", self.LHLE[4])
            print("TO LHL:", self.LHLE[5])
            print("TO LLH:", self.LHLE[6])
            print("TO LLL:", self.LHLE[7])
            print("-----LLH-----")
            print("TO HHH:", self.LLHE[0])
            print("TO HHL:", self.LLHE[1])
            print("TO HLH:", self.LLHE[2])
            print("TO HLL:", self.LLHE[3])
            print("TO LHH:", self.LLHE[4])
            print("TO LHL:", self.LLHE[5])
            print("TO LLH:", self.LLHE[6])
            print("TO LLL:", self.LLHE[7])
            print("-----LLL-----")
            print("TO HHH:", self.LLLE[0])
            print("TO HHL:", self.LLLE[1])
            print("TO HLH:", self.LLLE[2])
            print("TO HLL:", self.LLLE[3])
            print("TO LHH:", self.LLLE[4])
            print("TO LHL:", self.LLLE[5])
            print("TO LLH:", self.LLLE[6])
            print("TO LLL:", self.LLLE[7])

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
            state_probs = self.HHHE
        elif state == 'HHL':
            state_probs = self.HHLE
        elif state == 'HLH':
            state_probs = self.HLHE
        elif state == 'HLL':
            state_probs = self.HLLE
        elif state == 'LHH':
            state_probs = self.LHHE
        elif state == 'LHL':
            state_probs = self.LHLE
        elif state == 'LLH':
            state_probs = self.LLHE
        else:
            state_probs = self.LLLE
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


my_class = GetActionProbabilities()
# my_class.print_probabilities('N')
# my_class.print_probabilities('E')
# my_class.print_probabilities('W')
prev_costs = [[0], [0], [0], [0], [0], [0], [0], [0]]
flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8 = False, False, False, False, False, False, False, False
flag_all = False
final_pos = 0
for a in range(1, 1000):
    prev_costs = my_class.bellman_equations(prev_costs, 'HHH', a)
    prev_costs = my_class.bellman_equations(prev_costs, 'HHL', a)
    prev_costs = my_class.bellman_equations(prev_costs, 'HLH', a)
    prev_costs = my_class.bellman_equations(prev_costs, 'HLL', a)
    prev_costs = my_class.bellman_equations(prev_costs, 'LHH', a)
    prev_costs = my_class.bellman_equations(prev_costs, 'LHL', a)
    prev_costs = my_class.bellman_equations(prev_costs, 'LLH', a)
    prev_costs = my_class.bellman_equations(prev_costs, 'LLL', a)
    """print("\nThis is the", a, "iteration")
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

    if prev_costs[0][a] == prev_costs[0][a - 1]:
        flag1 = True
    if prev_costs[1][a] == prev_costs[1][a - 1]:
        flag2 = True
    if prev_costs[2][a] == prev_costs[2][a - 1]:
        flag3 = True
    if prev_costs[3][a] == prev_costs[3][a - 1]:
        flag4 = True
    if prev_costs[4][a] == prev_costs[4][a - 1]:
        flag5 = True
    if prev_costs[5][a] == prev_costs[5][a - 1]:
        flag6 = True
    if prev_costs[6][a] == prev_costs[6][a - 1]:
        flag7 = True
    if prev_costs[7][a] == prev_costs[7][a - 1]:
        flag8 = True

    if flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7 and flag8:
        flag_all = True

    if flag_all:
        final_pos = a
        break

print("Number of iterations:", final_pos)
for i in range(8):
    if i == 0:
        print("V(HHH): ", prev_costs[i][final_pos])
    elif i == 1:
        print("V(HHL): ", prev_costs[i][final_pos])
    elif i == 2:
        print("V(HLH): ", prev_costs[i][final_pos])
    elif i == 3:
        print("V(HLL): ", prev_costs[i][final_pos])
    elif i == 4:
        print("V(LHH): ", prev_costs[i][final_pos])
    elif i == 5:
        print("V(LHL): ", prev_costs[i][final_pos])
    elif i == 6:
        print("V(LLH): ", prev_costs[i][final_pos])
    else:
        print("V(LLL): ", prev_costs[i][final_pos])
