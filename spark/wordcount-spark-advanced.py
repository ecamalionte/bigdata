

#Shows
#> hdfs dfs -ls input/map-reduce
show_views_file = sc.textFile("input/map-reduce/final/join2_gennum?.txt")
show_views_file.take(2)

# [u'Hourly_Sports,21', u'PostModern_Show,38']

def split_show_views(line):
    show, views = line.split(',')
    return (show, int(views))

show_views = show_views_file.map(split_show_views)


#Channels
show_channel_file = sc.textFile("input/map-reduce/final/join2_genchan?.txt")
def split_show_channel(line):
    show, channel = line.split(',')
    return (show, channel)

show_channel = show_channel_file.map(split_show_channel)


#Join
joined_dataset = show_views.join(show_channel)

def extract_channel_views(show_views_channel):
    show, views_channel = show_views_channel
    views, channel = views_channel
    return (channel, views)

channel_views = joined_dataset.map(extract_channel_views)

def some_function(a, b):
    return ( a + b )


channel_views.reduceByKey(some_function).collect()
