import json

files = ['../data/extracted_locations/extracted_lrt_stns.json',
         '../data/extracted_locations/extracted_mrt_stns.json',
         '../data/extracted_locations/short_manual_buildings_name_list.json',
         '../data/extracted_locations/extracted_buildings_address_list.json',
         '../data/extracted_locations/extracted_buildings_postcode.json',
         '../data/extracted_locations/extracted_road_names_list.json',
         '../data/extracted_locations/extracted_subzones.json'
         ]


def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    list(set(result))

    with open('../data/extracted_locations/combined_locations.json', "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)


merge_JsonFiles(files)
