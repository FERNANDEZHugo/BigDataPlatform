echo "First we launch the data"

hdfs dfs -put arbres.csv


echo "Then we run a map reduce job that will done the 3 jobs asked :"

hadoop jar /home/hugo/Logiciel/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar \
-file /home/hugo/Logiciel/arbre_mapper2.py    -mapper /home/hugo/Logiciel/arbre_mapper2.py \
-file /home/hugo/Logiciel/arbre_reducer2.py   -reducer /home/hugo/Logiciel/arbre_reducer2.py \
-input /user/hugo/arbres.csv -output /user/hugo/output1/

echo "Then we extract our resulta in the file Result.txt"

hdfs dfs -get /user/hugo/output1/part-00000 Result.txt

