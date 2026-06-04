def sum_of_numbers(a_list):
    if len(a_list) == 1:
        return a_list[0]
    cur_val = a_list[0]
    return cur_val + sum_of_numbers(a_list[1:]) 

def main():
    my_list = [1,2,3,4,5]
    print(sum_of_numbers(my_list))

if __name__ == "__main__":
    main()