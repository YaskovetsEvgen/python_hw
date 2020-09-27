import re
# определяем количество запросов
def request_numbers():  
    with open('pars.txt', 'r') as f:
        counter = -1
        for line in f:
            counter += 1
        print('запросов :', counter)
# определяем количество уникальных запросов
def unique_ip():  
    with open('pars.txt', 'r') as f:
        ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip_list = set()
        for line in f:
            if len(line) <= 1:
                continue
            else:
                result = re.search(ip, line)
                ip_list.add(result.group(0))
        print('уникальных ip адресов:', len(ip_list))
# определяем какие браузеры обращались и сколько раз
def browser_counter():  
    with open('pars.txt', 'r') as f:
        counter = {
            'Opera': 0,
            'Chrome': 0,
            'Safari': 0,
            'Firefox': 0,
             }
        for line in f:
            brows = line[-60:-6]
            for keys in counter.keys():
                if keys in brows:
                    counter[keys] += 1
        print('обращений браузоров:')
        for keys, values in counter.items():
            print(keys, '-', values)

if __name__ == '__main__':
    request_numbers()
    unique_ip()
    browser_counter()