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
     -reducer map-reduce/join1_reducer.py
  ```
