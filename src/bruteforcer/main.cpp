#include <vector>
#include <iostream>
#include <stdlib.h>     /* exit, EXIT_FAILURE */

const int DISTANCES[28][28] = {{0,2164,1239,577,1789,1146,621,756,711,1501,2212,1768,1864,357,1481,1974,1515,2148,669,912,430,2014,1297,1744,1125,1458,936,1094},
             {2164,0,1877,1803,745,1125,2137,2855,2874,2469,563,1446,2851,2391,2368,860,1795,2232,1496,2606,2095,4160,1051,526,2408,2387,1283,1598},
             {1239,1877,0,1500,1972,1497,1759,1471,1676,2603,2234,2362,1007,1138,505,1219,2336,3010,1055,2143,831,2963,858,1748,2278,2541,1350,1863},
             {577,1803,1500,0,1296,688,355,1318,1204,1105,1737,1192,2314,932,1869,1846,953,1608,505,838,878,2385,1184,1319,810,1041,524,517},
             {1789,745,1972,1296,0,645,1575,2540,2481,1752,446,705,2977,2092,2474,1371,1059,1498,1189,2005,1872,3674,1140,297,1744,1671,858,945},
             {1146,1125,1497,688,645,0,1012,1895,1843,1460,1069,866,2470,1449,1974,1342,930,1569,561,1482,1244,3071,810,631,1317,1379,214,545},
             {621,2137,1759,355,1575,1012,0,1239,1050,883,2021,1327,2479,956,2072,2199,979,1560,841,483,1027,2104,1532,1637,522,837,870,672},
             {756,2855,1471,1318,2540,1895,1239,0,309,2024,2955,2507,1642,464,1450,2514,2210,2795,1378,1265,781,1492,1885,2474,1629,2004,1682,1827},
             {711,2874,1676,1204,2481,1843,1050,309,0,1768,2912,2363,1942,556,1718,2625,2028,2576,1378,991,898,1336,1967,2452,1377,1756,1639,1688},
             {1501,2469,2603,1105,1752,1460,883,2024,1768,0,2148,1163,3361,1821,2948,2798,714,892,1589,787,1908,2414,2202,1946,396,82,1439,915},
             {2212,563,2234,1737,446,1069,2021,2955,2912,2148,0,1019,3237,2500,2739,1388,1437,1756,1584,2448,2255,4118,1376,504,2174,2070,1276,1386},
             {1768,1446,2362,1192,705,866,1327,2507,2363,1163,1019,0,3324,2119,2833,2027,455,798,1368,1637,2003,3380,1639,979,1280,1090,1025,679},
             {1864,2851,1007,2314,2977,2470,2479,1642,1942,3361,3237,3324,0,1586,503,2096,3234,3907,1965,2739,1454,2950,1862,2754,2990,3312,2299,2760},
             {357,2391,1138,932,2092,1449,956,464,556,1821,2500,2119,1586,0,1263,2078,1872,2501,918,1154,343,1888,1433,2014,1433,1784,1235,1449},
             {1481,2368,505,1869,2474,1974,2072,1450,1718,2948,2739,2833,503,1263,0,1653,2765,3440,1485,2387,1053,2889,1363,2253,2593,2893,1809,2290},
             {1974,860,1219,1846,1371,1342,2199,2514,2625,2798,1388,2027,2096,2078,1653,0,2243,2817,1376,2679,1738,3961,682,1075,2615,2719,1374,1886},
             {1515,1795,2336,953,1059,930,979,2210,2028,714,1437,455,3234,1872,2765,2243,0,675,1284,1215,1826,2958,1738,1284,836,639,1004,475},
             {2148,2232,3010,1608,1498,1569,1560,2795,2576,892,1756,798,3907,2501,3440,2817,675,0,1960,1644,2486,3306,2377,1777,1227,867,1670,1151},
             {669,1496,1055,505,1189,561,841,1378,1378,1589,1584,1368,1965,918,1485,1376,1284,1960,0,1310,684,2677,698,1096,1314,1520,355,810},
             {912,2606,2143,838,2005,1482,483,1265,991,787,2448,1637,2739,1154,2387,2679,1215,1644,1310,0,1342,1744,2007,2096,417,787,1351,1063},
             {430,2095,831,878,1872,1244,1027,781,898,1908,2255,2003,1454,343,1053,1738,1826,2486,684,1342,0,2230,1105,1757,1544,1859,1033,1367},
             {2014,4160,2963,2385,3674,3071,2104,1492,1336,2414,4118,3380,2950,1888,2889,3961,2958,3306,2677,1744,2230,0,3299,3700,2132,2448,2886,2769},
             {1297,1051,858,1184,1140,810,1532,1885,1967,2202,1376,1639,1862,1433,1363,682,1738,2377,698,2007,1105,3299,0,895,1978,2126,765,1316},
             {1744,526,1748,1319,297,631,1637,2474,2452,1946,504,979,2754,2014,2253,1075,1284,1777,1096,2096,1757,3700,895,0,1884,1864,817,1074},
             {1125,2408,2278,810,1744,1317,522,1629,1377,396,2174,1280,2990,1433,2593,2615,836,1227,1314,417,1544,2132,1978,1884,0,379,1242,811},
             {1458,2387,2541,1041,1671,1379,837,2004,1756,82,2070,1090,3312,1784,2893,2719,639,867,1520,787,1859,2448,2126,1864,379,0,1362,835},
             {936,1283,1350,524,858,214,870,1682,1639,1439,1276,1025,2299,1235,1809,1374,1004,1670,355,1351,1033,2886,765,817,1242,1362,0,555},
             {1094,1598,1863,517,945,545,672,1827,1688,915,1386,679,2760,1449,2290,1886,475,1151,810,1063,1367,2769,1316,1074,811,835,555,0}};



int find_minimum_refuelings(std::vector<int>& tour)
{
    int tour_size = tour.size();
    int min_refuelings = 10000;
    for (int shift = 0; shift < tour_size; shift++) {
        int tank = 3199;
        int refuelings = 0;
        int current_index = shift;
        do {
            int next_index = (current_index + 1) % tour_size;
            int distance = DISTANCES[current_index][next_index];
            if (tank < distance) {
                tank = 3199;
                refuelings++;
            }
            tank -= distance;
            current_index = next_index;
        } while (current_index != shift);
        if (refuelings < min_refuelings)
            min_refuelings = refuelings;
    }
    return min_refuelings;
}


bool check_valid_route(std::vector<int>& route)
{
    int prev = -1;
    int distance_in_air = 0;
    for (auto i: route) {
        int distance;
        if (prev == -1) {
            distance = DISTANCES[route.back()][route[0]];
        } else {
            distance = DISTANCES[prev][i];
        }
        prev = i;
        if (distance > 3199)
            return false;
        distance_in_air += distance;
    }

    float time_in_air = distance_in_air / 800.0 * 60.0;
    float naive_time_tanking = -60 + distance_in_air / 3199.0 * 60;
    int time_docking = route.size() * 60;
    if (time_in_air + naive_time_tanking + time_docking > 1200) {
        return false;
    }

    int refuelings = find_minimum_refuelings(route);
    return (time_in_air + time_docking + refuelings * 60) <= 1200;
}

int calculate_cost(std::vector<int>& route)
{
    int PASSENGERS[28][28] = {{0,213,119,278,89,302,388,153,341,273,112,361,302,324,269,206,147,400,367,172,45,321,100,135,86,95,257,371},
        {373,0,377,341,202,161,354,182,424,69,96,52,141,5,224,425,277,88,380,290,444,89,0,28,376,296,323,7},
        {403,165,0,327,231,403,113,287,218,264,443,166,436,322,37,206,252,291,414,271,223,287,408,251,127,299,3,58},
        {143,238,15,0,110,380,387,205,280,65,208,56,289,82,221,249,273,363,77,272,365,444,175,363,35,428,206,61},
        {320,360,375,345,0,433,246,239,82,20,205,350,271,41,335,327,31,307,17,262,424,349,273,369,253,448,238,263},
        {86,1,281,370,75,0,354,255,22,31,105,342,183,73,120,91,256,89,70,236,108,242,274,421,331,166,329,249},
        {49,264,371,277,292,3,0,330,363,143,197,184,209,50,414,164,421,394,262,390,214,363,28,187,337,187,96,34},
        {110,413,36,366,31,174,75,0,102,138,101,269,283,205,166,38,38,332,118,352,59,338,14,91,332,20,418,163},
        {46,313,371,24,87,414,44,196,0,49,78,351,112,432,290,121,369,5,187,97,55,428,41,264,441,191,37,245},
        {119,262,389,175,147,431,194,368,319,0,62,107,85,120,129,96,342,302,425,245,187,419,189,133,315,424,289,92},
        {261,20,14,81,390,154,41,450,356,165,0,75,291,41,55,138,58,88,350,295,84,150,334,120,101,405,280,65},
        {244,362,175,118,38,201,332,168,417,324,162,0,363,137,4,170,232,326,397,302,3,5,4,359,347,369,413,308},
        {251,248,431,243,318,398,407,290,378,45,70,16,0,140,94,100,215,293,265,202,168,374,51,293,120,435,368,324},
        {91,424,232,148,310,410,120,393,406,266,110,434,450,0,193,288,40,128,442,144,63,95,9,341,110,220,320,138},
        {235,136,341,383,255,414,181,228,223,140,76,304,326,293,0,438,23,93,123,378,449,362,203,194,386,123,365,373},
        {191,359,76,10,39,293,116,129,4,314,428,273,388,342,321,0,18,239,402,164,441,47,429,423,9,276,334,323},
        {179,430,128,330,307,405,87,202,91,325,91,209,42,309,446,434,0,280,415,106,333,161,309,403,383,430,117,246},
        {5,360,144,212,46,48,409,375,267,326,51,306,95,16,365,59,8,0,351,37,219,397,242,245,245,407,30,375},
        {25,61,232,425,309,252,38,69,205,77,310,350,328,393,177,106,21,102,0,219,56,126,318,265,120,247,263,426},
        {79,103,351,40,133,150,116,0,206,187,369,157,295,177,115,152,331,366,154,0,4,122,402,342,379,361,382,325},
        {206,25,450,341,234,100,345,290,179,81,388,285,415,222,83,280,227,352,181,440,0,81,378,331,100,113,304,109},
        {316,4,398,268,419,161,73,36,96,385,373,434,123,295,16,172,109,360,196,356,263,0,382,314,322,352,120,417},
        {157,62,337,246,314,271,250,180,387,386,379,41,255,49,139,332,283,313,337,7,121,97,0,275,357,348,78,413},
        {107,403,353,383,54,407,142,66,360,408,377,80,430,193,131,341,216,176,224,77,251,43,381,0,16,122,175,237},
        {285,335,166,287,215,108,275,131,362,267,250,18,421,302,280,57,368,100,391,390,134,391,77,409,0,157,244,100},
        {373,433,407,186,98,377,122,110,247,398,299,236,12,15,78,177,307,260,135,27,272,288,127,153,415,0,257,324},
        {312,322,57,159,135,450,15,12,92,47,41,440,315,39,193,124,224,68,439,28,290,287,366,153,427,115,0,314},
        {441,256,62,423,215,432,412,128,361,128,138,360,87,181,113,389,200,141,300,281,337,9,180,203,379,290,165,0}};


    int cost = 0;
    int prev = -1;
    for (auto i: route)
    {
        int distance=0;
        int passengers=0;
        if (prev == -1) {
            distance = DISTANCES[route.back()][route[0]];
            int passengers = PASSENGERS[route.back()][route[0]];
            if (passengers > 199)
                passengers = 199;
            PASSENGERS[route.back()][route[0]] -= passengers;
        } else {
            distance = DISTANCES[prev][i];
            passengers = PASSENGERS[prev][i];
            if (passengers > 199)
                passengers = 199;
            PASSENGERS[prev][i] -= passengers;
        }
        cost += passengers * distance;
        prev = i;
    }
    return cost;
}

int checked = 0;
int valid = 0;

int best_cost = 0;
std::vector<int> best_route;

int best_updates = 0;

void check_tree(std::vector<int>& route, float time_so_far, int depth)
{
    if (time_so_far > 1200) {
        return;
    }

    checked++;
    if (check_valid_route(route)) {
        int cost = calculate_cost(route);
        if (cost > best_cost) {
            best_cost = cost;
            best_route = route;
            std::cout << "new best cost " << best_cost << " with route [";
            for (auto i: best_route)
            {
                std::cout << i << ", ";
            }
            std::cout << "]\n";
            best_updates++;
        }
        valid++;
    }
    for (int i = 0; i < 28; i++)
    {
        int distance = DISTANCES[route.back()][i];
        if (distance > 3199 || i == route.back())
            continue;
        float additional_time_in_air = distance / 800.0 * 60;
        float additional_naive_tanking_time = distance / 3199.0 * 60;
        route.push_back(i);
        check_tree(route, time_so_far + additional_naive_tanking_time + additional_time_in_air + 60, depth+1);
        route.pop_back();
    }
    if (depth < 3)
        std::cout << "depth " << depth << " checked " << checked << " valid " << valid << std::endl;
}

int main(int argc, char* argv[])
{
    int homebase = 0;
    std::vector<int> route;
    route.reserve(20);
    route.push_back(homebase);

    check_tree(route, 0, 0);
   
    return 0;
}
