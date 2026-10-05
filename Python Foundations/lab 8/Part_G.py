class Report:
    def get_summary(self):
        return "This is the base report"


class SalesReport(Report):
    def get_summary(self):
        return super().get_summary() + " and includes Sales report"


sales_report = SalesReport()

print(sales_report.get_summary())
