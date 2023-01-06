import os
import shutil
import time

import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.headless = True
connection = psycopg2.connect(
    host="127.0.0.1",
    database="postgres9",
    user="postgres",
    password="0852")

def my_selen():
    driver = webdriver.Chrome(options=options)
    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM my")
    all_data = cursor.fetchall()
    input_link = all_data[-1][1]
    replace_folder_path = all_data[-1][2]
    print(input_link,'111')
    print(replace_folder_path,'222')
    # input_link = "https://intranet.ytit.uz/course/view.php?id=2877"
    # replace_folder_path = ''

    driver.get("https://intranet.ytit.uz/login/index.php")
    driver.find_element(By.NAME, 'username').send_keys('ier20037')
    time.sleep(2)
    driver.find_element(By.NAME, 'password').send_keys('AC2558243')
    time.sleep(3.2)
    button = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[3]/div/div/section/div/div[2]/div/div[2]/div[1]/form/button')
    button.click()
    time.sleep(2.5)
    driver.get(input_link)
    time.sleep(2.5)
    driver.refresh()
    all_data = driver.find_element(By.XPATH, '//*[@id="region-main"]').text
    data = all_data.split(' ')
    data1 = ' '.join(map(str, data))
    data2 = data1.split('\n')
    fake_data = ['Ваши достижения', 'Тематический план', 'Объявления', 'Форум', 'Общее', '']
    all_texts = []
    for i in data2:
        if i not in fake_data:
            all_texts.append(i)

    # print(all_texts)

    all_data = driver.find_element(By.XPATH, '//*[@id="region-main"]').text
    data = all_data.split(' ')
    data1 = ' '.join(map(str, data))
    data2 = data1.split('\n')
    all_h3 = []
    h3 = driver.find_elements(By.TAG_NAME, 'h3')
    for i in h3:
        if i.text == '':
            continue
        if i.text == 'Click here!':
            continue
        if i.text == 'Final Exam':
            continue
        if i.text == 'videolar':
            continue

            # print(i.text, 'h3 tags')
        all_h3.append(i.text)
        # else:
        #     continue
    # print(all_h3)

    f_data = []

    for el in all_h3:
        indeks_of_week = [i for i in range(0, len(all_texts)) if el == all_texts[i]]
        for i in indeks_of_week:
            if i not in f_data:
                f_data.append(i)
    try:
        for k in range(0, len(f_data)):
            if all_texts[f_data[k]] == all_texts[f_data[k + 1]]:
                del f_data[k + 1]
    except:
        print('bajarildi')
    # print(f_data)
    # replace_folder_path = "D:\LMS_FILES\Advertising-uzbek"
    all_files = []
    list_of_files = filter(lambda x: os.path.isfile(os.path.join(replace_folder_path, x)),
                           os.listdir(replace_folder_path))
    list_of_files = sorted(list_of_files, key=lambda x: os.path.getmtime(os.path.join(replace_folder_path, x)))
    for file_name in list_of_files:
        all_files.append(file_name)
    # print(all_files)
    parent_dir = "D:\est"
    directory1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/header/div/div/div/div[1]/div[1]/div/div').text
    # directory1 = 'ADVERTISING-UZBEK'
    # directory1 = str(random.randint(1, 1000))
    print(directory1)
    path = os.path.join(parent_dir, directory1)
    print('path ga keldi')
    os.mkdir(path)
    print('os ga', len(all_h3))
    extra = []
    for i in all_h3:
        # print('i', i, 'shu')
        parent_dir1 = f"{parent_dir}\{directory1}"
        parent_dir2 = f"{parent_dir}\{directory1}\{i.replace(':', ' ').replace('(', '').replace(')', '').replace('*','')}"
        extra.append(parent_dir2.replace('\\', '/'))

        path1 = os.path.join(parent_dir1, i.replace(':', ' ').replace('(', '').replace(')', '').replace('*',''))
        os.mkdir(path1)
    print(extra)
    try:
        for i in range(0, len(all_h3) + 1):
            if i > 0 and f_data[i] == 0:
                cycle = all_texts[f_data[i]:f_data[i + 1]]
            if i == 0:
                cycle = all_texts[0:f_data[i]]
            if i != 0:
                cycle = all_texts[f_data[i - 1]:f_data[i]]
            if i == 0 and f_data[i] == 0:
                cycle = all_texts[f_data[i]:f_data[i + 1]]
            if (len(cycle) >= 2) or ('Файл' in cycle) or ('Папка' in cycle):
                all1 = []
                all_sizes1 = []
                for i1 in range(0, len(cycle)):
                    # #telebots2('cycle', cycle)
                    if ('Видео-урок' in cycle[i1] or 'Proyeksiyalash mashqlar' in cycle[i1]) and cycle[
                        i1 + 1] == 'Файл' or 'Гиперссылка' in cycle[i1].strip():
                        continue
                    if cycle[i1] == 'Файл':
                        all_file = f"{replace_folder_path}\{all_files[0]}"
                        all1.append(all_file)
                        del all_files[0]
                    else:
                        continue
                parent_dir1 = f"{parent_dir}\{directory1}"
                # print(all1)
                list_of_files = filter(lambda x: os.path.isfile(os.path.join(replace_folder_path, x)),
                                       os.listdir(replace_folder_path))
                list_of_files = sorted(list_of_files,
                                       key=lambda x: os.path.getmtime(os.path.join(replace_folder_path, x)))
                for file, file_name in zip(all1, list_of_files):
                    print(file_name)
                    # org_file = f"{extra[i]/file_name}"
                    # print(org_file)
                    print(file)
                    # D:\LMS_FILES\Advertising-uzbek\Интернет реклама.pptx
                    shutil.copy(file, extra[i])
    except:
        print('tugadi')

# shutil.move('/Users/billy/d1/xfile.txt', '/Users/billy/d2/xfile.txt')
#indeks_file = [d for d in range(0, len(cycle)) if cycle[d] == "Файл"]
# driver.quit()
my_selen()
