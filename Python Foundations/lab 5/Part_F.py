# 1
def create_report(title, *sections, **metadata):
    """
    Section can be either string or dictionary.
    Both are allowed. Because some sections are sentences and some are just counts
    """
    student_report = {"title" : title, "sections" : sections}
    student_report.update(metadata)
    return student_report

print("Q-1")
metadata_1 = {"author" : "Mr. Harry", "department" : "IT", "version" : 1.0, "date" : "16-09-2026", "Confidential" : True}
report_1 = create_report("Weekly Engineering Status Report", "Weekly Update", **metadata_1)
print(report_1)


# 2
# section as dictionary
print("\nQ-2")
section = {"Completed" : 5, "In-Progress" : 1, "Pending" : 2}
report_2 = create_report("Weekly Report", section, **metadata_1)
print(report_2)

# 3
metadata_1 = {"author" : "Mr. Harry", "department" : "IT", "version" : 1.0, "date" : "16-09-2026", "Confidential" : True}

# 4
def summarize_report(report):
    text = []
    text.append(f"Title : {report.get('title')}")
    text.append(f"Section : {report.get('sections')}") # need to figure out better way
    for k, v in report.items():
        if k not in ("title", "sections"):
            text.append(f"{k} : {v}")
    text = "\n".join(text)
    return text

print("\nQ-4")
summary = summarize_report(report_1)
print(summary)
summary_1 = summarize_report(report_2)
print(summary_1)


# 5
print("\nQ-5")
def count_words(*sections):
    words = []
    for s in sections:
        words.extend(s.split()) # splitting based on whitespace(spaces, tabs, newlines, drops leading and trailing whitespace)
    return len(words)

section_1 = "Weekly student report"
section_2 = "Weekly Engineering Student Report"
print(count_words(section_1, section_2))


# 6
print("\nQ-6")
metadata_2 = {"author" : "Mr. Potter", "department" : "CS", "version" : 2.0, "date" : "17-09-2026", "Confidential" : False}

report_3 = create_report("Book", "Infrastructure Update", **metadata_1)
report_4 = create_report("Book", "Curriculum changes", **metadata_2)

print(report_3)
print(report_4)


# 7
print("\nQ-7")
metadata_3 = {"author" : "Ms. Granger"}

report_5 = create_report("Library Report", "Book", **metadata_3)
print(summarize_report(report_5))
