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

    data = read_comb_output(sys.stdin)
    for category, video_id, country_sum in data:
        if current_category != category:

            output = "{}: {}".format(current_category, round(video_id_dict[video_id]/len(video_id_dict), 2))
            print(output.strip())
            current_category = category
            video_id_dict = {}

        # video_id_set = video_id_dict.get(current_category, set())
        # video_id_set.add(video_id)
        # video_id_dict[current_category] = video_id_set

        video_id_dict[video_id] = video_id_dict.get(video_id, 0) + country_sum

    if current_category != "":
        output = "{}: {}".format(current_category, round(video_id_dict[video_id]/len(video_id_dict), 2))
        print(output.strip())


if __name__ == "__main__":
    reducer()
