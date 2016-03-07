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
