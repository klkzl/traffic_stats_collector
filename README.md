# traffic_stats_collector

## tcpdump

Catches internet traffic on a predefined port and generates the traffic file which contains IP traffic information.
Created files are .txt files of a predefined size, numbered in an ascending order. If files of a predefined name appear in the dedicated folder, acquireing of the traffic has been successful.

This data has to be copied from your (target) Debian machine to where you want to process your traffic, into a dedicated folder.
<br>
## main program

The main program contains three functions for reading data, processing data and uploading the data to a database for best readability for a user.
<br>
#### Reading data:

```
directory_function()
```
takes as a parameter a user defined directory.

It allows for looking through the contents of directory for traffic files, extracting the data and providing viable output for further parsing.
<br>
#### Processing data:

```
extract_function()
```
takes as a parameter a traffic file.

It sorts the data within the file into one second intervals, gives them a time stamp, extracts the information about the protocol, ammount of traffic in bytes within a given second and number of messages exchanged using that protocol within the aggregated time.
The processing function prepares the data in a format that can be easily uploaded to a database.
<br>
#### Uploading the data to a database:

```
init_db()
```
creates a database, if a database does not exist.

```
add_record()
```
takes as a parameter a list of arguments prepared by the processing data function.

Database column are the protocol data obtained previously, sorted into records by timestamp (divided by second), containing data on the protocol, the amount of traffic (size in bytes) and the total number of messages exchanged within that second.
<br><br>
#### In case of problems:

The program should upload the data to the database. If it does not happen, check if correct directory name has been provided. Check if the directory contains the traffic files and make sure that during copying the data it did not become corrupted.
