class Exporter:
    def export(self, data):
        return "Base Exporter"

    def __str__(self):
        return f"{type(self).__name__} object"


class ConsoleExporter(Exporter):
    def export(self, data):
        return f"{data['name']} - {data['course']} - {data['score']}"


class TextExporter(Exporter):
    def export(self, data):
        text = ""
        for key, value in data.items():
            text += f"{key}: {value}\n"
        return text.strip()


class SummaryExporter(Exporter):
    def export(self, data):
        result = "passed" if data["score"] >= 50 else "failed"
        return f"{data['name']} {result} {data['course']}"


# Composition: Report HAS-A exporter.
# Report does not inherit from Exporter; it stores an exporter
# object in self.export_obj and asks it to do the exporting.
# We can swap in any exporter without changing the Report class.
class Report:
    def __init__(self, title, export_obj):
        self.title = title
        self.export_obj = export_obj

    def publish_data(self, data):
        return f"=== {self.title} ===\n{self.export_obj.export(data)}"


# Duck typing: Storage does NOT inherit from Exporter,
# but it has an export(data) method with the same name.
# Python only checks that the method exists, not which class
# the object comes from, so Storage works in the same loop.
class Storage:
    def export(self, data):
        return f"Name : {data['name']}, Course : {data['course']}, Score : {data['score']}"

    def __str__(self):
        return "Storage object (not an Exporter)"


data = {"name": "Anna", "course": "Python", "score": 88}
exporters = [ConsoleExporter(), TextExporter(), SummaryExporter(), Storage()]

for exporter in exporters:
    print(f"\n{exporter}")
    print(exporter.export(data))

print(f"\nis SummaryExporter instance of Exporter ?  {isinstance(SummaryExporter(), Exporter)} ")
print(f"is Storage instance of Exporter ?  {isinstance(Storage(), Exporter)}\n")

new_data = {"name": "Harry", "course": "Java", "score": 30}
export_obj = SummaryExporter()
report = Report("Student Result", export_obj)
print(report.publish_data(new_data))
