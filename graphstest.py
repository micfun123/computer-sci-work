import matplotlib.pyplot as plt
import numpy as np

def plot_A2():

    fysiker = ("JB", "EG")

    volymer_A2 = {
        'M4': (22.9, 17.6), 
        'M5': (22.0, 16.4),
        'M6': (21.4, 16.0),
        'M7': (21.8, 17.6),
    }

    x = np.arange(len(fysiker))  # the label locations
    width = 0.15  # the width of the bars
    multiplier = -0.5

    fig, ax = plt.subplots(layout='constrained')

    patterns = ['/', '.','+','o']  # Define the patterns for the bars

    for index, (attribute, measurement) in enumerate(volymer_A2.items()):
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, color='gray', hatch=patterns[index%len(patterns)], label=attribute)  # Use hatch parameter to set the pattern
        ax.bar_label(rects, padding=3)
        multiplier += 1
  
    # Plot true volume
    volume_A2 = 18.77
    ax.plot([-2,5], [volume_A2, volume_A2], "k--", linewidth=1, color='gray', label='True volume')
   
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Volume (ml)')
    ax.set_title('Phantom A2')
    ax.set_xticks(x + width, fysiker)
    ax.legend(loc='upper center')
    ax.set_ylim(15, 25)
    ax.set_xlim(-0.2, 1.5)

    plt.show()

plot_A2()
