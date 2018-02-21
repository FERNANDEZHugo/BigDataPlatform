echo "First we launch our data :"
hadoop fs -mkdir input
wget http://www.textfiles.com/etext/FICTION/defoe-robinson-103.txt
hadoop fs -copyFromLocal defoe-robinson-103.txt input
wget http://www.textfiles.com/etext/FICTION/callwild
hadoop fs -copyFromLocal callwild input

echo "Then we run our first map reduce job that will count word for Callwild then for Defoe with MapReduce"

hadoop jar /home/hugo/Logiciel/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar \
-file /home/hugo/Logiciel/mapper.py    -mapper /home/hugo/Logiciel/mapper.py \
-file /home/hugo/Logiciel/reducer.py   -reducer /home/hugo/Logiciel/reducer.py \
-input /user/hugo/input/callwild -output /user/hugo/output1/out-call.txt

hadoop jar /home/hugo/Logiciel/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar \
-file /home/hugo/Logiciel/mapper.py    -mapper /home/hugo/Logiciel/mapper.py \
-file /home/hugo/Logiciel/reducer1_2.py   -reducer /home/hugo/Logiciel/reducer1_2.py \
-input /user/hugo/input/defoe-robinson-103.txt -output /user/hugo/output1/out-defoe.txt

echo "Then we compute the frequency of the word and it's number of occurence in the corpus with MapReduce"

hadoop jar /home/hugo/Logiciel/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar \
-file /home/hugo/Logiciel/mapper2.py    -mapper /home/hugo/Logiciel/mapper2.py \
-file /home/hugo/Logiciel/reducer2.py   -reducer /home/hugo/Logiciel/reducer2.py \
-input /user/hugo/output1/* -output /user/hugo/output2

echo "Finally we compute the TF-IDF for both text with MapReduce"

hadoop jar /home/hugo/Logiciel/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar \
-file /home/hugo/Logiciel/mapper3.py    -mapper /home/hugo/Logiciel/mapper3.py \
-file /home/hugo/Logiciel/reducer3.py   -reducer /home/hugo/Logiciel/reducer3.py \
-input /user/hugo/output2/* -output /user/hugo/output3

hdfs dfs -get /user/hugo/output3/part-00000 output.csv

echo "We print the 20 words that have the highest TF-IDF score for each document:"

python result.py