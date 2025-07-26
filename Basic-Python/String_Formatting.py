def print_formatted(number):
    # your code goes here
    bi_len = len(bin(number)[2:])
    
    for i in range(1,number+1):
        print(str(i).rjust(bi_len," "), oct(i)[2:].rjust(bi_len," "), hex(i)[2:].upper().rjust(bi_len," "), bin(i)[2:].rjust(bi_len," "))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)