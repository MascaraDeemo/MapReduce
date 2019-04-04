#!/usr/bin/python3

import sys


def mapper():
    """ This mapper select tags and return the tag-owner information.
    Input format: video_id,trending_date,category_id,category,publish_time,views,likes,dislikes,
    comment_count,ratings_disable,video_error_or_removed,country
    Output format: category,video_id,country
    """
    for line in sys.stdin:
        # Clean input and split it

        line = line.strip()
        parts = line.split(",")

        # Check that the line is of the correct format
        if len(parts) != 12:
            continue

        video_id = parts[0].strip()
        category = parts[3].strip()
        if category == 'category':
            continue
        country = parts[11].strip()
        print("{cat}\t{meta}".format(cat=category, meta='%s,%s' % (video_id, country)))


if __name__ == "__main__":
    mapper()
