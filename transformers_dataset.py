import os
from argparse import ArgumentParser
from tqdm import tqdm
import blingfire


def main(args):

    assert not os.path.isfile(args.output_file), (
        f"Cannot overwrite {args.output_file}"
    )
    for filename in args.input_files:
        assert os.path.isfile(filename), f"Input file {filename} does not exist"

    with open(args.output_file, "w") as out_file:
        for filename in args.input_files:
            with open(filename) as in_file:

                for line in tqdm(in_file, desc="Transforming file"):
                    line = line.strip()
                    if line == "":
                        out_file.write(line + "\n")
                    else:
                        for sentence in blingfire.text_to_sentences(line).split("\n"):
                            sentence = sentence.strip()
                            if len(sentence) > 0:
                                out_file.write(sentence + "\n")


if __name__ == "__main__":

    parser = ArgumentParser("Parse multiple wikipedia processed dumps into a single dataset")

    # Global level parameters
    parser.add_argument('-i', '--input_files', type=str, required=True, nargs='+',
                        help="Preprocessed dataset")
    parser.add_argument('-o', '--output_file', type=str, required=True,
                        help='Specify an output file')

    # get NameSpace of paramters
    args = parser.parse_args()

    main(args)

