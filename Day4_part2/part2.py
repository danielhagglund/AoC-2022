def is_overlap(range1, range2):
    set1 = set(range1)
    overlapping_sections = set1.intersection(range2)
    if overlapping_sections != set():
        return True
    return False
    
sections_map = open("./input.txt", encoding="utf8").read().splitlines()

number_of_overlaps = 0

for section_pair in sections_map:
    sections_tuple = section_pair.rpartition(",")
    section1_start = int(sections_tuple[0].rpartition("-")[0])
    section2_start = int(sections_tuple[2].rpartition("-")[0])
    section1_end = int(sections_tuple[0].rpartition("-")[2])
    section2_end = int(sections_tuple[2].rpartition("-")[2])

    range1 = range(section1_start,section1_end+1)
    range2 = range(section2_start, section2_end+1)
    if is_overlap(range1,range2) is True:
        number_of_overlaps = number_of_overlaps+1

print(number_of_overlaps)
