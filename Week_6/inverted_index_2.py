import argparse
import json
import itertools


class InvertedIndex:
    def __init__(self, word_to_docs_mapping):
        self.word_to_docs_mapping = word_to_docs_mapping
        self.articles = set(itertools.chain(
            *self.word_to_docs_mapping.values()))

    def query(self, words):
        common_articles = set(self.articles)
        words_not_present = 0
        for word in words:
            try:
                common_articles &= self.word_to_docs_mapping[word]
            except KeyError:
                words_not_present += 1
        if words_not_present > 0:
            return set()
        return common_articles

    def dump(self, filepath):
        data = dict(map(lambda item: (item[0], list(
            item[1])), self.word_to_docs_mapping.items()))
        with open(filepath, "w") as file:
            json.dump(data, file)

    @classmethod
    def load(cls, filepath):
        with open(filepath) as file:
            data = json.load(file)
        data = dict(map(lambda item: (item[0], set(item[1])), data.items()))
        return cls(data)


def load_document(filepath):
    articles = dict()
    with open(filepath, encoding="utf8") as file:
        lines = file.readlines()
    data = map(lambda line: line.split("\t", maxsplit=1), lines)
    for x in data:
        articles[int(x[0])] = x[1].strip()
    return articles


def build_inverted_index(articles):
    inverted_index = dict()
    for index, text in articles.items():
        for word in text.split():
            inverted_index[word] = inverted_index.setdefault(word, set()) | {
                index}
    return InvertedIndex(inverted_index)


def main():
    parser = argparse.ArgumentParser(
        description="Final task: build an inverted index and query articles")
    subparsers = parser.add_subparsers(dest="command")
    build_parser = subparsers.add_parser(
        "build", help="builds an inverted index")
    build_parser.add_argument(
        "--dataset", help="path of the dataset containing the articles", required=True)
    build_parser.add_argument(
        "--index", help="path of the file that contains the inverted index", required=True)
    query_parser = subparsers.add_parser(
        "query", help="queries an article from the inverted index")
    query_parser.add_argument(
        "--index", help="path of the file that contains the inverted index", required=True)
    query_parser.add_argument(
        "--query_file", help="path to file containing the queries", required=True)
    args = parser.parse_args()
    if args.command == "build":
        articles_file, inverted_index_object_file = args.dataset, args.index
        inverted_index = build_inverted_index(
            load_document(articles_file))
        inverted_index.dump(inverted_index_object_file)
    elif args.command == "query":
        inverted_index_object_file, query_file = args.index, args.query_file
        inverted_index = InvertedIndex.load(inverted_index_object_file)
        with open(query_file, "r") as file:
            lines = []
            for line in file:
                lines.append(line.rstrip().split())
        for line in lines:
            result = inverted_index.query(line)
            print(*sorted(result), sep=",")


if __name__ == "__main__":
    main()
