#! /usr/bin/env python
""" A script that formats the data generated by pyeclib microbenches """

import os
import sys

import numpy

SIZES = [4, 16, 64]
NAME_ESCAPINGS = {
    "liberasurecode_rs_vand": "liberasure\\nrs\\\_vand",
    "jerasure_rs_vand": "jerasure\\nrs\\\_vand",
    "jerasure_rs_cauchy": "jerasure\\nrs\\\_cauchy",
    "flat_xor_hd_3": "flat\\\_xor\\nhd\\\_3",
    "flat_xor_hd_4": "flat\\\_xor\\nhd\\\_4",
    "isa_l_rs_vand": "isa\\\_l\\nrs\\\_vand"
}

def escape_name(name):
    """
    Escapes the name for gnuplot eps/pdf production
    """
    return NAME_ESCAPINGS.get(name, name.replace("_", r"\\_"))


def __format_data(scheme, directory):
    """
    Returns formatted data microbench data from a directory.
    The data is formatted in the following format:
    'library'   'throughtput'   'mean response time'   'standard deviation of response time'
    """
    output = []
    for library in os.listdir(directory):
        throughputs = []
        means = []
        standard_deviations = []
        dirpath = os.path.join(DIRECTORY, library)
        for size in SIZES:
            records = []
            microbench_file_prefix = "microbench-" + scheme + "-" + str(size) + "MB"
            microbench_files = [x for x in os.listdir(dirpath) if x.find(microbench_file_prefix) != -1]
            for microbench in microbench_files:
                filepath = os.path.join(dirpath, microbench)
                with open(filepath, "r") as microbench_file:
                    data = [float(x.strip()) for x in microbench_file.read().splitlines()[1:]]
                    records.extend(data)
            mean = -1
            standard_deviation = -1
            if len(records) > 0:
                mean = numpy.mean(records)
                standard_deviation = numpy.std(records)
            means.append(str(mean))
            standard_deviations.append(str(standard_deviation))
            throughput = (size) / (mean / 1000)
            throughputs.append(str(throughput))
        escaped_library_name = escape_name(library)
        output.append("\"" + escaped_library_name +"\" "+ " ".join(throughputs) + " " + " ".join(means) + " " +  " ".join(standard_deviations))
    output.sort()
    return "\n".join(output)


def format_encode_data(directory):
    """
    Returns formatted encoding microbench data
    """
    return __format_data("encode", directory)

def format_decode_data(directory):
    """
    Returns formatted decoding microbench data
    """
    return __format_data("decode", directory)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(0)
    DIRECTORY = sys.argv[1]
    ENCODERS_DATA = format_encode_data(DIRECTORY)
    DECODERS_DATA = format_decode_data(DIRECTORY)
    PATH_TO_ENCODERS_DATA_FILE = os.path.join(os.path.dirname(__file__), \
    "../papers/DAIS-2016/plots/microbench_tput/data/encoders_data.txt")
    PATH_TO_DECODERS_DATA_FILE = os.path.join(os.path.dirname(__file__), \
    "../papers/DAIS-2016/plots/microbench_tput/data/decoders_data.txt")
    with open(PATH_TO_ENCODERS_DATA_FILE, "w") as f:
        f.write(ENCODERS_DATA)
    with open(PATH_TO_DECODERS_DATA_FILE, "w") as f:
        f.write(DECODERS_DATA)
