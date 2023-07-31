import pymysql


def fetch_all_records():
    # create db connection
    db = None
    cursor = None
    try:
        # create db connection
        # db = pymysql.connect("localhost","root","m@vra123","test")
        db = pymysql.connect(host="localhost",
                             user="root",
                             password="",
                             db="bcs")

        cursor = db.cursor(pymysql.cursors.DictCursor)      # cursor which returns results as a dictionary
        query = "Select id,name,city  from students"
        # args=(1)
        cursor.execute(query)

        # result = cursor.fetchone()         # fetch one record
        # print(result)
        # print("id :", result["id"])
        # print("name :", result["name"])
        # print("city :", result["city"])

        results = cursor.fetchall()
        print("return type", type(results))
        # print(results)
        for r in results:
            print("id :", r["id"], "    name :", r["name"], "   city :", r["city"])

    except Exception as e:
        print("Error connecting db", str(e))
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


fetch_all_records()
