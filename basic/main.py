robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

print("Robot Name:", robot["name"])
print("Robot Model:", robot["model"])

robot["battery"] = 100
print("Robot Battery:", robot["battery"])

robot["color"] = "Pink and Teal"
print("Robot Color:", robot["color"])

robot.pop("mode")
print("Total Settings", len(robot))
for key, value in robot.items():
    print(key, ":", value)

