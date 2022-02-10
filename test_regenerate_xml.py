import argparse
import sys

from Prepare_Dataset.get_missed_formulaids_in_xml_files import get_file_missed_formulas_post_file
from Prepare_Dataset.re_generate_post import regenerate_xml_files


def test_run(source_root):
    missed_formula_ids_path = "missed_formula_id.txt"
    missed_post_ids_path = "missed_post_id.txt"
    old_file_path = "Posts.V1.2.xml"
    latex_dir = "latex_representation_v2/"
    print("Getting missing formula ids")
    #Get missed ids
    get_file_missed_formulas_post_file(source_root + old_file_path, source_root + latex_dir,
                                       missed_formula_ids_path,
                                       missed_post_ids_path)
    print("Fixing XML file")
    # Regenerate XML file
    new_file_path = "Posts.V1.3.xml"
    regenerate_xml_files(missed_formula_ids_path, source_root + old_file_path, source_root + new_file_path,
                         source_root + latex_dir)

    print("Checking Generated file")
    # Get missed ids
    missed_formula_id_path = "new_missed_formula_id.txt"
    new_missed_post_ids = "new_missed_post_id.txt"
    get_file_missed_formulas_post_file(source_root + new_file_path, source_root + latex_dir,
                                       missed_formula_id_path,
                                       new_missed_post_ids)


def main():
    source_root = sys.argv[1]
    test_run(source_root)


if __name__ == '__main__':
    main()