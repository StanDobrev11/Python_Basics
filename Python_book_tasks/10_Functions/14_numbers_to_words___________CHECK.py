def letterize(number_as_string):
    number_letter_dict = {"1": "one",
                          "2": "two",
                          "3": "three",
                          "4": "four",
                          "5": "five",
                          "6": "six",
                          "7": "seven",
                          "8": "eight",
                          "9": "nine",
                          "10": "ten",
                          "11": "eleven",
                          "12": "twelve",
                          "13": "thirteen",
                          "14": "fourteen",
                          "15": "fifteen",
                          "16": "sixteen",
                          "17": "seventeen",
                          "18": "eighteen",
                          "19": "nineteen",
                          "20": "twenty",
                          "30": "thirty",
                          "40": "forty",
                          "50": "fifty",
                          "60": "sixty",
                          "70": "seventy",
                          "80": "eighty",
                          "90": "ninety",
                          }
    result = ""
    if number_as_string in number_letter_dict:
        result = number_letter_dict[number_as_string]
    elif len(number_as_string) == 2:  # number in format "ab" different from above, ex. 99
        number = int(number_as_string)
        a = number_letter_dict[str(number - number % 10)]
        b = number_letter_dict[str(number % 10)]
        result = f"{a} {b}"
    elif len(number_as_string) == 3:  # number in format "abc" ex. 109
        keyword_1 = "hundred"
        num_as_list = list(number_as_string)
        if num_as_list[1] == "0" and num_as_list[2] == "0":  # number ex. 100, 200 ...
            a = number_letter_dict[num_as_list[0]]
            result = f"{a}-{keyword_1}"
        elif num_as_list[1] == "0":  # number ex. 106, 209 ...
            a = number_letter_dict[num_as_list[0]]
            c = number_letter_dict[num_as_list[2]]
            result = f"{a}-{keyword_1} and {c}"
        elif num_as_list[2] == "0" or \
                (num_as_list[1] + num_as_list[2]) in number_letter_dict:  # number ex. 110 - 119, 320, 240 ...
            a = number_letter_dict[num_as_list[0]]
            b = number_letter_dict[num_as_list[1] + num_as_list[2]]
            result = f"{a}-{keyword_1} and {b}"
        else:  # number ex. 126, 249 ...
            number = int(number_as_string)
            a = number_letter_dict[num_as_list[0]]
            b = number_letter_dict[str(number % 100 - number % 10)]
            c = number_letter_dict[num_as_list[2]]
            result = f"{a}-{keyword_1} and {b} {c}"
    return result


entries = int(input())
for _ in range(entries):
    num = input()
    if int(num) > 999:
        print("too large")
    elif int(num) < - 999:
        print("too small")
    elif int(num) < 0:
        num = str(abs(int(num)))
        print(f"minus {letterize(num)}")
    elif num == "0" or num == "-0":
        print("zero")
    else:
        print(letterize(num))
