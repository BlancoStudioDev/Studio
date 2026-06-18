"""Genera PDF dalla cheat sheet markdown."""

import re

from fpdf import FPDF


class CheatSheetPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.cell(0, 8, "Python for Statistics - Cheat Sheet", align="C")
            self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Pagina {self.page_no()}/{{nb}}", align="C")


def clean_text(text):
    # Rimuove emoji
    emoji_pattern = re.compile(
        "[" + "\U0001f300-\U0001f64f\U0001f680-\U0001f6ff"
        "\U0001f1e0-\U0001f1ff\U00002702-\U000027b0\U000024c2-\U0001f251]+",
        flags=re.UNICODE,
    )
    text = emoji_pattern.sub("", text)
    # Simboli matematici greci -> ASCII
    for u, a in [
        ("\u2264", "<="),
        ("\u2265", ">="),
        ("\u2260", "!="),
        ("\u03bb", "lambda"),
        ("\u03c7", "chi"),
        ("\u03a3", "Sigma"),
        ("\u03b1", "alpha"),
        ("\u03bc", "mu"),
        ("\u03c3", "sigma"),
        ("\u03a6", "Phi"),
        ("\u2202", "d"),
        ("\u2192", "->"),
        ("\u2190", "<-"),
        ("\u2013", "-"),
        ("\ufeff", ""),
    ]:
        text = text.replace(u, a)
    # Elimina qualsiasi altra cosa fuori latin-1
    return "".join(c if ord(c) < 256 else "" for c in text)


def md_to_pdf(md_path, pdf_path):
    pdf = CheatSheetPDF()
    pdf.alias_nb_pages()
    pdf.set_margins(15, 15, 15)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, "Python per Statistica", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(
        0,
        7,
        "Cheat Sheet da esami ed esercizi reali",
        align="C",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(5)

    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_code = False
    in_table = False
    code_buf = []
    table_buf = []

    for line in lines:
        s = clean_text(line.rstrip())

        if s.startswith("```"):
            if in_code:
                pdf.set_fill_color(240, 240, 240)
                pdf.set_font("Courier", "", 7)
                ix = pdf.l_margin + 4
                w = pdf.w - pdf.r_margin - ix
                for cl in code_buf:
                    cl = (
                        cl.replace("&gt;", ">")
                        .replace("&lt;", "<")
                        .replace("&amp;", "&")
                    )
                    pdf.set_x(ix)
                    pdf.multi_cell(w, 3.5, cl, fill=True)
                pdf.ln(2)
                code_buf = []
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_buf.append(s)
            continue
        if not s and not in_table:
            continue

        # Table
        if "|" in s and "---" not in s:
            table_buf.append(s)
            in_table = True
            continue
        if in_table and (not s or "---" in s):
            continue
        if in_table:
            pdf.set_font("Helvetica", "", 6.5)
            tw = pdf.w - pdf.l_margin - pdf.r_margin
            cw = [tw * 0.35, tw * 0.65]
            for tr in table_buf:
                cols = [c.strip() for c in tr.split("|")[1:-1]]
                for i, c in enumerate(cols):
                    pdf.cell(cw[i] if i < len(cw) else cw[-1], 5, c, border=1)
                pdf.ln()
            pdf.ln(2)
            table_buf = []
            in_table = False

        if s.startswith("##"):
            pdf.set_font("Helvetica", "B", 13)
            pdf.ln(2)
            pdf.cell(0, 8, s.replace("##", "").strip(), new_x="LMARGIN", new_y="NEXT")
            continue
        if s.startswith("###"):
            pdf.set_font("Helvetica", "B", 11)
            pdf.cell(0, 7, s.replace("###", "").strip(), new_x="LMARGIN", new_y="NEXT")
            continue
        if s.startswith("####"):
            pdf.set_font("Helvetica", "BI", 10)
            pdf.cell(0, 6, s.replace("####", "").strip(), new_x="LMARGIN", new_y="NEXT")
            continue
        if s.startswith("***") and s.endswith("***"):
            pdf.set_font("Helvetica", "B", 10)
            pdf.multi_cell(0, 5, s.replace("***", ""))
            continue
        if s.startswith("- "):
            pdf.set_font("Helvetica", "", 9)
            bx = pdf.l_margin
            pdf.set_x(bx)
            pdf.cell(4, 5, "-")
            w = pdf.w - pdf.r_margin - pdf.get_x()
            pdf.multi_cell(w, 5, s[2:])
            pdf.set_x(bx)
            continue

        pdf.set_font("Helvetica", "", 9)
        pdf.multi_cell(0, 5, s)
        pdf.ln(1)

    if in_table and table_buf:
        pdf.set_font("Helvetica", "", 6.5)
        tw = pdf.w - pdf.l_margin - pdf.r_margin
        cw = [tw * 0.35, tw * 0.65]
        for tr in table_buf:
            cols = [c.strip() for c in tr.split("|")[1:-1]]
            for i, c in enumerate(cols):
                pdf.cell(cw[i] if i < len(cw) else cw[-1], 5, c, border=1)
            pdf.ln()
        pdf.ln(2)

    pdf.output(pdf_path)
    print(f"PDF salvato: {pdf_path}")


if __name__ == "__main__":
    h = "/Users/blanco05/Desktop"
    md_to_pdf(f"{h}/cheat_sheet_python_stat.md", f"{h}/cheat_sheet_python_stat.pdf")
