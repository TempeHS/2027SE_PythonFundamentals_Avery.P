from fpdf import FPDF


def main():
    name = input("Name: ").strip()

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 40)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C", ln=True)

    # Shirt image (A4 width is 210mm)
    shirt_width = 190
    shirt_x = (210 - shirt_width) / 2
    shirt_y = 70
    pdf.image("shirtificate.png", x=shirt_x, y=shirt_y, w=shirt_width)

    # Name text on shirt
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(140)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
