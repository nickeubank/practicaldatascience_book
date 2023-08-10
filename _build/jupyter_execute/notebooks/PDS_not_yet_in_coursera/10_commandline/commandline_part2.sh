# Normal `ls` display:
cd ~/github/practicaldatascience/Example_Data/command_line
ls

# With the `-l` flag, it also shows file sizes, when last modified, and all sorts of operating
# system information that you don't need to worry about. 
ls -l

# You can use these separately 
ls -l -h

# Or together!
ls -lh

# You thought you knew what was in this folder:
ls -l

# But there was another file hiding! Notice that `.this_file_is_invisible.txt` and `.DS_Store` were hidden before? 
ls -la

cd example_csvs
ls *.csv

ls *2018_2*

ls *2018_1*

ls -1 *.csv

ls -1 *.csv > ~/files_in_folder.txt
wc -l ~/files_in_folder.txt

ls -1 | wc -l

echo $PATH

export PATH="/NEW/FOLDER/ON/PATH:$PATH"
