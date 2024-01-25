class CircularArray:
    def __init__(self, size) -> None:
        self.size = size
        self.arr = [None] * size
        self.head = 0

    def insert(self, element):
        self.arr[self.head] = element
        self.head = (self.head + 1) % self.size

    def delete(self, element):
        found = False
        for i in range(self.size):
            if self.arr[i] == element:
                found = True
                # Shift elements to the left starting from the deleted element
                for j in range(i, self.size - 1):
                    self.arr[j] = self.arr[(j + 1) % self.size]
                # Set the last element to None to represent an empty slot
                self.arr[self.size - 1] = None
                break

        if not found:
            print(f"Element {element} not found in the array.")

    def display(self):
        print("Circular array:", end=' ')
        for i in range(self.size):
            if self.arr[i] is None:
                print(" ", end=" ")  # Print a blank space for empty slots
            else:
                print(self.arr[i], end=" ")
        print()

if __name__ == "__main__":
    circleArr = CircularArray(5)
    circleArr.insert(1)
    circleArr.insert(2)
    circleArr.display()

    circleArr.delete(1)
    circleArr.display()
