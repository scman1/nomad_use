import sys
import json
from nomad.client import parse, normalize_all


# parse the input file
def parse_file(archive_in):
    # Match and run the parser
    archive = parse(archive_in) #parse(sys.argv[1])

    # Run all normalizers
    normalize_all(archive[0])

    # Convert to a Python dictionary
    python_dict = archive[0].run[0].m_to_dict()

    return python_dict

#save the parsed json metadata
def save_parsed(python_dict, archive_out):
    # save
    with open(archive_out, "w") as f:
        json.dump(python_dict, f, indent=2)
        
# test files
archive_in = "./inputs/nomad_example_01_orcafiles/16459/16459.out"
archive_out = "./outputs/orca_examples/16459/16459_2.nomad.json"

if __name__ == "__main__":
    print("script is being run directly")
    if len(sys.argv)>1:
        archive_in = sys.argv[1]
        archive_out = sys.argv[2]
    else:
        print("run_nomad_parse.py [input_file_name] [output_file_name]")

    parsed_data = parse_file(archive_in)
    save_parsed(parsed_data, archive_out)
    
    
