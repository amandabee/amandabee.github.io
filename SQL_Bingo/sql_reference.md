#SQL Quick Reference Guide
##Statements 

    SELECT [ DISTINCT ] * | LIST OF COLUMNS, FUNCTIONS, CONSTANTS
       FROM LIST OF TABLES OR VIEWS
       [ WHERE CONDITION(S) ]
       [ ORDER BY ORDERING COLUMN(S) [ ASC | DESC ] ]
       [ GROUP BY GROUPING COLUMN(S) ]
       [ HAVING CONDITION(S) ]
    

    DELETE FROM TABLE NAME
        [ WHERE CONDITION(S) ] 
    
     INSERT INTO TABLE NAME
        [ (COLUMN LIST) ]
        VALUES (VALUE LIST) 

    UPDATE TABLE NAME
        SET COLUMN NAME = VALUE
        [ WHERE CONDITION ]
 

##Functions 

| Function | Purpose                  |
|----------|--------------------------|
| SUM      | Total of the values in a field.
| AVG      | Average of the values in a field. 
| MIN      | Lowest value in a field.
| MAX      | Highest value in a field.
| COUNT    | Number of values in a field, not counting Null (blank) values.

##Predicates 

| Predicate | Description            | 
|-----------|------------------------| | BETWEEN ... AND | Compares a value to a range formed by two values. 
| IN        | Determines whether a value exists in a list of values or a table
| LIKE      | Compares, in part or in whole, one value with another. 
| JOIN      | Joins two tables.

## Data Definition 

    CREATE TABLE TABLE_NAME
        ( COLUMN_NAME DATA_TYPE [(SIZE)] COLUMN_CONSTRAINT,
        [, other column definitions,...]
        [, primary key constraint]
        )
     
    
    ALTER TABLE TABLE_NAME ADD | DROP | MODIFY
        ( COLUMN_NAME DATA_TYPE [(SIZE)] COLUMN_CONSTRAINT,
        [, other column definitions,...]
        )
     
    
    DROP TABLE TABLE_NAME
 

    CREATE [UNIQUE] [ASC | DESC] INDEX INDEX_NAME
        ON TABLE_NAME ( COLUMN_LIST ) 
    
    DROP INDEX INDEX_NAME ON TABLE_NAME 
    
     CREATE VIEW VIEW_NAME AS QUERY_NAME 
    
     CONSTRAINT CONSTRAINT_NAME
         {PRIMARY KEY | UNIQUE | NOT NULL | 
         REFERENCES FOREIGN_TABLE [(FIELD_LIST)]}
     
# Less Quick SQL Reference
From www.phphelp.com

SQL is based on just four functions. The rest are transformations (and some expressions). What is a transformation? Well, anything that just changes the format or type of data to another format or an expression that produces a result based on input. These are the various data type conversion functions, such as date conversion, string conversion, sub string, math functions, conditionals, etc. Only Select, Insert, Update and Delete actually store, affect or retrieve any data. This economy is what makes SQL easy to learn and difficult to master. It is also what makes it a popular language, because like the HTTP protocol it consists of a very few standard operations.

+ SELECT 
+ DELETE 
+ INSERT 
+ UPDATE

##Select
The `SELECT` statement enables you to find and view information contained in tables in a variety of useful ways. You will meet some very complex select statements as you progress in learning SQL, but no matter how complex a `SELECT` statement might appear, they all follow the same basic pattern:

    SELECT select list
    FROM table list
    [WHERE search criteria]
    
    
The select list specifies the column or columns included in the results. The part following the `FROM` statement is called the table list, which specifies the tables information is to be retrieved from. With the optional `WHERE` clause, you choose the rows you want to retrieve based on some conditional search criteria.

The simplest query you can make finds every row of the table and displays values for all columns.

    SELECT * FROM images_of_america_books


The asterisk has special meaning in the select list. It stands for all the column names in all the tables in the table list. Columns are displayed in the same order they were created. Use the asterisk when you want to see all the columns in a table.

We can obtain the same result by naming each column in the select list.

    SELECT title, location FROM images_of_america_books
    

An important use of the select list is to limit the displayed columns to only those named in the select list. The general form follows this pattern:
 
    SELECT column_a, column_b, column_c, . . .
    FROM table_a, table_b, . . .
    

 This probably looks a bit complicated now, because it shows that you can potentially select columns from more than one table at once. That's a very useful thing to do, but you do not have to worry about that now.

This query shows how to use the select list to limit columns retrieved from the table to just those you're interested in. In this example we look at the same table of books. To obtain just the title and location from the information stored about each book in a row, we specify just those two columns.
 
    SELECT title, location FROM images_of_america_books


 **Efficiency Note:**  Asking for only the columns you need makes a select query more efficient. Only mention columns in the select list if you intend to use their values.

     SELECT ColumnName, ColumnName, . . .
     FROM TableName 
    WHERE (Expression, Expression, Expression)
    
Suppose we wish to provide a function where a member who has lost their password can retrieve it from the database in secure manner. This select query finds the password matching an email address submitted by the user through a web form. If the email address exists in the database, the script will send the password to the user's email address. (Note: the quoted values would actually come from form variables).

    SELECT (Password) FROM MemberProfile 
        WHERE EmailAddress = 'someone@this.site' 


Web Application Note: Select is a very efficient query because most SQL servers keep tables open for a period of time after they have been initially opened for a query.

## Delete
    DELETE FROM TableName [WHERE Definition] [LIMIT Rows]

The `DELETE` operator deletes rows from the specified table satisfying the condition given in the `WHERE` definition. It returns the number of rows affected.

    DELETE FROM UserProfile WHERE EmailAddress = 'someone@this.site'


**Caution:**  If you issue a `DELETE` with no `WHERE` clause, all rows are deleted. If you have a mailing list stored in a table and mistakenly issue a `DELETE` operation without a `WHERE` clause, your database will be lost.

For example, this SQl statement deletes all records inclusive of 38 to 44 (greater than or equal to 38 and less than or equal to 44).

    DELETE FROM images WHERE id BETWEEN 38 AND 44;
    Query OK, 7 rows affected (0.01 sec)


**Efficiency Note:**  `DELETE` can be a slow operation.

## Insert
An `INSERT` query inserts a new row into an existing table. Values are inserted into the table either as explicitly specified values or as values resulting from evaluating an expression. The result of the expression becomes the value inserted for a given column.

 The `INSERT` clause may specify column names and expressions separately in a `VALUES` clause, or using a `SET` clause may group column names with their corresponding expressions. (An explicity defined value is a kind of expression too, so we refer to all values in the syntax example as expressions).
 
    INSERT INTO TableName
     ColumnName, ColumnName, . . .
    VALUES( Expression , Expression , Expression )
    
The `INSERT ... SET` form inserts values based on an expression.

    INSERT INTO TableName SET ColumnName  = Expression , 
        ColumnName  = Expression , 
        ColumnName  = Expression , ...


Here, this insert query shows you how to add a new individual to an email distribution list. A web form would accept the name and email address to be inserted into the database. (Note: the quoted values would actually come from form variables).
 
    INSERT (name, email_address) INTO distribution_list 
    VALUES ('Steve Knoblock','knoblock@some.tld')


 **Efficiency Note:**  Using `INSERT` to import a large number of records into a database is inefficient and should be avoided. Use the import/export functions provided. Also, `INSERT`s become progressively slower as the number of indexed columns grows. Each index must be updated when a new row is inserted.

##Update

    UPDATE TableName SET ColumnName, ColumnName, . . . 
    VALUES(Expression, Expression, Expression)

The `UPDATE` operator updates the values in existing table rows. The `SET` clause specifies which columns are modified and what new values they will be given. An optional `WHERE` clause specifies which rows should be updated:

    UPDATE UserProfile SET Name = 'Steve Knoblock' 
    WHERE EmailAddress = 'knoblock@some.tld'


**Caution:**  If no where clause is given, all records in the table for that table are updated and modified. What does this mean? Well, if you wrote `UPDATE mail_list SET email_address = "mickey@mouseclub.com";` it would set every email address in every record in the database to that one address. Ouch! Use extreme caution when running SQL statements like these from the command line. It's easy to forget the WHERE clause irretrievably ruining thousands of records in the blink of an eye. Backup your database before you enter queries on the command line. Be careful when writing update queries in database applications.

**Efficiency Note:**  If you set a column to the same value it currently holds, most SQL servers will notice and not update the column.