import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.styles import getSampleStyleSheet
import os

def make_bar_chart(chart_data, filename="my_chart.png"):
    names = list(chart_data.keys())
    numbers = list(chart_data.values())

    plt.figure()
    plt.bar(names, numbers, color="blue")
    plt.title("Performance Chart")
    plt.xlabel("Categories")
    plt.ylabel("Amount")
    
    plt.savefig(filename)
    plt.close()
    print("Chart created and saved")

def generate_my_report(report_title, kpis, chart_info):
    pdf_name = "final_report.pdf"
    
    chart_file = "temp_chart.png"
    make_bar_chart(chart_info, chart_file)

    pdf = SimpleDocTemplate(pdf_name, pagesize=letter)
    story = []
    
    styles = getSampleStyleSheet()

    story.append(Paragraph(report_title, styles['Heading1']))
    story.append(Paragraph("Here is the summary of our business KPIs and performance.", styles['Normal']))
    story.append(Spacer(1, 20))

    story.append(Paragraph("Key Metrics:", styles['Heading2']))
    
    table_rows = [["Metric Name", "Value"]]
    for key, value in kpis.items():
        table_rows.append([key, str(value)])

    my_table = Table(table_rows)
    story.append(my_table)
    story.append(Spacer(1, 20))

    story.append(Paragraph("Visual Data:", styles['Heading2']))
    story.append(Image(chart_file, width=400, height=200))

    pdf.build(story)
    print("PDF generated successfully!")

    if os.path.exists(chart_file):
        os.remove(chart_file)
        print("Cleaned up temp files.")

if __name__ == "__main__":
    my_kpis = {
        "Total Sales": "$5,000",
        "New Users": "120",
        "Growth": "+15%"
    }

    my_chart_data = {
        "Jan": 100,
        "Feb": 250,
        "Mar": 400,
        "Apr": 300
    }

    generate_my_report("My Monthly Business Report", my_kpis, my_chart_data)