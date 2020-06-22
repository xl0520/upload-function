import mysql.connector

# It can be put in the follow_app.py file or search.py file(the parent class) for using. 
def upload_to_DCtest(self):
    # I created a db on server called DCtest, now I want to connect to the db.
    mydb = mysql.connector.connect(
    host = '172.19.41.99',
    port = 3306,
    user = 'root',
    password = '*7CF3B132713D48DCED3D735CDF2C13E671F359C3', 
    database = 'DCtest' 
    )
    # I cannot actually get connection from local in this way, I want more help about this part(I think probably the value for host, 
    # port, user and password is wrong here). I saw you use sqlalchemy and pyodbc  
    # in utility.py file to get connection to some db like customer advocacy and reliance prod, while I don't use these much, should I
    # wirte a connection funtion imitate your connection function like get_customer_advocacy_connection in utility.py to get connection
    # to my db? I googled it but still a bit confused about how do you create engine(the url part). 
    
    mycursor = mydb.cursor()
    
    Title = ''.join(self.title) #''.join for converting the data type from list to string
    Path_ = "" #I don't find this part in the follow_app.py file 
    Parent_landing_page_path = ''.join(self.sharepoint_folder_url)
    Landing_page_path = ''.join(self.sharepoint_site_url)
    Repository_path = ""
    Github_repository_path = ''.join(self.report_location)
    Short_description = ''.join(self.description)
    Long_description = ""
    Long_description_html = ""
    technical_description = ""
    databases_used = ''.join(self._databases_needed)
    technical_databases_used = ""
    created_by = __author__
    maintained_by = __maintainer__
    maintained_by_backup = ""

    # I created a table called test in DCtest db and I want to put records there. Every time this function is called, new record of 
    # different data file would be added into this table. Finally this table would collect info for all data files. 
    sql  = """
    INSERT INTO test 
    VALUES (
        TestID,
        Title,
        Path_,
        Parent_landing_page_path,
        Landing_page_path,
        Repository_path,
        Github_repository_path,
        Short_description,
        Long_description,
        Long_description_html,
        technical_description,
        databases_used,
        technical_databases_used,
        created_by,
        maintained_by,
        maintained_by_backup
    )
    """
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")






