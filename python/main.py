from time import sleep
import webbrowser as wb

with open("image.txt") as file:
    lines = file.readlines()

wb.open("http://127.0.0.1:52013/index.html")
for line in lines:
    print(line)
    sleep(0.1)