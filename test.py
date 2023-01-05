# # Python program to explain os.mkdir() method
#
# # importing os module
# import os
#
# # Directory
# directory = "masdas"
#
# # Parent Directory path
# parent_dir = "D:"
#
# # Path
# path = os.path.join(parent_dir, directory)
#
# # Create the directory
# # 'GeeksForGeeks' in
# # '/home / User / Documents'
# os.mkdir(path)
# print("Directory '% s' created" % directory)
#
#
# parent_dir = "D:\est"
# directory1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/header/div/div/div/div[1]/div[1]/div/div').text
# # directory1 = 'ADVERTISING-UZBEK'
# # directory1 = str(random.randint(1, 1000))
# print(directory1)
# path = os.path.join(parent_dir, directory1)
# print('path ga keldi')
# os.mkdir(path)
# print('os ga', len(all_h3))
# for i in all_h3:
#     # print('i', i, 'shu')
#     parent_dir1 = f"{parent_dir}\{directory1}"
#     # print(parent_dir1)
#     path1 = os.path.join(parent_dir1, i.replace(':', ' ').replace('(', '').replace(')', ''))
#     os.mkdir(path1)
# import shutil
#
# shutil.move('D:/LMS_FILES/Advertising-uzbek/1-mavzu.pptx','D:/est/ADVERTISING-UZBEK/1-mavzu  Reklama bilan tanishish  Kecha, bugun va ertaga reklama/')
import psycopg2

connection = psycopg2.connect(
    host="127.0.0.1",
    database="postgres9",
    user="postgres",
    password="0852")
cursor = connection.cursor()
cursor.execute("SELECT * FROM my")
all_data = cursor.fetchall()
# print(all_data)
# print(all_data[-1])
print(all_data[-1][1])
print(all_data[-1][2])
