def print_rangoli(n):
    for i in range (n * 2 -1):
        if i < n :
            print_pos = int((4 * n - 3) / 2) - (i * 2)
            # print_count_max = 
            print_count = 0
            print_var = n-i
        else:
            print_pos = 2 + (i-n)*2
            print_count = 0
            print_var = 2 + i-n
        for j in range (4*n - 3):
            if j == print_pos :
                print (chr(print_var+96), end='')
                if print_var < n and print_pos < int((4 * n - 3) / 2):
                    print_var = print_var+1
                else:
                    print_var = print_var - 1
                # print (n-i,end='')
                print_count = print_count+1
                if i < n and print_count >= (2*i + 1):
                    print_pos = -1
                elif i >= n and print_count >= (int((4 * n - 3) / 2) -1 - 2*(i-n)):
                     print_pos = -1
                else:
                    print_pos = print_pos+2
            else:
                print ('-',end='')
        print('')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)