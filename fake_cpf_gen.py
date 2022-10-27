import random as random

def get_digit(number, n):
    return number // 10**n % 10

def loop_digits(cpf, reps=9):
    i = 2; product = []; sum = 0

    for x in range(reps):
        product.append((x, get_digit(cpf, x) * i ))
        i+=1
        sum += product[x][1] # sum each item's product
                
    if(len(product) == 9):
        # print(sum)
        tenth = generate_first_digit(sum)
        nineth_and_tenth = int('%i%i' % (cpf, tenth))
        loop_digits(nineth_and_tenth, 10)

    elif (len(product) == 10):
        # print(sum)
        eleventh = generate_second_digit(sum)
        # print(eleventh)
        tenth_and_eleventh = int('%i%i' % (cpf, eleventh))
        print("=" * 30, "CPF: ", tenth_and_eleventh, "=" * 30)

def generate_nine_digits():
    nine_numbers = random.sample(range(000000000,999999999),1)
    nine_numbers = int(''.join([ "%d"%x for x in nine_numbers]))   
    loop_digits(nine_numbers)

def generate_first_digit(sum):    
    if (sum % 11 < 2):
        digit_one = 0
    else: 
        digit_one = 11 - (sum % 11)
    return digit_one

def generate_second_digit(sum):
    if (sum % 11 < 2):
        digit_two = 0
    else: 
        digit_two = 11 - (sum % 11)
    return digit_two

def main():
    for x in range(999999999):
        generate_nine_digits()

if __name__ == "__main__":
    main()