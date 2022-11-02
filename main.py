# # import datetime
# #
# # prev_time = "2022-09-21 12:48:12.274862"
# # converted_prev_time = datetime.datetime.strptime(prev_time, '%Y-%m-%d %H:%M:%S.%f')
# # print(converted_prev_time)
# # print(type(converted_prev_time))
# #
# # time_now = datetime.datetime.now()
# # print(time_now)
# # print(type(time_now))
# #
# # diff = time_now - converted_prev_time
# # print("Diff is", diff.total_seconds())
#
# regex = "^\+254\d{9}"
# import re
# # if re.search(regex, "+254712345678"):
# #     print("Ok")
# # else:
# #     print("Not ok")
# #
# # def solve(s):
# #    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
# #    if re.match(pat,s):
# #       return True
# #    return False
# #
# # s = "popular_website15@comPany.com"
# # print(solve(s))
#
# # Password validation in Python
# # using naive method
#
# # Function to validate the password
# def password_check(passwd):
#     SpecialSym = ['$', '@', '#', '%']
#     val = True
#
#     if len(passwd) < 8:
#         return 'length should be at least 6'
#
#     if not any(char.isdigit() for char in passwd):
#         return 'Password should have at least one numeral'
#
#     if not any(char.isupper() for char in passwd):
#         return 'Password should have at least one uppercase letter'
#
#     if not any(char.islower() for char in passwd):
#         return 'Password should have at least one lowercase letter'
#
#     if not any(char in SpecialSym for char in passwd):
#         return 'Password should have at least one of the symbols $@#'
#     else:
#         return True
#
# print(password_check("klguiuyi3A$"))
#
#
#

list = ['Tyres-5000', 'Wipers-1500']

for service in list:
    print(service)
    split = service.split('-')
    print(split)
    item = split[0]
    cost = split[1]
    print('Item', item)
    print('Cost is ',cost)

