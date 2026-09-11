class DataStructure:

    data_list = []


    def __init__(self, data, idx):
        self.data = data
        self.idx = idx
        

    def addData(self, data, idx):
        add_data = [data, idx+1]
        self.data_list.append(add_data)
        print(self.data_list)

    def insertData(self, data, idx):
        self.data_list.insert(idx, [data, idx+1])
        if len(self.data_list) <= idx:
            return
        new_i = [i for i in self.data_list[2] if self.data_list[2] >= idx]
        self.data_list[idx] = self.data[data, idx+1]

    def reversData(self):
        revers_data = self.data_list.reverse()
        print(revers_data)

    def deleteData(self):
        self.data_list.pop()
        print(self.data_list)

    def main(self):
        print("1. 공백리스트에 노드3개 삽입하기")
        a = self.addData(3, 0)
        b = self.addData(5, 1)
        c = self.addData(7, 2)      