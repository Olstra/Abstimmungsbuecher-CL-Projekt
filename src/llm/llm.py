import json
import os

import fitz
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pdfminer.high_level import extract_pages
from pdfminer.layout import LAParams, LTTextContainer
from langchain_core.messages import HumanMessage, SystemMessage


# load_dotenv()
#
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# model = ChatOpenAI(model="gpt-4o-mini")


def extract_text_from_pdf(pdf_path: str) -> str:
    result = []
    pages = extract_pages(pdf_path, laparams=LAParams())

    for page in extract_pages(pdf_path, laparams=LAParams()):
        for element in page:
            if isinstance(element, LTTextContainer):
                result.append(element.get_text())
    return result


if __name__ == "__main__":
    path = "../../test_data/five_pagers/Erste_5-Erlaeuterungen_Juni_RM_web.pdf"
    prompt = "Make paragraph text segmentation from this text. Expected output: {{'id':0,'content':'...'},{...}}:\n"
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=extract_text_from_pdf(path)),
    ]
    #print(model.invoke(messages).content)

    the_text = ""
    doc = fitz.open(path)
    for page in doc:
        the_text += page.get_text("text")

    print(the_text)
