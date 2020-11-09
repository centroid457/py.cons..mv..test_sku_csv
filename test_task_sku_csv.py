import csv
import sys, time
import winsound

# USER DATA
SKU = "WP260qJAo6"          #testing variant
LEVEL = 0.0
fname = "recomends_5m.csv"


# MAIN CODE
arg_count = len(sys.argv)
if arg_count >= 2:
    SKU     = sys.argv[1] if len(sys.argv[1])==10 and sys.argv[1].isalnum() else exit("incorrect SKU")
if arg_count >= 3:
    try:
        LEVEL   = float(sys.argv[2]) if float(sys.argv[2]) <= 1 else exit("incorrect LEVEL")
    except ValueError:
        exit("incorrect LEVEL")

print("finding:",SKU, LEVEL)

csvfile = open(fname, newline='')
csvfile_obj = csv.reader(csvfile)

time_start = time.time()
result = set()
#winsound.Beep(1000, 500)

if LEVEL == 0:
    [result.update([c2]) for c1,c2,c3 in csvfile_obj if c1 == SKU]
else:
    [result.update([c2]) for c1,c2,c3 in csvfile_obj if c1 == SKU and float(c3) >= LEVEL]

print(round(time.time() - time_start, 2), "seconds")
print(len(result), result)
#winsound.Beep(1000, 500)
