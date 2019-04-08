from pyspark import SparkContext
import argparse


def mapper(line):
    line = line.strip()
    part = line.split(',')
    vid = part[0].strip()
    trending_date = part[1].strip()
    category = part[3].strip()
    likes = part[6].strip()
    dislikes = part[7].strip()
    country = part[11].strip()
    key = vid + '/' + country + '/' + category
    value = trending_date + '/' + likes + '/' + dislikes
    return key, value


def calculate_difference(value):
    line_in_iterator = [i for i in value]
    likes_dislikes = [[0, 0], [0, 0]]
    difference = [0, 0]
    if len(line_in_iterator) > 1:
        for i in range(2):
            split = line_in_iterator[i].split("/")
            likes_dislikes[i][0] = int(split[1])
            likes_dislikes[i][1] = int(split[2])

        difference[0] = likes_dislikes[1][0] - likes_dislikes[0][0]
        difference[1] = likes_dislikes[1][1] - likes_dislikes[0][1]
        result = difference[1] - difference[0]
        return result
    return 0


def mapToFormat(line):
    overall = line[0]
    result = line[1]
    splited = overall.split('/')
    vid = splited[0]
    country = splited[1]
    category = splited[2]
    key = vid
    value = str(result) + ',' + category + ',' + country
    return key, value


if __name__ == "__main__":
    sc = SparkContext(appName='part-2')
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Input path", default='~/')
    parser.add_argument("--output", help="Output path", default='~/')
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    csv = sc.textFile(input_path + 'AllVideos_short.csv')
    csvNoHead = csv.zipWithIndex().filter(lambda tup: tup[1] > 0).keys()
    after_map = csvNoHead.map(mapper)
    after_calculate = after_map.groupByKey().mapValues(calculate_difference)
    sortedByResult = after_calculate.sortBy(lambda a: a[1], 0)
    answer = sortedByResult.map(mapToFormat)
    output = answer.collect()[:10]
    output1 = sc.parallelize(output)
    output1.saveAsTextFile(output_path)

