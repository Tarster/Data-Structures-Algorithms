class Searching(object):
    
    def __init__(self, data_array:list) -> None:
        self.array = data_array
        self.length = len(data_array)
    
    # I have used 2 optimization, not comparing the last element and ending in between if no swap happened.
    def bubble_sort(self):
        for i in range(self.length):
            flag = True
            for j in range(self.length - 1 -i):
                # If we flip the if sign '>' to '<' the list will be sorted in descending order
                # Because now we are pushing the smallest element to the end
                if self.array[j] > self.array [j + 1]:
                    # Simple swap 
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    # Updating flag because swap happened
                    flag = False 
            # Check and abort early
            if flag:
                # print("Already Sorted")
                return self.array    
        return self.array 
    
    def insertion_sort(self):
        # Move an element to the left sorted side and swap it until it doesn't find a smaller element then itself
        for i in range(1, self.length):
            while self.array[i-1] > self.array[i] and i > 0:
                self.array[i], self.array[i - 1] = self.array[i-1], self.array[i]
                i -= 1
        return self.array
    
    def selection_sort(self):
        # Find the smallest element and in the end swap the 2 do it for all the elements
        for i in range(self.length - 1):
            min  = i
            for j in range(i+1, self.length):
                if self.array[min] > self.array[j]:
                    min = j
            self.array[min], self.array[i] = self.array[i], self. array[min]
            # print("iteration:",i, self.array)
        return self.array

print(Searching([]).insertion_sort())