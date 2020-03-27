class SortingAlgorithms:
    def __init__(self, numbers):
        self.numbers = numbers

    def selection_sort(self):
        new_numbers = self.numbers

        for i in range(len(new_numbers)):
            minimum_index = i

            for j in range(i + 1, len(new_numbers)):
                if new_numbers[j] < new_numbers[minimum_index]:
                    minimum_index = j

            new_numbers[i], new_numbers[minimum_index] = new_numbers[minimum_index], new_numbers[i]

        return new_numbers

    def quick_sort(self, numbers):

        # for the initial case
        if numbers is None:
            numbers = self.numbers

        if len(numbers) < 2:
            return numbers

        pivot = numbers[0]
        less_than_pivot = [number for number in numbers[1:] if number <= pivot]
        greater_than_pivot = [number for number in numbers[1:] if number > pivot]

        return self.quick_sort(less_than_pivot) + [pivot] + self.quick_sort(greater_than_pivot)

    def recursive_insertion_sort(self, numbers, num):

        # for the initial case
        if numbers is None:
            numbers = self.numbers
            num = len(numbers)

        if num <= 1:
            return

        self.recursive_insertion_sort(numbers, num - 1)

        last_element = numbers[num - 1]
        second_to_last = num - 2

        while second_to_last >= 0 and numbers[second_to_last] > last_element:
            numbers[second_to_last + 1] = numbers[second_to_last]
            second_to_last = second_to_last - 1

        numbers[second_to_last + 1] = last_element

        return numbers

    def merge_sort(self):

        # Placeholder
        pass
