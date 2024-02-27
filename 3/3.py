def next_palindrome(from_num, radix):
    if radix < 2 or radix > 36:
        return 0, from_num

    while True:
        from_num += 1
        num_in_base = base_convertor(from_num, radix)
        if num_in_base == num_in_base[::-1]:  # Check if it's a palindrome
            return 1, from_num

def base_convertor(num, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num > 0:
        num, remainder = divmod(num, base)
        result = digits[remainder] + result
    return result

def main():
    form = [123, 188, 1441, 95, 45395, 1027, 1000, 18446744073709551614, 18446744073709551615]
    radix = [10, 10, 10, 15, 36, 2, 100, 2, 2]
    next_palindrom_check = [131, 191, 1551, 96, 45431, 1057, 1057, 18446744073709551615, 18446744073709551615]

    for i in range(len(form)):
        if radix[i] < 2 or radix[i] > 36:
            print("Invalid radix")
            continue
        result, next_palindrom = next_palindrome(form[i], radix[i])
        print(result, next_palindrom, next_palindrom_check[i])

if __name__ == "__main__":
    main()