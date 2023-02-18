# country_file = open('countries.txt', 'r')
# print(country_file.readable())
# print(country_file.readline())
# print(country_file.readlines())
# print(country_file.readlines()[3])


# for lines in country_file.readlines():
#     print(lines)


country_file = open('countries.txt', 'w')

country_file.write('This is the new text')
country_file.write('\nThis is the new line')
# country_file.readline()

country_file.close
