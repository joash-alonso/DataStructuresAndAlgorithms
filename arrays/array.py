class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        item = self.data[index]
        self._shift_items(index)
        return item

    def _shift_items(self, index):
        for i in range(index, self.length - 1, 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1


if __name__ == "__main__":
    array = Array()
    array.push("hi")
    array.push("hello")
    array.push("there")
    array.push("!")
    print(array.data)
    array.pop()
    array.delete(1)
    print(array.data)
