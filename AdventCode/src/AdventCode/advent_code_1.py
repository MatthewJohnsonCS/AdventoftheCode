from math import floor


class CalculateTheRequiredFuel:

    def read_all_module_weights(self):
        weight_for_each_individual_module = open('../AdventInput/advent1.txt', 'r')
        fuel_required_for_all_modules = 0
        for fuel_required_for_module in weight_for_each_individual_module:
            while self.calculate_fuel_required(fuel_required_for_module) > 0:
                fuel_required_for_module = self.calculate_fuel_required(fuel_required_for_module)
                fuel_required_for_all_modules += fuel_required_for_module
        weight_for_each_individual_module.close()
        print('Here is the required amount of fuel to launch everything: ', fuel_required_for_all_modules)

    def calculate_fuel_required(self, weight):
        number_to_divide_by = 3
        number_to_subtract_by = 2

        fuel_required_for_current_module = int(weight) / number_to_divide_by
        fuel_required_for_current_module = floor(fuel_required_for_current_module)
        fuel_required_for_current_module -= number_to_subtract_by
        return fuel_required_for_current_module
