# -*- coding: utf-8 -*-
# author: https://github.com/Zfour
from bs4 import BeautifulSoup
import os
import request
import json
import config

version = 'v3'
outputdir = version  # 输出文件结构变化时，更新输出路径版本
filenames = []
json_pool = []


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("create dir:", path)
    else:
        print("dir exists:", path)


def github_issuse(json_pool):
    print('\n')
    print('------- github issues start ----------')
    baselink = 'https://github.com/'
    cfg = config.load()
    filter = cfg['issues']
    for lbl in filter["labels"]:
        try:
            filenames.append(lbl)
            for number in range(1, 100):
                print('page:', number)
                url = 'https://github.com/' + filter[
                    'repo'] + '/issues?page=' + str(number) + '&q=is%3Aopen'
                if lbl:
                    url = url + '+label%3A' + lbl
                if filter['sort']:
                    url = url + '+sort%3A' + filter['sort']
                print('parse:', url)
                github = request.get_data(url)
                soup = BeautifulSoup(github, 'html.parser')
                main_content = soup.find_all('div', {'aria-label': 'Issues'})
                linklist = main_content[0].find_all('a',
                                                    {'class': 'Link--primary'})
                if len(linklist) == 0:
                    print('> end')
                    break
                for item in linklist:
                    issueslink = baselink + item['href']
                    issues_page = request.get_data(issueslink)
                    issues_soup = BeautifulSoup(issues_page, 'html.parser')
                    try:
                        issues_linklist = issues_soup.find_all('pre')
                        source = issues_linklist[0].text
                        if "{" in source:
                            source = json.loads(source)
                            print(source)
                            json_pool.append(source)
                    except:
                        continue
        except Exception as e:
            print('> end')

    print('------- github issues end ----------')
    print('\n')


# 友链规则
github_issuse(json_pool)
mkdir(outputdir)
full_path = []
i = 0
for filename in filenames:
    full_path.append(outputdir + '/' + filename + '.json')
    with open(full_path[i], 'w', encoding='utf-8') as file_obj:
        data = {'version': version, 'content': json_pool}
        json.dump(data, file_obj, ensure_ascii=False, indent=2)
    i += 1
