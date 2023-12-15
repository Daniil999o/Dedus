# -*- coding: utf-8 -*-

import graphs
from extensions import *

docs_folder = 'docs/'
filtered_folder = 'filtered/'
documents = [docs_folder + f for f in os.listdir(docs_folder) if os.path.isfile(os.path.join(docs_folder, f))]


def filter_and_save_docs(docs):
    print('Start filtering...')

    files = {}

    for i, x in enumerate(docs):
        print(f'Filtered texts: {i}/{len(docs)}')
        files[x] = filter_text(read(x))

    print('\nStart recording...')

    for i in range(len(docs)):
        print(f'Recorded and fully filtered files: {i}/{len(docs)}')
        file = files[docs[i]]

        save(show_all(file), f'filtered_{i}')
        save(show_all(get_roots(file)), f'filtered_all_{i}')

    print('\n\n\n')


def compare_with_others(current_text_id, words, all_words):
    counter = Counter(words)

    percentages = {}
    percentages2 = {}

    all_counters = []

    for i, x in enumerate(all_words):
        if i != current_text_id:
            commons = remove_duplicates(words + x)
            temp_counter = Counter(x)
            all_counters.append(temp_counter)

            temp_percent = 0
            x_a = 0
            x_b = 0

            for word in commons:
                total = counter[word] + temp_counter[word]
                print(
                    f'Word {word} frequency: Text {current_text_id + 1}={counter[word]} {round(counter[word] / total * 100)}%, Text {i + 1}={temp_counter[word]} {round(temp_counter[word] / total * 100)}%')

                temp_percent += 1 if counter[word] > 0 and temp_counter[word] > 0 else 0

                # x_a += counter[word]
                # x_b += temp_counter[word]
                x_a += 1 if counter[word] > 0 else 0
                x_b += 1 if temp_counter[word] > 0 else 0

            temp_percent /= len(commons)
            percentages[i + 1] = round(temp_percent * 100, 2)
            percentages2[i + 1] = round(100 - (((x_a - x_b) / (x_a + x_b)) ** 2) * 100, 2)

            print('\n\n\n')

    print(f'Text {current_text_id + 1}. "{documents[current_text_id].split("/")[1]}" similars:\n')

    document_names = []
    for x in percentages:
        name = documents[x - 1].split('/')[1]
        print(f'Text {x}. "{name}" on v.1: {percentages[x]}% or v.2: {percentages2[x]}%')
        document_names.append(name)

    graphs.show_graph(documents[current_text_id].split("/")[1], counter, all_counters, document_names)


def show_counts():
    use_roots = input('Use only roots? y/n: ').lower() == 'y'

    docs = [filtered_folder + f for f in os.listdir(filtered_folder) if
            os.path.isfile(os.path.join(filtered_folder, f)) and
            (use_roots and '_all_' in f or not use_roots and '_all_' not in f)]

    all_docs = [get_words_from_lines(x) for x in docs]

    print('Current documents:')

    for i, x in enumerate(documents):
        name = x.split('/')[1]
        print(f'{i + 1}. {name}')

    print('')

    index = int(input('Enter text index for comparing: ')) - 1
    if 0 <= index < len(all_docs):
        compare_with_others(index, all_docs[index], all_docs)


def main():
    if not os.path.isdir('filtered'):
        os.makedirs('filtered')

    if len(os.listdir(filtered_folder)) <= 0 < len(documents):
        filter_and_save_docs(documents)

    show_counts()
    input()
    print('\n')
    main()


if __name__ == '__main__':
    if os.path.isdir('filtered') and input('Rewrite your existing files? y/n: ').lower() == 'y':
        shutil.rmtree('filtered')
        os.makedirs('filtered')

    main()
