if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    l_x = [i for i in range(x+1)]
    l_y = [i for i in range(y+1)]
    l_z = [i for i in range(z+1)]
    # print(l_x, l_y, l_z)
    l = [[i,j,k] for i in l_x for j in l_y for k in l_z if i+j+k != n]
    print(l)