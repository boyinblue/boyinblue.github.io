---
title: mysql 컬럼 목록 조회 쿼리
description: mysql 컬럼 목록을 살펴보는 방법에 대해서 설명합니다.
---


mysql 컬럼 목록 조회 쿼리
===


mysql 컬럼 목록을 살펴보는 방법에 대해서 설명합니다.


### mysql 컬럭 목록을 간략하게 살펴보는 쿼리


<code>show columns from TABLE_NAME;</code> 명령을 통해서 
컬럼 목록을 조회할 수 있습니다. 


쿼리의 마지막은 반드시 세미콜론으로 끝나야 합니다.


```
mysql> show columns from wp_users;
+---------------------+-----------------+------+-----+---------------------+----------------+
| Field               | Type            | Null | Key | Default             | Extra          |
+---------------------+-----------------+------+-----+---------------------+----------------+
| ID                  | bigint unsigned | NO   | PRI | NULL                | auto_increment |
| user_login          | varchar(60)     | NO   | MUL |                     |                |
| user_pass           | varchar(255)    | NO   |     |                     |                |
| user_nicename       | varchar(50)     | NO   | MUL |                     |                |
| user_email          | varchar(100)    | NO   | MUL |                     |                |
| user_url            | varchar(100)    | NO   |     |                     |                |
| user_registered     | datetime        | NO   |     | 0000-00-00 00:00:00 |                |
| user_activation_key | varchar(255)    | NO   |     |                     |                |
| user_status         | int             | NO   |     | 0                   |                |
| display_name        | varchar(250)    | NO   |     |                     |                |
+---------------------+-----------------+------+-----+---------------------+----------------+
10 rows in set (0.00 sec)
---


위에서 확인한 컬럼명으로 필요한 컬럼만 골라서 출력할 수 있습니다. 


### 필요한 컬럼만 조회하는 방법


```sql
mysql> select id, user_login from wp_users;
+----+------------------------+
| id | user_login             |
+----+------------------------+
|  1 | esregnet0409@gmail.com |
+----+------------------------+
1 row in set (0.00 sec)
```



