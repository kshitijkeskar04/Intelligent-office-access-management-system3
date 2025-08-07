import os
import mysql.connector
from mysql.connector import errorcode

# --- Securely get credentials from environment variables ---
DB_HOST = "office-access-db.cvi6c0e4ckud.ap-south-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = os.getenv("DB_PASSWORD") # Reads the variable you set in the terminal
DB_NAME = "employee_db"

# 🔑 Check if the password was found in the environment
if not DB_PASSWORD:
    print(" FATAL ERROR: The DB_PASSWORD environment variable is not set.")
    print("Please set it in your terminal before running the script.")
    exit() # Stop the script if the password is not available

try:
    # --- Step 1: Connect to the MySQL server ---
    db_connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD # Use the variable from the environment
    )
    cursor = db_connection.cursor()
    print(" Connected to RDS instance.")

    # --- The rest of your script remains the same ---
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print(f"Database '{DB_NAME}' is ready.")
    
    cursor.execute(f"USE {DB_NAME}")
    print(f"Switched to database '{DB_NAME}'.")

    print("\nTables in the database:")
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    if not tables:
        print("(No tables found yet)")
    else:
        for table in tables:
            print(f"- {table[0]}")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" Access Denied: Something is wrong with your user name or password.")
    else:
        print(f" An error occurred: {err}")
finally:
    if 'db_connection' in locals() and db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print("\n Database connection closed.")