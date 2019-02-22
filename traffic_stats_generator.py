from traffic_stats_mysql import init_db, add_record, insert_records
from traffic_stats_files import directory_function, extract_function

# init_db()

# answer = input("Please provide directory with statistic files:\n")

filelist = directory_function('C:/Users/kkoziel/Documents/Python/capstone/test2/')
# print(filelist)
z = len(filelist)

for i in range(0,z):
    my_path = 'C:/Users/kkoziel/Documents/Python/capstone/test2/' + filelist[i]
    my_list = []
    my_list = extract_function(my_path)
    insert_records(my_list)
