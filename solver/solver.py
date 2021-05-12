import math

PAYOUTS = [0, 0, 0, 0, 0, 0,
           10000, 36, 720, 360,
           80, 252, 108, 72,
           54, 180, 72, 180,
           119, 36, 306, 1080,
           144, 1800, 3600]

LINES = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
         (0, 3, 6), (1, 4, 7), (2, 5, 8),
         (0, 4, 8), (2, 4, 6))


class Solver:
    def __init__(self):
        self.input = [0] * 9
        self.hidden_values = []
        self.revealed_values = []
        self.line_values = []

    def feed_input(self, board_state):
        """
        Assigns a given board state to the solver's internal variables.
        :param board_state: A given cactpot board state as a 1D list.
        """
        self.input = board_state.copy()
        self.get_hidden_and_revealed(self.input.copy())

    def get_hidden_and_revealed(self, board_state):
        """
        Finds the hidden and revealed values from a board_state and
        assigns them to the solver's internal variables.
        :param board_state: A given cactpot board state as a 1D list.
        """
        self.hidden_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.revealed_values = []
        for number in range(1, 9):
            if number in board_state:
                self.hidden_values.remove(number)
                self.revealed_values.append(number)
        # print(self.hidden_values)
        # print(self.revealed_values)

    def calculate_expected_line_values(self):
        """
        Calculates the expected (mean) value for each line in the board state.
        :return:
        """

        def calculate_line(selected_line, selected_hidden):
            """
            Calculates the expected value for a given 1D array line.
            :param selected_line:
            :param selected_hidden:
            :return:
            """
            full = True
            for i in range(len(selected_line)):
                if selected_line[i] == 0:
                    full = False

            if full:
                total = sum(selected_line)
                permutation_values.append(total)
            else:
                # Find the first 0.
                selected_line.sort()
                if selected_line[0] == 0:
                    for value in selected_hidden:
                        new_line = selected_line.copy()
                        new_line[0] = value
                        new_hidden = selected_hidden.copy()
                        new_hidden.remove(value)
                        calculate_line(new_line, new_hidden)

        def convert_permutations_to_payouts(permutation_list):
            """
            Calculates the expected payout from a list of permutation line values.
            :param permutation_list: A list of permutation line total values.
            :return: The expected (mean) payout rounded down (floor).
            """
            payout_list = []
            for entry in permutation_list:
                payout_list.append(PAYOUTS[entry])
            payout = 0
            for value in payout_list:
                payout += value
            payout = payout/len(payout_list)
            return math.floor(payout)

        for line in LINES:
            permutation_values = []
            line_list = [self.input[line[0]], self.input[line[1]], self.input[line[2]]]
            calculate_line(line_list, self.hidden_values)
            expected_value = convert_permutations_to_payouts(permutation_values)
            self.line_values.append(expected_value)

        return self.line_values


if __name__ == "__main__":
    matrix = [1, 0, 0,
              0, 0, 0,
              0, 0, 0]
    solver = Solver()
    solver.feed_input(matrix)
    print(solver.calculate_expected_line_values())
