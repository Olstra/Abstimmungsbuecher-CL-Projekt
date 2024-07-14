import pymupdf

pdf_path = "abstimmungsbuecher/erlaeuterungen_desbundesrates_26112006.pdf"
doc = pymupdf.open(pdf_path)
out = open("results/test_output.txt", "wb")
for page in doc:
    text = page.get_text().encode("utf8")
    out.write(text)
    out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
out.close()
