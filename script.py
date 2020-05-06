import os
import pandas as pd
import wget

printPDF = True
printEPUB = True

df = pd.read_excel("Free+English+textbooks.xlsx")

for idx, row in df.iterrows():
    print(row["Book Title"] + "\n")
    doi = row["DOI URL"]
    doi = doi.split("doi.org/")[1]
    # print(doi)
    doi = doi.replace("/", "%2F")

    try:
        if printPDF:
            url = "https://link.springer.com/content/pdf/" + doi + ".pdf"
            print(url + "\n")
            filename = wget.download(url)
            print("\n")
            os.rename(filename, row["Book Title"] + ".pdf")

        if printEPUB:
            url = "https://link.springer.com/download/epub/" + doi + ".epub"
            print(url + "\n")
            filename = wget.download(url)
            print("\n")
            os.rename(filename, row["Book Title"] + ".epub")
    except:
        continue
