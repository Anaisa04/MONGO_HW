from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/Users/cerda005/Downloads/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    urls = {}

    url = "https://astrogeology.usgs.gov/maps/mars-viking-hemisphere-point-perspectives"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    return urls