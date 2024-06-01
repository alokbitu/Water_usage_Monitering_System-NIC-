import random
import time
from config import *
import mysql.connector
import datetime

mydb = mysql.connector.connect(user='root', password='admin123', host='localhost', database='nicrtdas', auth_plugin='mysql_native_password')

def calculation():
    one_day_flow = []
    while len(one_day_flow) < 24:
        one_hr_flow = []
        while len(one_hr_flow) < 60:
            # mycursor = mydb.cursor()
            # flow_sql = "select min_flow from minute_flow_table"
            # flow = mycursor.execute(flow_sql)
            flow = random.uniform(0.0, 30.0)
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

            # Write to file without timestamp (overwrite)
            with open('LATEST_RANDOM_DATA.txt', 'w') as file2:
                file2.write(f'{round(flow, 3)}, {timestamp}\n')

            with open('cons&use_random.txt','r') as file3:
                file_contents = file3.read()
                consumption,extra_use = file_contents.split(',')

            # mycursor = mydb.cursor()
            # sql = "INSERT INTO minute_flow_table(stn_id, plant_nm, device_id, minute_flow, allocation, consumption, datetime) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            # try:
            #     mycursor.execute(sql, (station_id, plant_nm, DEVICE_ID, round(flow, 3), allocation, consumption, timestamp))
            #     mydb.commit()
            #     print(mycursor.rowcount, "details inserted")
            # except Exception as e:
            #     print("Something went wrong:", e)
            #     mycursor.close()
            #     mydb.close()
            #     return
            mycursor = mydb.cursor()
            sql = "INSERT INTO db_migrate_pollutant_level_data_2023_6(plant_id,analyzer,station_id,parameter_code,recorded_time,recorded_level,min_recorded_level,max_recorded_level,sum_level,total_level,recorded_day,recorded_hour,recorded_type) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s)"
            try:
                mycursor.execute(sql,
                                 ('nic', 'water' , DEVICE_ID, 'flow',timestamp, round(flow, 3), 23,50, 40,100,13.3,23.3,1))
                mydb.commit()
                print(mycursor.rowcount, "details inserted")
            except Exception as e:
                print("Something went wrong:", e)
                mycursor.close()
                mydb.close()
                return

            one_hr_flow.append(round(flow, 3))
            time.sleep(60)

        if len(one_hr_flow) == 60:
            # Find the minimum, maximum, and average values
            min_value = min(one_hr_flow)
            max_value = max(one_hr_flow)
            average = round(sum(one_hr_flow) / len(one_hr_flow), 3)
            hourly_flow = round(sum(one_hr_flow),3)

            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M')

            mycursor = mydb.cursor()
            sql = "INSERT INTO hourly_flow_table(stn_id, plant_nm, device_id, hr_flow, allocation, datetime) VALUES (%s, %s, %s, %s, %s, %s)"
            try:
                mycursor.execute(sql,(station_id, plant_nm, DEVICE_ID, round(hourly_flow, 3), allocation, timestamp))
                mydb.commit()
                print(mycursor.rowcount, "details inserted")
            except Exception as e:
                print("Something went wrong:", e)
                mycursor.close()
                mydb.close()
                return

            print("Hourly Minimum value:", min_value)
            print("Maximum value:", max_value)
            print("Average value:", average)

        one_day_flow.append(round(sum(one_hr_flow)))

    if len(one_day_flow) == 24:
        min_value = min(one_day_flow)
        max_value = max(one_day_flow)
        average = round(sum(one_day_flow) / len(one_day_flow), 3)

        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')

        mycursor = mydb.cursor()
        sql = "INSERT INTO oneday_flow_table(stn_id, plant_nm, device_id, min_flow, max_flow, avg_flow, allocation, datetime) values (%s, %s, %s, %s, %s,%s,%s,%s)"
        try:
            mycursor.execute(sql, (station_id, plant_nm, DEVICE_ID, round(min_value, 3), round(max_value, 3), round(average, 3), allocation, timestamp))
            mydb.commit()
            print(mycursor.rowcount, "details inserted")
        except Exception as e:
            print("Something went wrong:", e)

            mycursor.close()
            mydb.close()

        print("One_day_Minimum value:", min_value)
        print("Maximum value:", max_value)
        print("Average value:", max_value)



if __name__ == '__main__':
    while True:
        calculation()
        print('loop reinitiated')
