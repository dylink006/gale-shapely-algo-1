import matplotlib.pyplot as plt

def create_data_plot(x: list[int], y: list[int], verify: bool = False):
    plt.plot(x, y, linewidth=2.0)
    plt.xlabel("n")
    plt.ylabel('exec time in seconds')

    if verify:
        plt.savefig("verifier_chart.png")
    else:
        plt.savefig("gs_chart.png")

    plt.show()