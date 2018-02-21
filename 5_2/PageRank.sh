echo "Copy file from local"

hdfs dfs -copyFromLocal soc-Epinions1.txt /user/hugo

echo "Run the first map_reduce job"
hadoop jar /home/hugo/Logiciel/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar \
-file /home/hugo/Logiciel/PRmapper1.py    -mapper /home/hugo/Logiciel/PRmapper1.py  \
-file /home/hugo/Logiciel/PRreducer1.py   -reducer /home/hugo/Logiciel/PRreducer1.py \
-input /user/hugo/soc-Epinions1.txt  -output /user/hugo/output1

echo "Upload the Ranks 20 times with MapReduce"


for ((k=1;k<=20;k++)); do
    
    
    
    j=$[$k+1]
    echo "$k / 20, $j"
    hadoop jar /home/hugo/Logiciel/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar \
	-file /home/hugo/Logiciel/PRmapper2.py    -mapper /home/hugo/Logiciel/PRmapper2.py  \
	-file /home/hugo/Logiciel/PRreducer2.py   -reducer /home/hugo/Logiciel/PRreducer2.py \
	-input /user/hugo/output$k/* -output /user/hugo/output$j
    
done

echo "We use a last Map reduce job which sort only the pair node pagerank"
hadoop jar /home/hugo/Logiciel/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar \
-file /home/hugo/Logiciel/PRmapper2.py    -mapper /home/hugo/Logiciel/PRmapper2.py  \
-file /home/hugo/Logiciel/PRreducer3.py   -reducer /home/hugo/Logiciel/PRreducer3.py \
-input /user/hugo/output21/* -output /user/hugo/output22

echo "We extract the result and sort it"

hdfs dfs -get /user/hugo/output22/part-00000 pagerank.csv

python Rank.py
