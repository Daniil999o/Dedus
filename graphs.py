import matplotlib.pyplot as plt

max_words = 15


def show_graph(title, counter, counters, documents):
    counter = counter.most_common(max_words)

    plt.title(f'{title} graph')

    plt.xlabel('Words', fontsize=15)
    plt.ylabel('Counting', fontsize=15)

    plt.grid(True)

    keys = [k for k, v in counter]
    values = [v for k, v in counter]

    plt.text(keys[0], values[0], title, fontsize=10)
    plt.plot(keys, values)

    for i, x in enumerate(counters):
        this_counts = []
        for y in keys:
            this_counts.append(x[y])

        maximum = max(this_counts)
        plt.text(keys[this_counts.index(maximum)], maximum, documents[i], fontsize=10)
        plt.plot(keys, this_counts, linewidth=2.0)

    plt.show()
