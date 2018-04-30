from matplotlib import pyplot

machine_counts = [18, 4, 2]

machine_names = ["PC","MAC","LINUX"]

pyplot.pie(machine_counts, labels = machine_names, autopct="%.1f%%", shadow = True, explode=[0,0.2,0])
pyplot.title("PC vs MAC vs LINUX usage")
pyplot.axis("equal")

pyplot.show()
