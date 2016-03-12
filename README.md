# Big Data
Hadoop Platform and Application Framework. Content and exercises from Coursera - University of California, San Diego

## Map Reduce

### Generate input data

  ```
  > sh map-reduce/data_generator/data_generator.script
  ```
### Running without hadoop stack (local)

  ```
  > cat map-reduce/input/join2_gen* | map-reduce/join2_mapper.py | sort | map-reduce/join2_reducer.py
  ```

### Running with hadoop stack (remote - cloudera)
  ```
  > hdfs dfs -put map-reduce/input /user/cloudera/input
  > hdfs dfs -ls /user/cloudera/input
  > hdfs dfs -cat /user/cloudera/input/join2_genchanA.txt
  ```

  ```
  > hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
     -input /user/cloudera/input \
     -output /user/cloudera/output \
     -mapper map-reduce/join2_mapper.py \
     -reducer map-reduce/join2_reducer.py
  ```


## Spark
Wordcount exercise using PySpark

You will need to enter in the PySpark console:
  ```
  > sudo easy_install ipython==1.2.1
  ```

  ```
  > PYSPARK_DRIVER_PYTHON=ipython pyspark
  ```

Reading: Resiliant Destributed Datasets

  ```
  Spark> fileA = sc.textFile("input/map-reduce/join1_FileA.txt")
  Spark> fileA.collect()
  Spark>  Out[]: [u'able,991', u'about,11', u'burger,15', u'actor,22']

  Spark> fileB = sc.textFile("input/map-reduce/join1_FileB.txt")
  Spark> fileB.collect()
  Spark> Out[29]:
     [u'Jan-01 able,5',
       u'Feb-02 about,3',
       u'Mar-03 about,8',
       u'Apr-04 able,13',
       u'Feb-22 actor,3',
       u'Feb-23 burger,5',
       u'Mar-08 burger,2',
       u'Dec-15 able,100']
  ```

Loading code into PySpark console:
  ```
  Spark> load spark/wordcount.py
  ```

Testing code:
  ```
  Spark> test_splitA()
  Spark> True
  Spark> test_splitB()
  Spark> True
  ```

Applying split_fileA function to dataset A:

  ```
  Spark> fileA_data = fileA.map(split_fileA)
  Spark> fileA_data.collect()
  ```

Applying split_fileB function to dataset B:

  ```
  Spark> fileB_data = fileB.map(split_fileB)
  Spark> fileB_data.collect()
  ```


Join A and B:
  ```
  Spark> fileB_joined_fileA = fileB_data.join(fileA_data)
  Spark> fileB_joined_fileA.collect()
  ```

