st = open("st.txt", "w")
st.write("Hi from Python!")
st.close()

with open("st2.txt", 'w') as f:
    f.write("Hello again!")

with open("st2.txt", "r") as f:
    print(f.read())

import csv
with open("self_taught2.csv", 'w', newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

with open("self_taught2.csv", 'r') as f:
    r = csv.reader(f, delimiter=',')
    for row in r:
        print(",".join(row))