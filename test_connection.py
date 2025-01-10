import pyodbc

def test_sql_connection():
    # Connection string
    conn_str = (
        "Driver={SQL Server};" 
        "Server=SPCDMSQL-NEW\CDMGDATAREPORTS;"
        "Database=CDMGdata;"
        "UID=cdmgreporting.sql;"
        "PWD=Clouds#473builDings;"
    )
    
    try:
        # Attempt connection
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        # Simple test query
        cursor.execute("SELECT @@version")
        row = cursor.fetchone()
        print("Connection successful!")
        print("Server version:", row[0])
        
        # Clean up
        cursor.close()
        conn.close()
        return True
        
    except pyodbc.Error as e:
        print("Connection failed!")
        print("Error:", str(e))
        return False

if __name__ == "__main__":
    test_sql_connection()