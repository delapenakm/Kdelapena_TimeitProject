// README.txt

FILES:
COMP255_Program_Report.pdf - Formal Report of tables and graphs used to analyze the various process times
Timing.ipynb - Jupyter Notebook that has instructions and code on how to run timing experiment
macbookPro_search_results.csv - Data collected from my MacBook used in some of the graphs
Linux_search_results.csv - Data collected from Linux boxes in cS lab, also for some of the graphs in report
test_LinearVSbinarySearch.py - pytesting file
searchFunctions.py - file containing all functions used in pytests

STATUS:
My program appears to be working. I did attempt all parts listed in the spec. Functions used for pytesting are stored in separate file (test_LinearVSbinarySearch.py) to make it easier to not have to install a bunch of things to pytest functions from the Jupyter notebook. All .csv files I used to create graphs and tables are in the folder and have not been edited at all since I used them. CSV files only store Minimum Search Time rather than Average and Maximum search time for the purpose of making it easier on myself to create tables. Average and Maximum search times are still outputted to console. To run the experiment, the code cells setting the variables N, samples, and trials must be ran first. If you do not rerun to change the variables, they will remain the same throughout the experiment.

kmd
09/28/26