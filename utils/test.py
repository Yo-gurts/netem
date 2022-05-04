import redis

REDIS_HOST = "192.168.1.37"
REDIS_PORT = 6379
REDIS_PASSWORD = "uEstC318.#"

if __name__ == "__main__":
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, password=REDIS_PASSWORD)
    # up, down, left, right
    r.hset("all_links", "1101", "1111,1102,1601,1201")
    r.hset("all_links", "1102", "1101,1103,1602,1202")
    r.hset("all_links", "1103", "1102,1104,1603,1203")
    r.hset("all_links", "1104", "1103,1105,1604,1204")
    r.hset("all_links", "1105", "1104,1106,1605,1205")
    r.hset("all_links", "1106", "1105,1107,1606,1206")
    r.hset("all_links", "1107", "1106,1108,1607,1207")
    r.hset("all_links", "1108", "1107,1109,1608,1208")
    r.hset("all_links", "1109", "1108,1110,1609,1209")
    r.hset("all_links", "1110", "1109,1111,1610,1210")
    r.hset("all_links", "1111", "1110,1101,1611,1211")

    r.hset("all_links", "1201", "1211,1202,1101,1301")
    r.hset("all_links", "1202", "1201,1203,1102,1302")
    r.hset("all_links", "1203", "1202,1204,1103,1303")
    r.hset("all_links", "1204", "1203,1205,1104,1304")
    r.hset("all_links", "1205", "1204,1206,1105,1305")
    r.hset("all_links", "1206", "1205,1207,1106,1306")
    r.hset("all_links", "1207", "1206,1208,1107,1307")
    r.hset("all_links", "1208", "1207,1209,1108,1308")
    r.hset("all_links", "1209", "1208,1210,1109,1309")
    r.hset("all_links", "1210", "1209,1211,1110,1310")
    r.hset("all_links", "1211", "1210,1201,1111,1311")

    r.hset("all_links", "1301", "1311,1302,1201,1401")
    r.hset("all_links", "1302", "1301,1303,1202,1402")
    r.hset("all_links", "1303", "1302,1304,1203,1403")
    r.hset("all_links", "1304", "1303,1305,1204,1404")
    r.hset("all_links", "1305", "1304,1306,1205,1405")
    r.hset("all_links", "1306", "1305,1307,1206,1406")
    r.hset("all_links", "1307", "1306,1308,1207,1407")
    r.hset("all_links", "1308", "1307,1309,1208,1408")
    r.hset("all_links", "1309", "1308,1310,1209,1409")
    r.hset("all_links", "1310", "1309,1311,1210,1410")
    r.hset("all_links", "1311", "1310,1301,1211,1411")

    r.hset("all_links", "1401", "1411,1402,1301,1501")
    r.hset("all_links", "1402", "1401,1403,1302,1502")
    r.hset("all_links", "1403", "1402,1404,1303,1503")
    r.hset("all_links", "1404", "1403,1405,1304,1504")
    r.hset("all_links", "1405", "1404,1406,1305,1505")
    r.hset("all_links", "1406", "1405,1407,1306,1506")
    r.hset("all_links", "1407", "1406,1408,1307,1507")
    r.hset("all_links", "1408", "1407,1409,1308,1508")
    r.hset("all_links", "1409", "1408,1410,1309,1509")
    r.hset("all_links", "1410", "1409,1411,1310,1510")
    r.hset("all_links", "1411", "1410,1401,1311,1511")

    r.hset("all_links", "1501", "1511,1502,1401,1601")
    r.hset("all_links", "1502", "1501,1503,1402,1602")
    r.hset("all_links", "1503", "1502,1504,1403,1603")
    r.hset("all_links", "1504", "1503,1505,1404,1604")
    r.hset("all_links", "1505", "1504,1506,1405,1605")
    r.hset("all_links", "1506", "1505,1507,1406,1606")
    r.hset("all_links", "1507", "1506,1508,1407,1607")
    r.hset("all_links", "1508", "1507,1509,1408,1608")
    r.hset("all_links", "1509", "1508,1510,1409,1609")
    r.hset("all_links", "1510", "1509,1511,1410,1610")
    r.hset("all_links", "1511", "1510,1501,1411,1611")

    r.hset("all_links", "1601", "1611,1602,1501,1101")
    r.hset("all_links", "1602", "1601,1603,1502,1102")
    r.hset("all_links", "1603", "1602,1604,1503,1103")
    r.hset("all_links", "1604", "1603,1605,1504,1104")
    r.hset("all_links", "1605", "1604,1606,1505,1105")
    r.hset("all_links", "1606", "1605,1607,1506,1106")
    r.hset("all_links", "1607", "1606,1608,1507,1107")
    r.hset("all_links", "1608", "1607,1609,1508,1108")
    r.hset("all_links", "1609", "1608,1610,1509,1109")
    r.hset("all_links", "1610", "1609,1611,1510,1110")
    r.hset("all_links", "1611", "1610,1601,1511,1111")
