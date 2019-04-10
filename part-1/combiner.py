#!/usr/bin/python3

import sys


def read_map_output(file):
    """ Return an iterator extracted from file (sys.stdin)
    Input format:  category,video_id, country
    Output format: category,video_id, country
    """
    for line in file:
        yield line.strip().split("\t", 1)


def combiner():
    """ This combiner reads in category, video_id and country_count returns the
    total sum of video_id per category and use country_count to divide it in order to get the average
    Input format: category,video_id,country
    Output format: category,(video_id, country_sum_for_videoId)
    """
    current_category = ""
    country_dict = {}

    data = read_map_output(sys.stdin)
    for category, video_id_and_country in data:
        if current_category != category:

            if current_category != "":
                for vid, country_set in country_dict.items():
                    output = "{cat}\t{vid_country}".format(cat=current_category,
                                                           vid_country='%s,%s' % (vid, len(country_set)))
                    print(output.strip())
            current_category = category
            country_dict = {}
        vid, country = video_id_and_country.split(',')
        country_set = country_dict.get(vid, set())
        country_set.add(country)
        country_dict[vid] = country_set

        # country_set = country_dict.get(video_id, set())
        # country_set.add(country)
        # country_dict[video_id] = country_set

    if current_category != "":
        for vid, country_set in country_dict.items():
            output = "{cat}\t{vid_country}".format(cat=current_category,
                                                   vid_country='%s,%s' % (vid, len(country_set)))
            print(output.strip())


if __name__ == "__main__":
    combiner()
