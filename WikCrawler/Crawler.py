#!/usr/bin/env python3
import argparse
from WikCrawler import info
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-s","--search",help="Search any topic")
parser.add_argument("-i","--info",help="Get info on any topic")
parser.add_argument("-q","--quick",help="Print a summary and relevant links to the IO and a .txt document")
parser.add_argument("-l","--lang",help="Get info in your native language (default english)")


a = parser.parse_args()

def arguments():

    #In case we want to do language selection
    
    #if a.quick and a.lang:
        #info.getSummary(a.quick,a.lang)
    #if a.info and a.lang:
        #info.getInfo(a.info,a.lang)
    #if a.search and a.lang:
        #info.searchInfo(a.search,a.lang)
    if a.search and a.lang == None:
        info.searchInfo(a.search)
    if a.info and a.lang == None:
        info.getInfo(a.info)
    if a.quick and a.lang == None:
        info.getSummary(a.quick)
   

arguments()


