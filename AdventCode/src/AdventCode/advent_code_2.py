import copy


class CustomComputer:

    def run_through_computer(self):
        base_memory = self.turn_opcodes_into_list()
        memory_after_running_program = []
        original_memory = []
        number_we_are_trying_to_find = 19690720
        index_of_value_after_exit = 0

        for first_number in range(0, 99):
            lower_bound = 0
            upper_bound = 98
            middle_bound = (upper_bound-lower_bound) / 2

            while upper_bound > middle_bound >= lower_bound or upper_bound >= middle_bound > lower_bound:
                original_memory = copy.deepcopy(base_memory)
                memory_after_running_program = self.run_opcodes_in_memory(original_memory, first_number, round(middle_bound))
                if memory_after_running_program[index_of_value_after_exit] == number_we_are_trying_to_find:
                    print('printing out the first number and second number: ', first_number, round(middle_bound))
                    break
                elif memory_after_running_program[index_of_value_after_exit] > number_we_are_trying_to_find:
                    upper_bound = middle_bound
                    middle_bound -= (upper_bound-lower_bound) / 2
                elif memory_after_running_program[index_of_value_after_exit] < number_we_are_trying_to_find:
                    lower_bound = middle_bound
                    middle_bound += (upper_bound-lower_bound)+1 / 2
            if memory_after_running_program[index_of_value_after_exit] == number_we_are_trying_to_find:
                break
        return original_memory

    def run_opcodes_in_memory(self, original_memory, first_number, second_number):
        current_instruction = 0
        first_argument_location_index = 1
        second_argument_location_index = 2
        where_to_store_result = 3
        next_instruction = 4
        opcode_for_addition = 1
        opcode_for_program_end = 99
        original_memory[1] = first_number
        original_memory[2] = second_number
        while original_memory[current_instruction] != opcode_for_program_end:
            if original_memory[current_instruction] == opcode_for_addition:
                first_value = original_memory[original_memory[current_instruction+first_argument_location_index]]
                second_value = original_memory[original_memory[current_instruction+second_argument_location_index]]
                storage_location = original_memory[current_instruction+where_to_store_result]
                original_memory[storage_location] = first_value+second_value

                current_instruction += next_instruction
            else:
                first_value = original_memory[original_memory[current_instruction + first_argument_location_index]]
                second_value = original_memory[original_memory[current_instruction + second_argument_location_index]]
                storage_location = original_memory[current_instruction+where_to_store_result]
                original_memory[storage_location] = first_value * second_value
                current_instruction += next_instruction

        return original_memory

    def turn_opcodes_into_list(self):
        all_op_codes_from_file = open('../src/AdventInput/advent2', 'r')
        contents_of_file = all_op_codes_from_file.read()
        original_memory = [opcode.strip() for opcode in contents_of_file.split(',')]
        original_memory = [int(i) for i in original_memory]
        all_op_codes_from_file.close()
        return original_memory
