if __name__ == '__main__':
    n_list = []
    s_list = []
    s_set = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        n_list.append(name)
        s_list.append(score)
        s_set.add(score)
        
    second_low= sorted(s_set)[1]
    
    ind = [i for i, s in enumerate(s_list) if s == second_low] 
    #The enumerate() function in Python takes an iterable (like a list) and returns pairs of (index, value) for each ite
    n_low = [n_list[i] for i in ind]
    # print(sorted(n_low))
    for n in sorted(n_low):
        print(n)