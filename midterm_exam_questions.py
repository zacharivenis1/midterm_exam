#Question 1
a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3
print(a)

#Question 2
print((2+3)*6/2 and 18.0)

#Question 3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#Question 4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

palindrome("9847255590886266818998186626880955527489")
palindrome("6800923757255865070000705685527573290086")
palindrome("6892149109325320763773670235239019412986")
palindrome("1414884937242655719669145562427394884141")

#Question 5
def count_pattern_occurrences(text):
    count = 0
    words = text.split()

    for word in words:
        if len(word) >= 4 and word[0] == 'C' and word[-3:] == "jeb":
            count += 1

    return count

text = "ChelloJeb Cexamplejeb Ctextjeb other Cnotmatching Ctestingjeb"
print(count_pattern_occurrences(text))

#Question 6
mutable_list = [1,2,3]
mutable_list[1] = 3
print(mutable_list) #as we can see the list can be changed

#Strings on the other hand are immutable
immutable_string = "hello"
#immutable_string[2] = "a"
#print(immutable_string)
#attempting to modify the string will result in error seeing as strings cant support assignment types

#Question 7
import random

# Create an empty list to store random numbers
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Goes through the list using the length of it and modifies the values based on conditions
for i in range(len(random_numbers)):  # Using range() to modify the list in place
    if random_numbers[i] > 80:
        # Replace numbers greater than 80 with their negative value
        random_numbers[i] = -random_numbers[i]
    elif random_numbers[i] < 40:
        # Replace numbers lower than 40 with the sum of their digits
        num = random_numbers[i]
        digits_sum = (num // 10) + (num % 10)  # Extract and sum the two digits
        random_numbers[i] = digits_sum

print(random_numbers) #print the final list

#Question 8
def is_url_valid(url):
    # Check if the string starts with http:// or https://
    if url[:7] == "http://" or url[:8] == "https://":
        # Check if there is at least one dot (".") in the url link, such as with "."com or ".net"
        #falls part of valid URL conditions
        if "." in url[7:]: #it checks the rest of the URL by passsing what has already been checked
            return True  #the URL meets the conditions set

    return False  # If any condition dont match then its not a valid URL and the function will return as False


#Some example cases to test the function
print(is_url_valid("http://example.com"))  # will return true
print(is_url_valid("ftp://example.com"))  # will return false as its not a valid URL based on the conditions

#Question 9
def days_since_birth(birthday):
    print("Please ensure you write your birthday in the DD-MM-YYYY Format")
    birth_year = int(birthday[-4:])  #Get last 4 characters, so the year you were born

    #setting the current year for the calculations
    current_year = 2025

    # Calculate whole years passed
    years_passed = current_year - birth_year - 1  # Excluding birth year and current year because
    #the questions asks for whole years that have passed

    # Convert to days basing off of 365 days in a year
    days_passed = years_passed * 365

    print(f"Approximetly {days_passed} days have passed since you were born")

#Example using my birthday
print(days_since_birth("27-08-2004"))

