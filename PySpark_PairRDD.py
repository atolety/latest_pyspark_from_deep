from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('IntellipaatPairRDD').setMaster('local')
sc = SparkContext.getOrCreate(conf=conf)
#-----------------------------------------------------------------------------------------------
# Pair RDDs are RDDs with Key-Value pairs. It is needed most of the cases than normal RDDs.
# Whenever you see <some-operation>ByKey, that transformation can only be performed on pair
# RDDs.
#-----------------------------------------------------------------------------------------------
# Convert a normal RDD to a key value pair RDD - using "map" transformation
#-----------------------------------------------------------------------------------------------
BasicRDD = sc.textFile('/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/violations_plus.csv')
# PairRDD = BasicRDD.map(lambda x: (x.split(',')[1],x))
#
# print('by map transformation...')
# for i in PairRDD.take(5):
#     print(i)

#-----------------------------------------------------------------------------------------------
# Convert a normal RDD to a key value pair RDD - using "keyBy" transformation
#-----------------------------------------------------------------------------------------------
# pairRDD = BasicRDD.keyBy(lambda x: x.split(',')[1])
#
# print('by keyBy transformation...')
# for i in pairRDD.take(5):
#     print(i)

# print(pairRDD.keys().collect())       # Extract keys
# print(pairRDD.values().collect())     # Extract values
# print(pairRDD.lookup('"20140114"'))

##############################################################################################
'''
Pair RDD Transformations:-
1. groupByKey() - Group based on a key: (K,V) -> (K, iterable <V>)
2. reduceByKey(func) - Aggregate by key based on the func: (K,V) -> (K, V after applying func)
3. sortByKey(ascending=True|False) - Sort on key basis: (K,V) -> (Sorted K,V)
4. join(rdd) - Joins two RDDs based on key: (K,V)&(K,W) -> (K,(V,W)).
   leftOuterJoin, rightOuterJoin, fullOuterJoin are also there.
5. cogroup(rdd) - Groups two RDDs based on key: (K,V)&(K,W) -> (K,(iterable V, iterable W))
6. cartesian(rdd) - cartesian product of two datasets -> (K1,V1)&(K2,V2) -> ((K,V),(K,V)) 
7. coalesce - Decrease the no. of partitions.
8. repartition - Modify the no. of partitions either by increasing or decreasing

Actions:-
reduce(), collect(), count(), countByKey(), take(), saveAsTextFile()

Transformations that trigger shuffle:-
1. reduceByKey
2. groupByKey
3. join
4. cogroup
5. repartition
6. coalesce
'''
##############################################################################################

#-----------------------------------------------------------------------------------------------
# PairRDD "mapValues" transformation
# mapValues operates on the value only (the second part of the tuple),
# while map operates on the entire record (tuple of key and value).
#-----------------------------------------------------------------------------------------------
# mapvaluesRDD = pairRDD.mapValues(lambda x: (x.split(',')[2], x.split(',')[4]))
# for i in mapvaluesRDD.take(5):
#     print(i)


#-----------------------------------------------------------------------------------------------
# Aggregation transformations - use Car Sales Data
#-----------------------------------------------------------------------------------------------
carRDD = \
sc.textFile("/Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/car_sales_data.csv")


#?? QNS 1 >>> Find the top 10 product that has the highest occurance in file
#---------------------------------------------------------------------------
# carKVRdd = carRDD.map(lambda x: (x.split(',')[3],x))
# carKVRdd = carRDD.keyBy(lambda x: x.split(',')[3])
# carKVRdd2 = carKVRdd.groupByKey()
# carKVRdd3 = carKVRdd2.map(lambda x: (x[0], len(list(x[1]))))
# sortedKVRdd = carKVRdd3.sortBy(lambda x: x[1],ascending=False)
#
# for i in sortedKVRdd.take(10):
#     print(i)


#?? QNS 2 >>> Which product was sold the most by Quantity - find top 5
# --------------------------------------------------------------------
# def convert_to_int(record):
#     try:
#         x = record[1]
#         x = int(x)
#         return x
#     except ValueError:
#         pass
#
# def add_quantity_sold(x,y):
#     x = int(x)
#     y = int(y)
#     return (x + y)
#
# carKvRdd = carRDD.map(lambda x: (x.split(',')[3],x.split(',')[5]))
# carKvRdd2 = carKvRdd.filter(lambda x: convert_to_int(x))
# carKvRdd3 = carKvRdd2.reduceByKey(lambda x,y: add_quantity_sold(x,y))
# carKvRdd31 = carKvRdd3.map(lambda x: (x[0], int(x[1])))
# carKvRdd4 = carKvRdd31.sortBy(lambda x: x[1], ascending=False)
#
# for i in carKvRdd4.take(5):
#     print(i)


#?? QNS 3 >>> Who are the product manufacturers
# ---------------------------------------------
# carKvRdd = carRDD.map(lambda x: x.split(',')[6])
# carKvRdd2 = carKvRdd.distinct()
# print('Total unique products: ',carKvRdd2.count())
#
# for i in carKvRdd2.collect():
#     print(i)


#?? QNS 4 >>> Which model was sold in which country the most - top 25
# -------------------------------------------------------------------
# def convert_to_int(record):
#     x = record[0]
#     y = record[1]
#
#     try:
#         y = int(y)
#         return (x,y)
#     except ValueError:
#         pass
#
# carPairRdd = carRDD.map(lambda x: (x.split(',')[3],x.split(',')[5],x.split(',')[11]))
# carPairRdd2 = carPairRdd.keyBy(lambda x: (x[0],x[2]))
# carPairRdd3 = carPairRdd2.map(lambda x:(x[0],x[1][1]))
# carPairRdd4 = carPairRdd3.filter(lambda x: convert_to_int(x))
# carPairRdd5 = carPairRdd4.map(lambda x: (x[0], int(x[1])))
#
# totQuantRdd = carPairRdd5.reduceByKey(lambda x,y: x+y)
# totQuantRddSorted = totQuantRdd.sortBy(lambda x: x[1],ascending=False)
#
# for i in totQuantRddSorted.take(25):
#     print(i)


#?? QNS 5 >>> Statewise sale figure in each country
# -------------------------------------------------
def remove_non_state_countries(record):
    state = record[1]

    if (len(state)) > 0:
        return record
    else:
        pass

carNewRdd = carRDD.map(lambda x: (x.split(',')[5], x.split(',')[10], x.split(',')[11]))
carNewRdd2 = carNewRdd.filter(lambda x: remove_non_state_countries(x))

carPairRdd =

for i in carNewRdd2.take(10):
    print(i)

#?? QNS 6 >>> Gender-wise distribution of Product Manufacturers
#-------------------------------------------------------------



#?? QNS 7 >>> Details of Car make, Product Name and Total Quantity of the oldest car
#---------------------------------------------------------------------------------



#?? QNS 8 >>> Distribution of colors across Product Names
#------------------------------------------------------


#?? QNS 9 >>> Find coutries and their currencies where cars are sold
#-------------------------------------------------------------------



#?? QNS 10 >>> Which credit has been used the most
#-------------------------------------------------



#?? QNS 11 >>> Country, State and Region wise sale figure
#--------------------------------------------------------


#?? QNS 12 >>> Total sales person in the company
#-----------------------------------------------


#?? QNS 13 >>> Given the sales person id, find his/her sale credentials
#-----------------------------------------------------------------------




#-----------------------------------------------------------------------------------------------
# Aggregation transformations - use Plant Data (JSON)
#-----------------------------------------------------------------------------------------------
plantRDD = \
sc.textFile('file:///Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/plant_data.csv')


#?? QNS 1 >>> which is the most occuring plant family
#----------------------------------------------------


#?? QNS 2 >>> Plant and Country wise distribution
#------------------------------------------------


#?? QNS 3 >>> Find location (state) of the most plant found in a country
#-----------------------------------------------------------------------



#?? QNS 4 >>> Find the occurance of plant name, plant family and scientific name combination
#-------------------------------------------------------------------------------------------




#-----------------------------------------------------------------------------------------------
# Join transformations - use Emp and Dept Data files
#-----------------------------------------------------------------------------------------------
empRDD = \
sc.textFile('file:///Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/emp_data.csv')

deptRDD = \
sc.textFile('file:///Users/soumyadeepdey/HDD_Soumyadeep/TECHNICAL/Training/Intellipaat/PySparkCodes/sampledata/dept_data.csv')

#?? QNS 1 >>>