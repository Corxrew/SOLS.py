# python3

class Query:
    def __init__(self):
        self.pb = [-1]*10000000
    
    def add(self, number, name):
        self.pb[number] = name

    def delete(self, number):
        if self.pb[number] != -1:
            self.pb[number] = -1
    
    def find(self, number):
        if self.pb[number] == -1:
            return "not found"
        return self.pb[number]




def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    for query in queries:
        q = query.split()
        cmd = q[0]
        number = int(q[1])
        if cmd == "add":
            phonebook.add(number, q[2])
        elif cmd == "find":
            print(phonebook.find(number))
        elif cmd == "del":
            phonebook.delete(number)

if __name__ == '__main__':
    phonebook = Query()
    n = int(input())
    queries = [input() for i in range(n)]
    process_queries(queries)

