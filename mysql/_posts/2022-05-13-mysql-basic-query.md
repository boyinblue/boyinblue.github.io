---
title: mySQL 기본 명령어 정리
description: mySQL 기본적인 명령어를 기록해두는 페이지입니다.
---


mySQL 기본 명령어 정리
===


mySQL 기본적인 명령어를 기록해두는 페이지입니다.


### mySQL 설치 방법


Ubuntu Linux 기준으로 설명드립니다. 


```bash
$ sudo apt-get install mysql-server mysql-client
```


만약 php와 연동하기 위해서는 <code>php-mysql</code> 패키지도 설치합니다. 


```bash
$ sudo apt-get install 
```


### mySQL 서비스 동작 상태 확인


설치가 정상적으로 되었다면, 서비스가 정상적으로 돌아야 합니다.


```bash
$ sudo service mysql status
```


<code>sudo service mysql status</code> 명령을 실행했을 때, 
아래와 같이 <code>active (running)</code>으로 상태가 표시되어야 합니다. 


![mysql 서비스가 정상적으로 실행중인 상태](/assets/images/mysql-service-is-running-well.png)


### mySQL 콘솔 접속 방법


<code>sudo mysql -uroot -p</code> 명령으로 mySQL 콘솔에 접속을 합니다. 
*반드시 sudo 권한으로 실행해야 합니다.* 
그렇지 않으면 아래와 같이 <code>ERROR 1698 (28000)</code> 에러가 뜹니다. 


```
$ mysql -uroot -p
Enter password: 
ERROR 1698 (28000): Access denied for user 'root'@'localhost'
```


mySQL 콘솔에 정상적으로 접속이 되면 
<code>mysql\></code> 프롬프트가 표시됩니다. 


### SQL 쿼리시에 주의할 점


*SQL 쿼리는 <code>;</code>로 끝나야 합니다.*
세미콜론을 입력하지 않고 엔터키를 누르면 
SQL은 쿼리가 계속되는지 알고 개행된 상태로 쿼리를 계속 받게 됩니다. 


이 점에 유의하시기 바랍니다. 


### 데이터베이스 목록 조회


<code>mysql\></code> 프롬프트에 <code>show databases;</code>를 입력하면 
데이터베이스 목록을 조회할 수 있습니다. 


```sql
mysql> show databases;
```


아래와 같이 실행 결과가 나옵니다. 


```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| wordpress          |
+--------------------+
5 rows in set (0.01 sec)
```


### 데이베이스 선택


<code>use</code> 명령을 통해서 데이터베이스를 선택할 수 있습니다. 
만약, wordpress라는 데이터베이스에 접속하려면 
<code>use wordpress;</code>와 같이 명령을 실행하면 됩니다. 


```sql
mysql> use wordpress;
```


wordpress라는 데이터베이스가 선택되었습니다. 


만약 데이터베이스를 선택하지 않은 상태에서 테이블을 살펴보면, 
<code>ERROR 1046 (3D000)</code> 에러가 발생하게 됩니다. 


```sql
mysql> show tables;
ERROR 1046 (3D000): No database selected
```


### 테이블을 출력하는 쿼리


사용할 DB를 선택했다면, 이번에는 테이블 목록을 살펴볼 차례입니다. 


<code>show tables;</code> 명령으로 데이터베이스 내부에 
어떤 테이블들이 있는지 살펴볼 차례입니다. 


```sql
mysql> show tables;
+-----------------------+
| Tables_in_wordpress   |
+-----------------------+
| wp_commentmeta        |
| wp_comments           |
| wp_links              |
| wp_options            |
| wp_postmeta           |
| wp_posts              |
| wp_term_relationships |
| wp_term_taxonomy      |
| wp_termmeta           |
| wp_terms              |
| wp_usermeta           |
| wp_users              |
+-----------------------+
12 rows in set (0.01 sec)
```


위와 같이 데이터베이스 내부의 테이블들이 표시됩니다. 


### 테이블의 모든 내용을 출력하는 명령


가장 기본이되는 <code>select</code> 명령이 등장할 차례입니다. 


```sql
mysql> select * from wp_users;
+----+------------------------+------------------------------------+-----------------------+-----------------------+----------------------------+---------------------+---------------------+-------------+------------------------+
| ID | user_login             | user_pass                          | user_nicename         | user_email            | user_url                   | user_registered     | user_activation_key | user_status | display_name           |
+----+------------------------+------------------------------------+-----------------------+-----------------------+----------------------------+---------------------+---------------------+-------------+------------------------+
|  1 | esregnet0409@gmail.com | ################################## | esregnet0409gmail-com | esrgnet0409@gmail.com | https://www.dhqhrtnwl.shop | 2022-05-12 07:14:10 |                     |           0 | esregnet0409@gmail.com |
+----+------------------------+------------------------------------+-----------------------+-----------------------+----------------------------+---------------------+---------------------+-------------+------------------------+
1 row in set (0.01 sec)
```


모든 데이터가 출력되기 때문에 필요한 항목들만 선택해서 출력할 수 있습니다. 


### 컬럼을 조회하는 쿼리


<code> show columns from wp_users; </code> 쿼리를 통해서 
컬럼 정보를 조회할 수 있습니다. 


```sql
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
10 rows in set (0.01 sec)
```


### 특정 항목만 선택해서 출력하는 쿼리


위에서 조회한 컬럼 목록에서 필요한 항목들만 선택해서 조회할 수 있습니다. 


<code>select user_login, user_email from wp_users;</code> 명령처럼 
필요한 항목들만 선택해서 출력도 가능합니다. 


```
mysql> select user_login, user_email from wp_users;
+------------------------+-----------------------+
| user_login             | user_email            |
+------------------------+-----------------------+
| esregnet0409@gmail.com | esrgnet0409@gmail.com |
+------------------------+-----------------------+
1 row in set (0.00 sec)
```


### 테이블 수정하는 방법


위의 레코드에서 user_email 항목에 오타가 발견되었습니다. 
수정을 위해서는 <code>update</code> 쿼리를 사용하면 됩니다. 


```sql
mysql> update wp_users set user_email = "esregnet0409@gmail.com"
    -> where user_email = "esrgnet0409@gmail.com";
Query OK, 1 row affected (0.07 sec)
```


세미콜론을 입력하지 않으면 쿼리를 계속 입력할 수 있기 때문에 
쿼리가 길어질 때는 여러줄로 표시할 수 있어서 편리합니다. 


다시 <code>select 구문</code>을 사용하여 
제대로 업데이트 되었는지 확인합니다.


```
mysql> select user_login, user_email from wp_users;
```


### mySQL 콘솔 종료 방법


<code>quit;</code> 명령을 입력하면 mySQL 콘솔을 종료시킬 수 있습니다. 



