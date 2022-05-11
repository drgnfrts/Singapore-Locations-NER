# Geocoding / Geotagging

## End Product

On Streamlit, key in example sentence. Location will be picked up by spaCy, disambiguated, and tagged onto a map.

## Steps to Get There

### Disambiguation of Locations

1. Spell check - spaCy has contextual_spellcheck and hunface extensions for spellcheck. Not sure if it will work for SG Locations but its worth a shot.
2. Removing of "Block" from informally referenced location names - screws up OneMap annd Mapbox
3. Informally referenced locations probably will face issues - OneMap, Mapbox and Google all have some rudimentary ability to tag when location names are slightly off, but when synonyms are used (e.g. "Maxwell Hawker Centre" instead of the formal "Maxwell Food Centre") they all die. I don't think I can fix this LOL but it doesn't really matter.
   1. Probably will just put a warning lor - this is an informally referenced location, there may be issues with geotagging. Until someone does coreferencing for SG locations, there's v little I can do -> will require some form of ML process, if not brute force matching which I DO NOT want to do LOL

### Geocoding and tagging options

Coding to query locations and generate a map should be relatively straightforward.

Problem is that no single geocoding service can do everything.

OneMap -> handles HDB and buildings v well, esp informally referenced HDBs. cannot reference roads or planning areas/subzones.

MapBox -> can basically input anything except planning areas/subzones. problem is that there's no validation of whether the tagged location is actually a building. hit or miss w informal place names, and not limited in scope to SG

Data for planning subzones and areas on data.gov.sg as kml/geojson files. -> will need conversion to mapbox.

### Geocoding and tagging strategy

- pull out location tags from model-processed text.
- iterate through planning area-subzone list.

- iterate thru planning areas/subzones. if ok, display seperate mapbox map if fail,
- search w mapbox. crosscheck w onemap - if latlong/place name do not match, indicate that it is either a road name, or

- search w onemap. if ok, take result and put in mapbox geocoding. if fail, indicate that this location is either ROADNAME or
-
- if ok, take result and put in mapbox geocoding, if fail,
- mapbox geocoding
