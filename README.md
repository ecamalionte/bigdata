# Big Data
Hadoop Platform and Application Framework. Content and exercises from Coursera - University of California, San Diego

## Map Reduce

### Generate input data

  ```
  > cd map-reduce
  > sh /data_generator/data_generator.script
  ```
### Run and test map/reduce without hadoop stack 

  ```
  > cat input/join2_gen* | ./join2_mapper.py | sort | ./join2_reducer.py
  ```

### Running with hadoop
  ```
  > hdfs dfs -put input /user/cloudera/input
  > hdfs dfs -ls /user/cloudera/input
  > hdfs dfs -cat /user/cloudera/input/join2_genchanA.txt
  ```
  
  ```
  > hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
     -input /user/cloudera/input \
     -output /user/cloudera/output \   
     -mapper ./join2_mapper.py \   
     -reducer ./join1_reducer.py
  ```
