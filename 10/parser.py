import re
import copy


tags = []
words = []
transition_count = {}
emission_count = {}
transition_probabilities = {}
emission_probabilities = {}


def import_tagged_files(filenames):
    """Load files and parse into 6 arrays:
    1. tags containing all states as strings
    2. words containing all emissions as strings
    3. transition_count a nested dict tag_k-1 -> tag_k -> number of occassions
    4. emission_count a nested dict tag_k -> emission_k -> number of occassions
    5.+6. same as count variants with probabilities instead of number of
      occassions
    """
    lines = read_files(filenames)
    last_tag = None
    for line in lines:
        last_tag = create_tag_from_line(line, last_tag)
    transition_probabilities = calculate_probabilties(transition_count)
    emission_probabilities = calculate_probabilties(emission_count)


def read_files(filesnames):
    """returns an array containing all lines from given filesnames"""
    lines = []
    for name in filesnames:
        with open(name, "r") as f:
            lines.extend(f.readlines())
    return lines


def add_tagged_word(tag, word, last_tag):
    """Creates or adjusts entries in the 4 arrays for a read tag"""
    if tags.count(tag) == 0:
        tags.append(tag)
    if words.count(word) == 0:
        words.append(word)

    if last_tag not in transition_count:
        transition_count[last_tag] = {tag: 1}
    elif tag not in transition_count[last_tag]:
        transition_count[last_tag][tag] = 1
    else:
        transition_count[last_tag][tag] += 1

    if tag not in emission_count:
        emission_count[tag] = {word: 1}
    elif word not in emission_count[tag]:
        emission_count[tag][word] = 1
    else:
        emission_count[tag][word] += 1


def create_tag_from_line(line, last_tag):
    """Parses a line into parts and creates it's entries"""
    if line != '\n':
        word, tag = re.split('\t', line.strip())
        add_tagged_word(tag, word, last_tag)
        return tag


def calculate_probabilties(counts):
    probabilities = copy.deepcopy(counts)
    for last_tag, tags in probabilities.items():
        count = 0
        for tag, tag_count in tags.items():
            count += tag_count
        for tag, tag_count in tags.items():
            probabilities[last_tag][tag] = tag_count / count
    return probabilities
