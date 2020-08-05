#!/usr/bin/env python
import sys
import random
from playsound import playsound, PlaysoundException # requires GStreamer
import time

# __main__():
years = ['1789', '1784', '1922', '1810', '1733', '1924', '1795', '1831', '1705', '1756', '1915', '1791', '1876', '2002', '1808', '1944', '1962', '1924', '1966', '1951', '2003', '2016', '1976', '1907', '1882', '1989', '1758', '1845', '1968', '2000', '1734', '1851', '1799', '1974', '2007', '1871', '1755', '1742', '1954', '1869', '1839', '1812', '1801', '1919', '1957', '1736', '1746', '1827', '1754', '1920', '1941', '1735', '1831', '1789', '1957', '1788', '1829', '1972', '1960', '2011', '1910', '1829', '1762', '1873', '1983', '1999', '1717', '1736', '1833', '2015', '1884', '1776', '1706', '1738', '1779', '1715', '1910', '2011', '1765', '1800', '1798', '1842', '1945', '1949', '1949', '1968', '1848', '1924', '1989', '1820', '1807', '1974', '1958', '1763', '1749', '1893', '1797', '2017', '1962', '1945', '1729', '1777', '1743', '1856', '1786', '1909', '2019', '1959', '1783', '1908', '1835']

if len(sys.argv) != 3:
    print("Usage: {} <start> <end>".format(sys.argv[0]))
    sys.exit(1)
try:
    range_start = int(sys.argv[1])
    range_end   = int(sys.argv[2])
    
    if range_start >= range_end or range_start < 1700 or range_end > 2020:
        raise ValueError()
    ans = []
    print("Press Ctrl+C to stop")
    while True:
        randn = random.randint(range_start, range_end).__str__()
        if randn in years:
            ans.append(randn)
            playsound("./years/{}.mp3".format(randn))
            time.sleep(1.5)
        else:
            pass
except KeyboardInterrupt:
    # Assumtion: Last number has already been fetch by the time we break the loop, so we ignore the unattempted last number 
    size  = len(ans)
    print(" Answers:")
    print(ans[:size-1]) 
    sys.exit(0)
except ValueError:
    print("Please pass years <start> and <end> values, in range [1700, 2020]")
    sys.exit(1)
except PlaysoundException:
    sys.exit(0)
except Exception as e:
    print("Unexpected error: " + e.__str__())
    sys.exit(1)

