from pathlib import Path
import sys
import string


def read_file(file_name):
    """
    Leser en tekstfil og returnerer en liste med linjene i filen.
    """
    with open(file_name, "r", encoding="utf-8") as f:
        return f.readlines()


def lines_to_words(lines):
    """
    Deler linjene i listen opp i enkeltord, fjerner tegnsetting og gjør alt til små bokstaver.
    """
    words = []
    for line in lines:
        # Fjerner punktuasjon og splitter linjen i ord
        line = line.translate(str.maketrans('', '', string.punctuation)).lower()
        words.extend(line.split())
    return words


def compute_frequency(words):
    """
    Lager en frekvenstabell over ordene.
    """
    freq_table = {}
    for word in words:
        freq_table[word] = freq_table.get(word, 0) + 1
    return freq_table


FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    """
    Fjerner fyllord fra frekvenstabellen.
    """
    return {word: count for word, count in frequency_table.items() if word not in FILL_WORDS}


def largest_pair(par_1, par_2):
    """
    Sammenligner to (ord, frekvens)-tupler og returnerer det med høyest frekvens.
    """
    return par_1 if par_1[1] >= par_2[1] else par_2


def find_most_frequent(frequency_table):
    """
    Finner det mest brukte ordet i frekvenstabellen.
    """
    return max(frequency_table.items(), key=lambda x: x[1])[0] if frequency_table else None


def main():
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        file = sys.argv[1]
    else:
        file = str(Path(__file__).parent.absolute()) + "/voluspaa.txt"

    lines = read_file(file)
    words = lines_to_words(lines)
    table = compute_frequency(words)
    table = remove_filler_words(table)
    most_frequent = find_most_frequent(table)

    if most_frequent:
        print(f"The most frequent word in {file} is '{most_frequent}' with {table[most_frequent]} occurrences.")
    else:
        print("No words found in the file.")


if __name__ == '__main__':
    main()

