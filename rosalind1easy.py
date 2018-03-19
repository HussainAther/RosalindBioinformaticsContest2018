file = open("/Users/syedather/Downloads/input_easy.txt", "r")

solutions = []

# 1 mole of glucose and 6 moles of oxygen produce
# 38 moles of ATP during aerobic respiration

# 1 mole of glucose produces 2 moles of ATP
# during fermentation

def fermentation(glucose):
    return(glucose*2)

def aerobic_respiration(x, a, b):
    return (38 * x) / (a + 6*b)

def atp_produced(x, a, b):
    if fermentation(x/a) > aerobic_respiration(x,a,b): # When you spend all your money on fermentation or divide your money between oxygen and glucose
        solutions.append(fermentation(x/a))
    else:
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
