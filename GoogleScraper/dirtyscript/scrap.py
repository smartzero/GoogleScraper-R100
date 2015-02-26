#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# pylint: disable=C0111
# pep8: disable=E501
from urllib import urlencode
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def parse_content(doc):
    soup = BeautifulSoup(doc)
    links = []
    for link in soup.find_all('a'):
        if link.get('href').startswith('https://www.google.co.in/patents/'):
            links.append(link.get('href'))
            links[-1] = links[-1][:links[-1].find('?')]
    return links


def main():
    driver = webdriver.Firefox()
    with open('queries.txt', 'r') as f:
        # print f.readline()
        for item in map(str.split, f.readlines()):
            index = item[0]
            Query = ' '.join(item[1:])
            print 'processing %s query' % index
            params = {
                'q': Query,
                'tbo': 'p',
                'tbm': 'pts',
                'num': 100,
                'start': 0
            }
            url = 'https://www.google.com/search?{}'.format
            for x in xrange(4, 10):
                params['start'] = x*100
                driver.get(
                    url(urlencode(params)))
                try:
                    links = parse_content(driver.find_element_by_class_name('srg').get_attribute('innerHTML'))
                except NoSuchElementException:
                    try:
                        elem = driver.find_element_by_name('captcha')
                        elem.send_keys(raw_input('captcha? '))
                        elem.submit()
                        links = parse_content(driver.find_element_by_class_name('srg').get_attribute('innerHTML'))
                    except NoSuchElementException:
                        print 'no results for', Query, x
                        break
                open('{} - {}'.format(Query, x), 'w').write('\n'.join(links))
                #driver.delete_all_cookies()
                # sleep(randrange(2, 3))


main()

