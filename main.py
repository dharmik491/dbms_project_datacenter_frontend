import psycopg2
from config import config

conn = psycopg2.connect(
    host="localhost",
    database="201901300_db",
    user="postgres",
    password="admin")

# def 
#     choice = input("Enter your choice")
#         while(choice){
            
#         }
#         print('PostgreSQL database version:')
#         execute_query(cur)
#         conn.commit()
#         # sql = """ SELECT *  FROM  datacenter_db."Data_Center" """
#         # cur.execute(sql)
#         # db_version = cur.fetchone()
#         # print(db_version)

#         # display the PostgreSQL database server version
#         cur.execute(""" SELECT * FROM datacenter_db."Tier" """)

#         db_query = cur.fetchall()
#         for each_row in db_query:
#             print(each_row) ( "Tier_ID", "Cost", "Max_capacity")

# if ty == 1:
#             print("Enter no of row")
#             no_of_entry = int(input())
#             data_lst = [no_of_entry*[]]
#             each_row = []
#             print("Enter the Entry in the Order of: ")
#             print("Tier_ID, Max_capacity, Cost ")
#             for x in range(no_of_entry):
#                 x1,x2,x3 = input().split()
#                 each_row.append(x1)
#                 each_row.append(x2)
#                 each_row.append(x3)
#                 data_lst.append(each_row)
#             cur.executemany(sql,data_lst)
#             print("Done")
#             for x in data_lst:
#                 for i in x:
#                     print(i)
#                 print(" ")

#         elif ty == 2:
            # print("Enter the Entry in the Order of: ")
            # print("Tier_ID, Max_capacity, Cost ")
            # x1,x2,x3 = input().split()
            # cur.execute(sql, (x1,x2,x3))

def show_table_details(cur,table_name):
    sql = "SELECT * FROM datacenter_db." + table_name
    if table_name == '"Tier"' :
        print("(Tier_ID, Max_capacity, Cost )")

    elif table_name == '"Managed_Client"' :
        print("(Client_ID, Client_name, Purchase_date, Time_Period)")

    elif table_name == '"Managed_Client_Contact"':
        print("Client_ID, Country_code, Telephone")

    elif table_name == '"Colocation_User"':
        print("(Cu_ID, Data_center_to_belong, Cu_name, Storage_used, Tier_used, Total_time, Purchase_date)")

    elif table_name == '"Colocation_User_Contact"':
        print("Cu_ID, Cu_contact_details")

    elif table_name == '"Data_Center"' :
        print("(Datacenter_ID, Capacity, Type, Owner_ID, Area)")

    elif table_name == '"Employee"':
        print("(Employee_ID, Employee_name, Salary, Data_center_to_belong, Joining_date, Role, Shift)")

    elif table_name == '"Hardware"' :
        print("(Hardware_ID, Type, Last_maintenance_date, Data_center_to_belong, Maintenence_period)")

    elif table_name == '"Location"' :
        print("(Location_ID, country, Zone, Region)")

    elif table_name == '"Maintenance_log"' :
        print("(Log_ID, Hardware_ID, Employee_ID, Problems, Action_taken, Cost)")

    elif table_name == '"Security_applied"' :
        print("(Data_center_to_belong, No_of_cameras, No_of_personnels, No_of_scanning_devices, X-ray_machines, No_of_Bio_metric_security_devices)")

    elif table_name == '"Software"' :
        print("(Prod_key, S_name, Validity, Purchase_date, Price, Data_center_to_belong, Manufacturer)")

    cur.execute(sql) 
    db_query = cur.fetchall()
    for each_row in db_query:
        print(each_row)


def insert_into_a_table(cur):
    table_name = input("Enter table name:  ")
    print("Sub-Menu:")
    print("1. Single Line Entry")
    print("2. Multi Line Entry")
    ty = int(input("Enter: "))

    if table_name == '"Tier"' : 
        sql = """ INSERT INTO datacenter_db."Tier" VALUES (%s, %s, %s); """
        print("Enter the Entry in the Order of: ")
        print("Tier_ID, Max_capacity, Cost ")
        x1,x2,x3 = input().split()
        cur.execute(sql, (x1,x2,x3))

    elif table_name == '"Managed_Client"' :
        sql = """INSERT INTO datacenter_db."Managed_Client"("Client_ID", "Client_name", "Purchase_date", "Time_Period") VALUES (%s, %s, %s, %s);"""
        print("Enter the Entry in the Order of: ")
        print("Client_ID, Client_name, Purchase_date, Time_Period")
        x1,x2,x3,x4 = input().split()
        cur.execute(sql, (x1,x2,x3,x4))
        sql = """ INSERT INTO datacenter_db."Managed_Client_Contact" ("Client_ID", "Country_code", "Telephone") VALUES (%s, %s, %s);"""
        print("You also have to enter the Contact details of the Managed Client:")
        print("Enter the Entry in the Order of: ")
        print("Client_ID, Country_code, Telephone")
        x1,x2,x3 = input().split()
        cur.execute(sql,(x1,x2,x3))

    elif table_name == '"Colocation_User"':
        sql = """INSERT INTO datacenter_db."Colocation_User"( "Cu_ID", "Data_center_to_belong", "Cu_name", "Storage_used", "Tier_used", "Total_time", "Purchase_date") VALUES (%s, %s, %s, %s, %s, %s, %s);"""
        print("Enter the Entry in the Order of: ")
        print("Cu_ID, Data_center_to_belong, Cu_name, Storage_used, Tier_used, Total_time, Purchase_date")
        x1,x2,x3,x4,x5,x6,x7 = input().split()
        cur.execute(sql, (x1,x2,x3,x4,x5,x6,x7))
        sql = """ INSERT INTO datacenter_db."Colocation_User_Contact"( "Cu_ID", "Cu_contact_details") VALUES (%s, %s); """
        print("You also have to enter the Customer contact details: ")
        x8 = input()
        cur.execute(sql,(x1,x8))

    elif table_name == '"Data_Center"' :
        sql = """ INSERT INTO datacenter_db."Data_Center"( "Datacenter_ID", "Capacity", "Type", "Owner_ID", "Area") VALUES (%s, %s, %s, %s, %s); """
        print("Enter the Entry in the Order of: ")
        print("Datacenter_ID, Capacity, Type, Owner_ID, Area")
        x1,x2,x3,x4,x5 = input().split()
        cur.execute(sql,(x1,x2,x3,x4,x5))

    elif table_name == '"Employee"':
        sql = """ INSERT INTO datacenter_db."Employee"( "Employee_ID", "Employee_name", "Salary", "Data_center_to_belong", "Joining_date", "Role", "Shift") VALUES (%s, %s, %s, %s, %s, %s, %s);"""
        print("Enter the Entry in the Order of: ")
        print("Employee_ID, Employee_name, Salary, Data_center_to_belong, Joining_date, Role, Shift")
        x1,x2,x3,x4,x5,x6,x7 = input().split()
        cur.execute(sql, (x1,x2,x3,x4,x5,x6,x7))

    elif table_name == '"Hardware"' :
        sql = """ INSERT INTO datacenter_db."Hardware"( "Hardware_ID", "Type", "Last_maintenance_date", "Data_center_to_belong", "Maintenance_period") VALUES (%s, %s, %s, %s, %s);"""
        print("Enter the Entry in the Order of: ")
        print("Hardware_ID, Type, Last_maintenance_date, Data_center_to_belong, Maintenence_period")
        x1,x2,x3,x4,x5 = input().split()
        cur.execute(sql,(x1,x2,x3,x4,x5))

    elif table_name == '"Location"' :
        sql = """ INSERT INTO datacenter_db."Location"("Location_ID", country, "Zone", "Region") VALUES (%s, %s, %s, %s);"""
        print("Enter the Entry in the Order of: ")
        print("Location_ID, country, Zone, Region")
        x1,x2,x3,x4 = input().split()
        cur.execute(sql,(x1,x2,x3,x4))
        sql = """ INSERT INTO datacenter_db."Location_Data_center_id"( "Location_ID", "Data_center_to_belong") VALUES (%s, %s);"""
        print("You also have to enter the location contact details:")
        x5 = input("Enter the Data_center_ID")
        cur.execute(sql,(x1,x5))


    elif table_name == '"Maintenance_log"' : 
        sql = """ INSERT INTO datacenter_db."Maintenance_log"( "Log_ID", "Hardware_ID", "Employee_ID", "Problems", "Action_taken", "Cost") VALUES (%s, %s, %s, %s, %s, %s);"""
        print("Enter the Entry in the Order of: ")
        print("Log_ID, Hardware_ID, Employee_ID, Problems, Action_taken, Cost")
        x1,x2,x3,x4,x5,x6 = input().split()
        cur.execute(sql, (x1,x2,x3,x4,x5,x6))

    elif table_name == '"Security_applied"' :
        sql = """ INSERT INTO datacenter_db."Security_applied"( "Data_center_to_belong", "No_of_cameras", "No_of_personnels", "No_of_scanning_devices", "X-ray_machines", "No_of_Biometric_devices") VALUES (%s, %s, %s, %s, %s, %s);"""
        print("Enter the Entry in the Order of: ")
        print("Data_center_to_belong, No_of_cameras, No_of_personnels, No_of_scanning_devices, X-ray_machines, No_of_Bio_metric_security_devices")
        x1,x2,x3,x4,x5,x6 = input().split()
        cur.execute(sql, (x1,x2,x3,x4,x5,x6))

    elif table_name == '"Software"' :
        sql = """ INSERT INTO datacenter_db."Software"( "Prod_key", "S_name", "Validity", "Purchase_date", "Price", "Data_center_to_belong", "Manufacturer") VALUES (%s, %s, %s, %s, %s, %s, %s);"""
        print("Enter the Entry in the Order of: ")
        print("Prod_key, S_name, Validity, Purchase_date, Price, Data_center_to_belong, Manufacturer")
        x1,x2,x3,x4,x5,x6,x7 = input().split()
        cur.execute(sql, (x1,x2,x3,x4,x5,x6,x7))


def delete_from_a_table(cur):
    table_name = input("Enter table name: ")
    sql = " DELETE FROM datacenter_db." + table_name + "where "  
    condition = input("Enter your Condition in Query format: ")
    sql += condition 
    cur.execute(sql)

def custom_query(cur):
    sql = input("Enter your Query")
    cur.execute()

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement

        for x in range(40): print("*",end="")
        print(" ")
        print("List of Operation:")
        print("1. Show your Table.")
        print("2. Insert into a Table.")
        print("3. Delete a entry from a Table.")
        print("4. Run your own custom Query.")
        print("0. To exit the Menu. :)")
        for x in range(40): print("*",end="")
        print(" ")
        choice = 1
        while choice !=  0 :
            print("Enter your Choice: ")
            choice = int(input())
            if choice == 1:
                table_name = input("Enter Table Name:  ")
                show_table_details(cur,table_name)

            elif choice == 2:
                insert_into_a_table(cur)

            elif choice == 3:
                delete_from_a_table(cur)

            elif choice == 4:
                custom_query(cur)

            for x in range(40): print("*",end="")
            print(" ")

        
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
         print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()


