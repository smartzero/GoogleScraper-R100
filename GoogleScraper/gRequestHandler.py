#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
gRequestHandler:
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import logging
from time import strftime
from urllib import urlencode


def timestamp():
    """
    About Me:
        what are looking at, i'm just a wallclock.
    """
    return strftime("%c")


class GoogReq(object):
    """
        gRequestHandler
    """
    def __init__(self, driver=None):
        self.driver = driver or webdriver.Firefox()

    def captcha_check(self):
        """
        About Me:
            I won't tolerate any smart ass.
        """
        try:
            elem = self.driver.find_element_by_name('captcha')
            elem.send_keys(raw_input('answer to the captcha challenge? '))
            return False
        except NoSuchElementException:
            logging.warning('%s :: captcha challenge!', timestamp())
        return True

    def load_page(self, url):
        """
        About Me:
            I am the captain of url shipment. I just do the delivery.
        Threat Assesment:
            None
        Intel:
            INFO level
        TODO:
            check if the url is perfectly encoded..
        """
        self.driver.get(url)
        logging.info('%s :: GoogReq.load_page is loading %s', timestamp(), url)

    def save_csv(self):
        """
            save_csv
        """
        pass


def main():
    """
        main program
    """
    # add config rigs to the firefox driver
    req = GoogReq()
    req.driver.capabilities[u'javascriptEnabled'] = False
    req.driver.capabilities[u'databaseEnabled'] = False
    req.driver.capabilities[u'locationContextEnabled'] = False
    req.driver.capabilities[u'platform'] = u'win32'
    req.driver.capabilities[u'browseName'] = u'chrome'
    req.driver.capabilities[u'webStorageEnabled'] = False
    with open('queries.txt', 'r') as f:
        for index, Query in map(str.split, f.readlines()):
            print 'processing %s query' % index
            params = {
                'q': Query,
                'num': 100
            }
            req.load_page(
                'https://www.google.com/search/?{}'.format(urlencode(params)))
            raw_input('waiting... ')

if __name__ == '__main__':
    main()
