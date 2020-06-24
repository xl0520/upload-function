def get_test_connection():
    import sqlalchemy
    from sqlalchemy import create_engine

    db_connect = "mysql+mysqldb://test:1234567@localhost/dc"
    engine = create_engine(db_connect, echo = True)
    return engine


def upload_doc_string_to_mysql(title = None, Path_ = None, Parent_landing_page_path = None, Landing_page_path = None, Repository_path = None, Github_repository_path = None, Short_description = None, Long_description = None, Long_description_html = None, technical_description = None, databases_used = None, technical_databases_used = None, created_by = None, maintained_by = None, maintained_by_backup = None):
    test_con = get_test_connection()

    if title == None:
        raise ValueError("title cannot be None")
    else:
        title = str(title)
        Path_ = str(Path_)
        Parent_landing_page_path = str(Parent_landing_page_path)
        Landing_page_path = str(Landing_page_path)
        Repository_path = str(Repository_path)
        Github_repository_path = str(Github_repository_path)
        Short_description = str(Short_description)
        Long_description = str(Long_description)
        Long_description_html =str(Long_description_html)
        technical_description = str(technical_description)
        databases_used = str(databases_used)
        technical_databases_used = str(technical_databases_used)
        created_by = str(created_by)
        maintained_by = str(maintained_by)
        maintained_by_backup = str(maintained_by_backup)
        
        
        con = test_con.connect()
        sql_upload = """
            insert into test values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = (title, Path_, Parent_landing_page_path, Landing_page_path, Repository_path, Github_repository_path, Short_description, Long_description, Long_description_html, technical_description, databases_used, technical_databases_used, created_by, maintained_by, maintained_by_backup)
        con.execute(sql_upload)


upload_doc_string_to_mysql(title = follow_app, Path_ = None, Parent_landing_page_path = None, Landing_page_path = None, Repository_path = None, Github_repository_path = https://github.com/dexcom-inc/Customer-Advocacy-Searches/blob/master/Library/Complaints/follow_app.py, Short_description = Testing, Long_description = None, Long_description_html = None, technical_description = None, databases_used = customer_advocacy_pms, technical_databases_used = None, created_by = Thomas McGinn, maintained_by = Thomas McGinn, maintained_by_backup = None)

