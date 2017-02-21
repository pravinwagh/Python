
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

import sqlite3


# In[3]:

create_table = """
CREATE TABLE student_score
(Id INTEGER, Name VARCHAR(20), Math REAL, Science REAL);"""


# In[4]:

executeSQL = sqlite3.connect(':memory:')
executeSQL.execute(create_table)
executeSQL.commit()


# In[5]:

SQL_query = executeSQL.execute('select * from student_score')


# In[6]:

resultset = SQL_query.fetchall()


# In[7]:

resultset


# In[8]:

insertSQL = [(10,'Jack',85,92),
            (29,'Tom',73,89),
             (65,'Ram',65.5,77),
             (5,'Steve',55,91)
            ]


# In[9]:

insert_statement = "Insert into student_score values(?,?,?,?)"
executeSQL.executemany(insert_statement,insertSQL)
executeSQL.commit()


# In[13]:

SQL_query = executeSQL.execute('select * from student_score')
resultset = SQL_query.fetchall()


# In[14]:

resultset
