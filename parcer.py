import time
import pandas as pd
from selenium import webdriver
from multiprocessing import Pool
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait



""" The parcer which parces data about phones from two sites """


# class TelephoneExtractor():


    # def __init__(self) -> None:
    #     pass


# @staticmethod
def data_extract(path):
    """The func extracts data from excel file and separates it into 2 columns Serial Number and Title 
    :param path: path to file
    :type path: str 
    :return: tuple with str in there
    """
    file_extract = pd.read_excel(path, sheet_name='Лист1')
    article = file_extract["Артикул"].to_list()
    title = file_extract["Название"].to_list()
    return article, title

data = data_extract(path = 'data21.xlsx')

urls_list = ['https://stylus.ua/', 'https://pulsepad.com.ua/']


def return_driver():
    """The func appeals to driver by path where the file is
    :return: variable with appeal to driver file
    """
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
            executable_path = "C:\\Users\\analytic8\\Desktop\\TelephoneParcer\\web_driver\\chromedriver", options = options)
            # executable_path = "C:\\Users\\analytic6\\Desktop\\TelephoneParcer\\web_driver\\chromedriver", options = options)
    return driver

# def send_request_to_pulsepad(url):
    """The func opens a browser and finds the site where needs to parse data about phones and makes requests to find elements with necessary data and parces they. After that the func adds this info to pd dataframe and saves it to excel
    :param url: path to necessary site
    :type url: str 
    :return: excel file with data
    """
#     try:
#         df = pd.DataFrame()
#         driver = return_driver()
#         driver.get(url = url)
#         for item in data[0]:
#             if item == 0:
#                 break
#             data_in_dict = {}
#             search = driver.find_element_by_class_name('input_search')
#             search.clear()
#             search.send_keys(item)
#             search.send_keys(Keys.ENTER)
#             time.sleep(1)
#             try:
#                 description_1 = WebDriverWait(driver, 10).until(lambda x: 
#                 x.find_element_by_xpath('//*[@id="mid_col"]/div[3]/p/span[1]'))
#                 description_2 = WebDriverWait(driver, 10).until(lambda x: 
#                 x.find_element_by_xpath('//*[@id="mid_col"]/div[3]/p/span[2]'))
#                 image_ref = driver.find_element_by_class_name('zoom')
#                 image_ref = image_ref.get_attribute("href")
#                 ram = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[6]/td[1]')
#                 ram_value = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[6]/td[2]/div/p')
#                 name_title = driver.find_element_by_xpath('//div/div/div/div/div/div/div/h1/span')
#                 memory = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[7]/td[1]')
#                 memory_value = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[7]/td[2]/div/p')
#                 sim = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[10]/td[1]')
#                 sim_value = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[10]/td[2]/div/p')
#                 processor = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[11]/td[1]')
#                 processor_value = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[11]/td[2]/div/p')
#                 battery = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[12]/td[1]')
#                 battery_value = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[12]/td[2]/div/p')
#                 monitor = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[14]/td[1]')
#                 monitor_value = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[14]/td[2]/div/p')
#                 operation_system = driver.find_element_by_xpath('//*[@id="all"]/table/tbody/tr[4]/td[1]')
#                 operation_system_value = driver.find_element_by_class_name('p_l-10')
#                 if not None:
#                     data_in_dict[monitor.text] = monitor_value.text
#                     data_in_dict[battery.text] = battery_value.text
#                     data_in_dict[processor.text] = processor_value.text
#                     data_in_dict[sim.text] = sim_value.text
#                     data_in_dict[memory.text] = memory_value.text
#                     data_in_dict[ram.text] = ram_value.text
#                     data_in_dict[operation_system.text] = operation_system_value.text
#                     data_in_dict['description'] = "".join(description_1.text) + "".join (description_2.text)
#                     data_in_dict['image'] = image_ref
#                     df = df.append(pd.DataFrame(data_in_dict, index=[name_title.text]))
#             except Exception as e:
#                 print(e)    
#         df.to_excel("phones_1.xlsx")
#     except Exception as e:
#         print(e)
#     finally:
#         driver.close()
#         driver.quit()
#         print("Data has been upload!")




# send_request_to_pulsepad(urls_list[1])

def send_request_to_stylus(url):
    """The func opens a browser and finds the site where needs to parse data about phones and makes requests to find elements with necessary data and parces they. After that the func adds this info to pd dataframe and saves it to excel
    :param url: path to necessary site
    :type url: str 
    :return: excel file with data
    """
    try:
        df = pd.DataFrame()
        driver = return_driver()
        driver.get(url = url)
        for item in data[1]:
            if item:
                try:
                    dict_with_data = {}
                    time.sleep(2)
                    search = driver.find_element_by_class_name('search-field')
                    search.clear()
                    search.send_keys(item)
                    search.send_keys(Keys.ENTER)
                    time.sleep(1)
                    title = driver.find_element_by_xpath('//*[@id="tab-all"]/div/div[2]/div/h2')
                    title = title.text
                    time.sleep(3)
                    dict_for_parcer = {'//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[2]/td[1]': '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[2]/td[2]', '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[3]/td[1]':'//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[3]/td[2]', '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[4]/td[1]':'//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[4]/td[2]', '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[6]/td[1]':'//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[6]/td[2]', '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[7]/td[1]': '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[7]/td[2]', '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[9]/td[1]': '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[9]/td[2]', '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[10]/td[1]': '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[10]/td[2]', '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[11]/td[1]': '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[11]/td[2]', '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[12]/td[1]': '//*[@id="tab-all"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[12]/td[2]'}
                    time.sleep(1)
                    for k, v in dict_for_parcer.items():
                        try:
                            if v != 'NaN':
                                name = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(k))
                                value = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(v))
                                dict_with_data[name.text] = value.text
                                dict_with_data['Description: '] = (WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath('//*[@id="tab-all"]/div/div[2]/div/div[1]/div[1]'))).text
                                image_ref = driver.find_element_by_xpath('//*[@id="product-layout"]/div[2]/div[1]/div[1]/div/ul/li[1]/picture/img')
                                image_ref = f'https://stylus.ua/{image_ref.get_attribute("src")}'
                                dict_with_data['Image:'] = image_ref
                            else:
                                v = 0
                        except Exception as e:
                            print(e)
                            continue
                    df = df.append(pd.DataFrame(dict_with_data, index=[title[15:]]))
                except Exception as e:
                    print(e)
            else: 
                continue
            df.to_excel(f"phones_from_{(urls_list[0].split('//'))[1].split('.')[0]}.xlsx")
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()
        print("Data has been upload!")

send_request_to_stylus(urls_list[0])







# if __name__ == '__main__':
#     p = Pool(processes=2)
#     p.map(send_request_to_parse_data, urls_list)