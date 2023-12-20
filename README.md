# Intrusion Detection System
This is a project to create an IDS using Machine Learning. 
The algorithms used here are Decision Tree and Random Forest

## Dataset
The dataset used here is [UNSW-NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset)  
## Dataset Information
This dataset consists of four CSV files containing data records, with each file encompassing both attack and normal records:

| File Name        | File Size    | Number of Records | Number of Features |
|------------------|--------------|-------------------|--------------------|
| UNSWNB15_1.csv   | 165.02 MB    | 700,000           | 49                 |
| UNSWNB15_2.csv   | 161.349 MB   | 700,000           | 49                 |
| UNSWNB15_3.csv   | 150.965 MB   | 700,000           | 49                 |
| UNSWNB15_4.csv   | 95.302 MB    | 440,044           | 49                 |

## Dataset Features

The dataset comprises 49 features, categorized into three different datatypes:

### Categorical Features:
- `proto`: Transaction protocol
- `state`: State and its dependent protocol
- `service`: Type of service (e.g., http, ftp, smtp, ssh, dns, ftp-data, irc)
- `attack_cat`: The name of each attack category

### Binary Features:
- `is_sm_ips_ports`: Binary indicator if source and destination IP addresses are equal and port numbers are equal
- `is_ftp_login`: Binary indicator if the FTP session is accessed by user and password

### Numerical Features:
- The rest of the features are numerical in nature, representing various aspects of network transactions.

##Feature

| #   | Feature             | Type      | Description                                                         |
| --- | ------------------- | --------- | ------------------------------------------------------------------- |
| 1   | srcip               | nominal   | Source IP address                                                   |
| 2   | sport               | integer   | Source port number                                                  |
| 3   | dstip               | nominal   | Destination IP address                                              |
| 4   | dsport              | integer   | Destination port number                                             |
| 5   | proto               | nominal   | Transaction protocol                                                |
| 6   | state               | nominal   | Indicates the state and its dependent protocol                      |
| 7   | dur                 | Float     | Record total duration                                               |
| 8   | sbytes              | Integer   | Source to destination transaction bytes                             |
| 9   | dbytes              | Integer   | Destination to source transaction bytes                             |
| 10  | sttl                | Integer   | Source to destination time to live value                             |
| 11  | dttl                | Integer   | Destination to source time to live value                            |
| 12  | sloss               | Integer   | Source packets retransmitted or dropped                             |
| 13  | dloss               | Integer   | Destination packets retransmitted or dropped                        |
| 14  | service             | nominal   | HTTP, FTP, SMTP, SSH, DNS, FTP-data, IRC, (-) if not much used service|
| 15  | Sload               | Float     | Source bits per second                                              |
| 16  | Dload               | Float     | Destination bits per second                                         |
| 17  | Spkts               | Integer   | Source to destination packet count                                  |
| 18  | Dpkts               | Integer   | Destination to source packet count                                  |
| 19  | swin                | Integer   | Source TCP window advertisement value                               |
| 20  | dwin                | Integer   | Destination TCP window advertisement value                          |
| 21  | stcpb               | Integer   | Source TCP base sequence number                                      |
| 22  | dtcpb               | Integer   | Destination TCP base sequence number                                  |
| 23  | smeansz             | Integer   | Mean of the flow packet size transmitted by the source              |
| 24  | dmeansz             | Integer   | Mean of the flow packet size transmitted by the destination         |
| 25  | trans_depth         | Integer   | Represents the pipelined depth into the connection of HTTP request/response transaction|
| 26  | res_bdy_len         | Integer   | Actual uncompressed content size of the data transferred from the server's HTTP service|
| 27  | Sjit                | Float     | Source jitter (mSec)                                                |
| 28  | Djit                | Float     | Destination jitter (mSec)                                           |
| 29  | Stime               | Timestamp | Record start time                                                   |
| 30  | Ltime               | Timestamp | Record last time                                                    |
| 31  | Sintpkt             | Float     | Source interpacket arrival time (mSec)                              |
| 32  | Dintpkt             | Float     | Destination interpacket arrival time (mSec)                         |
| 33  | tcprtt              | Float     | TCP connection setup round-trip time, the sum of 'synack' and 'ackdat'|
| 34  | synack              | Float     | TCP connection setup time, the time between the SYN and the SYN_ACK packets|
| 35  | ackdat              | Float     | TCP connection setup time, the time between the SYN_ACK and the ACK packets|
| 36  | is_sm_ips_ports     | Binary    | If source (1) and destination (3) IP addresses equal and port numbers (2)(4) equal then, this variable takes value 1 else 0|
| 37  | ct_state_ttl        | Integer   | No. for each state (6) according to a specific range of values for source/destination time to live (10) (11)|
| 38  | ct_flw_http_mthd    | Integer   | No. of flows that has methods such as Get and Post in HTTP service  |
| 39  | is_ftp_login        | Binary    | If the FTP session is accessed by user and password then 1 else 0    |
| 40  | ct_ftp_cmd          | Integer   | No. of flows that has a command in FTP session                       |
| 41  | ct_srv_src          | Integer   | No. of connections that contain the same service (14) and source address (1) in 100 connections according to the last time (26)|
| 42  | ct_srv_dst          | Integer   | No. of connections that contain the same service (14) and destination address (3) in 100 connections according to the last time (26)|
| 43  | ct_dst_ltm          | Integer   | No. of connections of the same destination address (3) in 100 connections according to the last time (26)|
| 44  | ct_src_ltm          | Integer   | No. of connections of the same source address (1) in 100 connections according to the last time (26)|
| 45  | ct_src_dport_ltm    | Integer   | No. of connections of the same source address (1) and the destination port (4) in 100 connections according to the last time (26)|
| 46  | ct_dst_sport_ltm    | Integer   | No. of connections of the same destination address (3) and the source port (2) in 100 connections according to the last time (26)|
| 47  | ct_dst_src_ltm      | Integer   | No. of connections of the same source (1) and the destination (3) address in 100 connections according to the last time (26)|
| 48  | attack_cat          | nominal   | The name of each attack category                                    |
| 49  | Label               | binary    | 0 for normal and 1 for attack records                               |

##Attack Cat
| Attack Category   | Occurrences |
|-------------------|-------------|
| Generic           | 193,696     |
| Exploits          | 40,112      |
| Fuzzers           | 21,920      |
| DoS               | 14,723      |
| Reconnaissance    | 12,624      |
| Analysis          | 2,400       |
| Backdoor          | 2,103       |
| Shellcode         | 1,359       |
| Worms             | 156         |
## ML Problem Formulation

#### Binary classification of attack category
In this dataset, the "label" column contains values of 0 and 1, where 0 represents normal (non-attack) and 1 represents an attack (anomaly). The goal is to use the available features to predict whether a given data point belongs to the attack or non-attack category.
