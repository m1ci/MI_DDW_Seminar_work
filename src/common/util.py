import datetime
import json
import time
from os import listdir
from os.path import isfile, join

import src.common.configuration as configuration


def get_name_from_url(url):
    return url[url.rfind('/') + 1:]


def get_mili_time_diff(initial_time, final_time):
    time_diff = final_time - initial_time
    return int(time_diff.total_seconds() * 1000)


def wait_crawl_delay(initial_time, crawl_delay):
    final_time = datetime.datetime.now()
    time_diff = get_mili_time_diff(initial_time, final_time)

    if time_diff < crawl_delay:
        time.sleep((crawl_delay - time_diff) / 1000)


def get_urls(value):
    path = ""
    url_array = []

    if value == configuration.DEBUG:
        path = "../data/dbpedia/debug.json"
    elif value == configuration.CITY:
        path = "../data/dbpedia/city.json"
    elif value == configuration.SPORT:
        path = "../data/dbpedia/sport.json"
    elif value == configuration.MUSICAL_ARTIST:
        path = "../data/dbpedia/musicalArtist.json"

    if path != "":
        with open(path) as f:
            data = json.load(f)

        for url in data["results"]["bindings"]:
            url_array.append(url["url"]["value"])

    return url_array


def get_available_urls(value):
    path = ""

    if value == configuration.DEBUG:
        path = "../data/dumps/available_urls_debug.json"
    elif value == configuration.CITY:
        path = "../data/dbpedia/available_urls_city.json"
    elif value == configuration.SPORT:
        path = "../data/dbpedia/available_urls_sport.json"
    elif value == configuration.MUSICAL_ARTIST:
        path = "../data/dbpedia/available_urls_musicalArtist.json"

    with open(path) as f:
        data = json.load(f)

    return data["urls"]


def get_all_files_from_path(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def generate_url_from_name(name):
    return "http://en.wikipedia.org/wiki/" + name


def save_file(filename, string):
    f = open(filename, 'w')
    f.write(string)
    f.close()


def remove_file_extension_from_name(file_name):
    return file_name[:file_name.rfind(".")]
