from Bio import SeqIO
import argparse
import os


def get_seq(orf_input, domain_seq, output_path):
    orf_seq_list = SeqIO.parse(orf_input, "fasta")
    orf_contain_domain = []
    for orf_seq in orf_seq_list:
        if domain_seq.upper() in orf_seq.seq.upper():
                orf_contain_domain.append(orf_seq)
    result_file = os.path.join(output_path, f"{domain_seq}.faa")
    SeqIO.write(orf_contain_domain, result_file, "fasta")


def parse_domain_list(domain_file):
    with open(domain_file) as domain_f:
        domains = domain_f.readlines()
    do_new = []
    for domain_seq in domains:
        if domain_seq[-1] == "\n":
            do_new.append(domain_seq[:-1])
    return do_new

def parse_args():
    parser = argparse.ArgumentParser(
        prog="Domain Screener",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    required_args = parser.add_argument_group("Required named args")
    required_args.add_argument("-f",
                               "--faa",
                               help="path to the Protein ORF seqs Input",
                               type=str)
    required_args.add_argument("-d",
                            "--domain",
                            help="path to the domain list file",
                            type=str)
    required_args.add_argument("-o",
                               "--output",
                               help="Folder of results",
                               default="work",
                               type=str)
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_args()
    orf_input = args.faa
    domain_list = parse_domain_list(args.domain)
    output_path = args.output
    os.mkdir(output_path)
    for domain_seq in domain_list:
        get_seq(orf_input, domain_seq, output_path)



