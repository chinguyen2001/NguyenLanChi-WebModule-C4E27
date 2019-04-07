from matplotlib import pyplot

machine_counts = [10, 5 ,6]

machine_names = ["PC", "PS4", "Nintendo"]

pyplot.pie(machine_counts, labels = machine_names, autopct = "%.1f%%", shadow=True, explode = [0.2, 0 ,0])
pyplot.axis("equal")
pyplot.title("PC vs PS4 vs Nintendo")

pyplot.show()