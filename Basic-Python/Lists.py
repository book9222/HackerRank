if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        in_command = input().split()
        match in_command[0]:
            case "insert" :
                # print("insert") 
                arr.insert(int(in_command[1]), int(in_command[2]))
            case "print" :
                print(arr)
            case "remove" :
                # print("remove ")
                arr.remove(int(in_command[1])) 
            case "append" :
                # print("append ") 
                arr.append(int(in_command[1]))
            case "sort" :
                # print("sort") 
                arr.sort()
            case "pop" :
                # print("pop") 
                arr.pop()
            case "reverse" :
                # print("reverse")
                arr.reverse() 