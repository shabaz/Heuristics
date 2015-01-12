import random

DISTANCES = [[0,2164,1239,577,1789,1146,621,756,711,1501,2212,1768,1864,357,1481,1974,1515,2148,669,912,430,2014,1297,1744,1125,1458,936,1094],
             [2164,0,1877,1803,745,1125,2137,2855,2874,2469,563,1446,2851,2391,2368,860,1795,2232,1496,2606,2095,4160,1051,526,2408,2387,1283,1598],
             [1239,1877,0,1500,1972,1497,1759,1471,1676,2603,2234,2362,1007,1138,505,1219,2336,3010,1055,2143,831,2963,858,1748,2278,2541,1350,1863],
             [577,1803,1500,0,1296,688,355,1318,1204,1105,1737,1192,2314,932,1869,1846,953,1608,505,838,878,2385,1184,1319,810,1041,524,517],
             [1789,745,1972,1296,0,645,1575,2540,2481,1752,446,705,2977,2092,2474,1371,1059,1498,1189,2005,1872,3674,1140,297,1744,1671,858,945],
             [1146,1125,1497,688,645,0,1012,1895,1843,1460,1069,866,2470,1449,1974,1342,930,1569,561,1482,1244,3071,810,631,1317,1379,214,545],
             [621,2137,1759,355,1575,1012,0,1239,1050,883,2021,1327,2479,956,2072,2199,979,1560,841,483,1027,2104,1532,1637,522,837,870,672],
             [756,2855,1471,1318,2540,1895,1239,0,309,2024,2955,2507,1642,464,1450,2514,2210,2795,1378,1265,781,1492,1885,2474,1629,2004,1682,1827],
             [711,2874,1676,1204,2481,1843,1050,309,0,1768,2912,2363,1942,556,1718,2625,2028,2576,1378,991,898,1336,1967,2452,1377,1756,1639,1688],
             [1501,2469,2603,1105,1752,1460,883,2024,1768,0,2148,1163,3361,1821,2948,2798,714,892,1589,787,1908,2414,2202,1946,396,82,1439,915],
             [2212,563,2234,1737,446,1069,2021,2955,2912,2148,0,1019,3237,2500,2739,1388,1437,1756,1584,2448,2255,4118,1376,504,2174,2070,1276,1386],
             [1768,1446,2362,1192,705,866,1327,2507,2363,1163,1019,0,3324,2119,2833,2027,455,798,1368,1637,2003,3380,1639,979,1280,1090,1025,679],
             [1864,2851,1007,2314,2977,2470,2479,1642,1942,3361,3237,3324,0,1586,503,2096,3234,3907,1965,2739,1454,2950,1862,2754,2990,3312,2299,2760],
             [357,2391,1138,932,2092,1449,956,464,556,1821,2500,2119,1586,0,1263,2078,1872,2501,918,1154,343,1888,1433,2014,1433,1784,1235,1449],
             [1481,2368,505,1869,2474,1974,2072,1450,1718,2948,2739,2833,503,1263,0,1653,2765,3440,1485,2387,1053,2889,1363,2253,2593,2893,1809,2290],
             [1974,860,1219,1846,1371,1342,2199,2514,2625,2798,1388,2027,2096,2078,1653,0,2243,2817,1376,2679,1738,3961,682,1075,2615,2719,1374,1886],
             [1515,1795,2336,953,1059,930,979,2210,2028,714,1437,455,3234,1872,2765,2243,0,675,1284,1215,1826,2958,1738,1284,836,639,1004,475],
             [2148,2232,3010,1608,1498,1569,1560,2795,2576,892,1756,798,3907,2501,3440,2817,675,0,1960,1644,2486,3306,2377,1777,1227,867,1670,1151],
             [669,1496,1055,505,1189,561,841,1378,1378,1589,1584,1368,1965,918,1485,1376,1284,1960,0,1310,684,2677,698,1096,1314,1520,355,810],
             [912,2606,2143,838,2005,1482,483,1265,991,787,2448,1637,2739,1154,2387,2679,1215,1644,1310,0,1342,1744,2007,2096,417,787,1351,1063],
             [430,2095,831,878,1872,1244,1027,781,898,1908,2255,2003,1454,343,1053,1738,1826,2486,684,1342,0,2230,1105,1757,1544,1859,1033,1367],
             [2014,4160,2963,2385,3674,3071,2104,1492,1336,2414,4118,3380,2950,1888,2889,3961,2958,3306,2677,1744,2230,0,3299,3700,2132,2448,2886,2769],
             [1297,1051,858,1184,1140,810,1532,1885,1967,2202,1376,1639,1862,1433,1363,682,1738,2377,698,2007,1105,3299,0,895,1978,2126,765,1316],
             [1744,526,1748,1319,297,631,1637,2474,2452,1946,504,979,2754,2014,2253,1075,1284,1777,1096,2096,1757,3700,895,0,1884,1864,817,1074],
             [1125,2408,2278,810,1744,1317,522,1629,1377,396,2174,1280,2990,1433,2593,2615,836,1227,1314,417,1544,2132,1978,1884,0,379,1242,811],
             [1458,2387,2541,1041,1671,1379,837,2004,1756,82,2070,1090,3312,1784,2893,2719,639,867,1520,787,1859,2448,2126,1864,379,0,1362,835],
             [936,1283,1350,524,858,214,870,1682,1639,1439,1276,1025,2299,1235,1809,1374,1004,1670,355,1351,1033,2886,765,817,1242,1362,0,555],
             [1094,1598,1863,517,945,545,672,1827,1688,915,1386,679,2760,1449,2290,1886,475,1151,810,1063,1367,2769,1316,1074,811,835,555,0]]


maxtime = 20 * 60



def check_valid_tour(tour):
    prev_node = tour[0]
    expanded_tour = tour + [tour[0]]
    time_in_air = 0
    time_docking = (len(tour)-1) * 60
    naive_time_refueling = -60
    for i in expanded_tour[1:]:
        next_distance = DISTANCES[prev_node][i]
        time_in_air += next_distance / 800.0 * 60.0
        naive_time_refueling += next_distance / 3199.0 * 60.0
        prev_node = i

    min_refuelings = 1000
    for shift in xrange(len(tour)):
        expanded_tour = tour[shift:] + tour[:shift] + [tour[shift]]
        tank = 3199
        prev_node = expanded_tour[0]
        refuelings = 0
        for i in expanded_tour[1:]:
            next_distance = DISTANCES[prev_node][i]
            prev_node = i
            if tank < next_distance:
                tank = 3199
                refuelings += 1
            tank -= next_distance
        if refuelings < min_refuelings:
            min_refuelings = refuelings
    total_time = time_in_air + time_docking + min_refuelings * 60
    #print min_refuelings * 60, naive_time_refueling
    return total_time <= 20 * 60


def find_valid_tour_extensions(tour):
    time_docking = (len(tour)-1)*60
    time_in_air = 0
    naive_time_tanking = -60
    prev_node = tour[0]
    for i in tour[1:]:
        distance = DISTANCES[prev_node][i]
        time_in_air += distance/800.0 * 60.0
        naive_time_tanking += distance/3199.0 * 60
        prev_node = i
    time_so_far = time_in_air + time_docking + naive_time_tanking
    valid_extensions = []
    for i in xrange(28):
        distance = DISTANCES[tour[-1]][i]
        if i == tour[-1] or distance > 3199:
            continue
        addition_time_in_air = distance/800.0 * 60
        additional_time_refeuling = distance/3199.0 * 60.0
        extra_time = addition_time_in_air + additional_time_refeuling + 60
        if time_so_far + extra_time > 1200:
            continue
        extensions = find_valid_tour_extensions(tour+[i])
        if not extensions:
            extension = [i]
            if tour[0] in extension and check_valid_tour(tour+extension):
                valid_extensions.append(extension)
        for extension in extensions:
            full_extension = [i] + extension
            if tour[0] in full_extension and check_valid_tour(tour+full_extension):
                last_removed = None
                while last_removed != tour[0]:
                    last_removed = full_extension[-1]
                    full_extension = full_extension[:-1]
                valid_extensions.append(full_extension)
    return valid_extensions



def gen_tour(tour=[0]):
    time_so_far = -60
    prev_node = tour[0]
    for i in tour[1:]:
        distance = DISTANCES[prev_node][i]
        time_in_air = distance/800.0 * 60.0
        naive_time_tanking = distance/3199.0 * 60
        time_so_far += time_in_air + naive_time_tanking + 60
        prev_node = i

    adding = True
    while adding:
        child_candidates = []
        time_left = maxtime - time_so_far
        for child in xrange(28):
            child_distance = DISTANCES[tour[-1]][child]
            if child == tour[-1] or child_distance > 3199:
                continue
            time_in_air = child_distance/800.0 * 60
            time_fueling = child_distance / 3199.0 * 60
            if time_in_air + time_fueling + 60 > time_left:
                continue
            child_candidates.append(child)
        if not child_candidates:
            adding = False
        else:
            next_child = random.choice(child_candidates)
            child_distance = DISTANCES[tour[-1]][next_child]
            tour.append(next_child)
            time_in_air = child_distance/800.0 * 60
            time_fueling = child_distance / 3199.0 * 60
            time_so_far += time_in_air + time_fueling + 60
    if tour[0] == tour[-1] and check_valid_tour(tour[:-1]):
        return tour[:-1]
    else:
        extensions = None
        while not extensions:
            tour = tour[:-1]
            extensions = find_valid_tour_extensions(tour)
            extensions = [i for i in extensions if i]
        extended =  tour + random.choice(extensions)
        return extended







#valid_tours = []
#actual_valid_tours = []
#for i in xrange(1000):
#    tour = gen_tour()
#    if tour:
#        valid_tours.append(tour)
#        if check_valid_tour(tour):
#            actual_valid_tours.append(tour)
#print len(valid_tours)
#print len(actual_valid_tours)

def permutate_tour(tour):
    start = random.randrange(1,len(tour))
    if start == len(tour) - 1:
        end = len(tour)
    else:
        end = random.randrange(start+1,len(tour))
    shifted_tour = tour[end:] + tour[:start]
    extended_tour = gen_tour(shifted_tour)
    end_size = len(tour[end:])
    extended_tour = extended_tour[end_size:] + extended_tour[:end_size]
    return extended_tour

tour = gen_tour()
print tour



for i in xrange(15):
    tour = permutate_tour(tour)
    print tour
    if not check_valid_tour(tour):
        print "non valid tour"




#    extensions = find_valid_tour_extensions(tour)
#    if not extensions:
#        if not check_valid_tour(tour):
#            print "OOOOOOPPPPS"
#        else:
#            extended_tour = shifted_tour
#    else:
#        extended_tour = shifted_tour + random.choice(find_valid_tour_extensions(tour))
#    end_size = len(tour[end:])
#    extended_tour = extended_tour[end_size:] + extended_tour[:end_size]
#    print extended_tour
#    while extended_tour[-1] == extended_tour[0]:
#        extended_tour = extended_tour[:-1]
#    if not check_valid_tour(extended_tour):
#        print "XXXXXXXXXXXXXXXXX"
#        print "XXXXXXXXXXXXXXXXX"
#        print "XXXXXXXXXXXXXXXXX"
#        print "XXXXXXXXXXXXXXXXX"
#        print "XXXXXXXXXXXXXXXXX"
#        quit()


