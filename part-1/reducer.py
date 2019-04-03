#!/usr/bin/python3

import sys


def read_comb_output(file):
    """ Return an iterator extracted from file (sys.stdin)
    Input format:  category,video_id,country_sum_for_vid
    Output format: same
    """
    for line in file:
        yield line.strip().split(",")


def reducer():
    """
    Input format: category,video_id,country_sum_for_vid
    Output format: category: average
    """
    current_category = ""
    video_id_dict = {}
    country_total = 0

    data = read_comb_output(sys.stdin)
    for category, video_id, country_sum in data:
        if current_category != category:

            if current_category != "":
                output = current_category + ": " + len(video_id_dict[current_category])/country_total
                print(output.strip())

            current_category = category
            video_id_dict = {}

        video_id_set = video_id_dict.get(current_category, set())
        video_id_set.add(video_id)
        video_id_dict[current_category] = video_id_set
        country_total += country_sum

    if current_category != "":
        output = current_category + ": " + len(video_id_dict[current_category])/country_total
        print(output.strip())


if __name__ == "__main__":
    reducer()
