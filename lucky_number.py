#lucky_number_finder
vowel_sounds = ["a","e","ı", "i", "o", "ö", "u", "ü"]
consonant_sounds = ["z", "y", "v", "t", "ş", "s", "r", "p", "n", "r", "m", "l", "k", "h", "j", "ğ", "g", "d", "ç", "c", "b"]
name_surname =input("Write Your Name and Surname:")
birthday = input("write Your Birthday DD.MM.YYYY:")
#counting for vowel and consonant sounds
number_of_vowel = 0
number_of_consonant = 0
gap_number = 0
for letter in name_surname.lower() :
    if letter in vowel_sounds:
        number_of_vowel +=1
    elif letter == " " :
        gap_number +=1
    else:
        number_of_consonant +=1
without_gaps = number_of_consonant-gap_number
# formating birthday date to int number
int_number_list =[] 
for str_number in birthday :
    if str_number.isdigit() :
        int_number_list.append(int(str_number))

finding_3_times  = list(filter(lambda x: x%3 == 0, int_number_list))
number_counting = 0
for find_it in finding_3_times:
    number_counting +=1

lucky_number =(f"Your Lucky Number is :{number_of_vowel}{number_of_consonant}{number_counting} ")
print(lucky_number)
