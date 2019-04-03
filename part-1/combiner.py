#!/usr/bin/python3

import sys


def read_map_output(file):
    """ Return an iterator extracted from file (sys.stdin)
    Input format:  category,video_id, country
    Output format: category,video_id, country
    """
    for line in file:
        yield line.strip().split(",")


def combiner():
    """ This reducer reads in category, video_id and country_count returns the
    total sum of video_id per category and use country_count to divide it in order to get the average
    Input format: category,video_id,country
    Output format: category,video_id, country_sum_for_videoId
    """
    current_category = ""
    country_dict = {}

    data = read_map_output(sys.stdin)
    for category, video_id, country in data:
        if current_category != category:

            if current_category != "":
                output = "{},{},{}".format(current_category, video_id, len(country_dict[current_category]))
                print(output.strip())

            current_category = category
            country_dict = {}

        country_set = country_dict.get(current_category, set())
        country_set.add(country)
        country_dict[current_category] = country_set

    if current_category != "":
        output = "{},{},{}".format(current_category, video_id, len(country_dict[current_category]))
        print(output.strip())


if __name__ == "__main__":
    combiner()