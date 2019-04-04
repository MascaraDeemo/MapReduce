#!/usr/bin/python3

import sys


def read_comb_output(file):
    """ Return an iterator extracted from file (sys.stdin)
    Input format:  category,video_id,country_sum_for_vid
    Output format: same
    """
    for line in file:
        yield line.strip().split("\t", 1)


def reducer():
    """
    Input format: category,video_id,country_sum_for_vid
    Output format: category: average
    """

    current_category = ""
    video_id_dict = {}
    country_total = 0

    data = read_comb_output(sys.stdin)
    for category, video_id_country_sum in data:
        if current_category != category:

            if current_category != "":
                output = "{cat}: {result}".format(cat=current_category, result="%.2f" % (country_total / len(video_id_set)))
                country_total = 0
                print(output.strip())

            current_category = category
            video_id_dict = {}
        vid, country_sum = video_id_country_sum.split(',')
        video_id_set = video_id_dict.get(current_category, set())
        video_id_set.add(vid)
        video_id_dict[current_category] = video_id_set
        country_total += int(country_sum)

    if current_category != "":
        output = "{cat}: {result}".format(cat=current_category, result="%.2f" % (country_total / len(video_id_set)))
        print(output.strip())


if __name__ == "__main__":
    reducer()