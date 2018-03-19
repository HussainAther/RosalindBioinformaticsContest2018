file = open("/Users/syedather/Downloads/input1_hard.txt", "r")

solutions = []

# 1 mole of glucose and 6 moles of oxygen produce
# 38 moles of ATP during aerobic respiration
# During aerobic respiration, each mole of oxygen produces 6 moles of ATP
# and each mole of glucose produces 2 moles of ATP


def aerobic_respiration(x, a, b):
    oxygen_oxygen = int((6 * x) / (a + 6 * b)) # _oxygen means oxygen is the rate-limiting factor
    glucose_oxygen = int((x - (b * oxygen_oxygen)) / a)
    atp_oxygen = (2 * glucose_oxygen) + (6 * oxygen_oxygen)
    glucose_glucose = int(x / (a + 6 * b)) # _glucose means glucose is the rate-limiting factor
    oxygen_glucose = int((x - (a * glucose_glucose)) / b)
    atp_glucose = (2 * glucose_glucose) + (6 * oxygen_glucose)
    if atp_glucose < atp_oxygen: # If glucose is the rate-limiting factor
        glucose = glucose_glucose
        oxygen = oxygen_glucose
        atp = atp_glucose
        leftover = int((x - ((a*glucose) + (b*oxygen))) / a)
        atp += 2 * leftover
    else: # If oxygen is the rate-limiting factor
        glucose = glucose_oxygen
        oxygen = oxygen_oxygen
        atp = atp_oxygen
        leftover = int((x - ((a*glucose) + (b*oxygen))) / a)
        atp += 2 * leftover
    return atp

def atp_produced(x, a, b):
    solutions.append(aerobic_respiration(x,a,b))

count = 0

for line in file.readlines():
    if count > 0:
        glucose_mole_cost = float(line.replace("\n","").replace("\r","").split()[0])
        oxygen_mole_cost = float(line.replace("\n","").replace("\r","").split()[1])
        total_money = float(line.replace("\n","").replace("\r","").split()[2])
        atp_produced(total_money, glucose_mole_cost, oxygen_mole_cost)
    count += 1

for item in solutions:
    print(item)



