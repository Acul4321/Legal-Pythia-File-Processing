import os

from pypdf import PdfReader
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/getText")
async def root():
    pdf = PdfReader("files/IHA_AGBH_8.1__LV-Broschuere__2021_3.pdf")
    noLines = len(pdf.pages)
    text = ""
    for x in range(noLines):
        page = pdf.pages[x]
        current = page.extract_text()
        current = current + "<br>"
        text = text + current
    return text

#python -m uvicorn LPFileClass:app --reload