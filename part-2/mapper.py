from pyspark import SparkContext
sc = SparkContext(appName='part-2')
output_path = 'output'
videos = sc.textFile('AllVideos_short.csv')


def mapper(line):
    line = line.strip()
    parts = line.split(",")
    vid = parts[0].strip()
    trending_date = parts[1].strip()
    category = parts[3].strip()
    likes = parts[6].strip()
    dislikes = parts[7].strip()
    country = parts[11].strip()
    key = vid + "," + category + "," + country
    value = trending_date + "," + likes + "," + dislikes
    return key, value

