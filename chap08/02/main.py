# we'll use one powered by the pypdf package that reads from a filepath:
# pip install pypdf
from langchain_community.document_loaders import PyPDFLoader

file_path = "./data/2001_1.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()

print(len(docs))
print(docs[0].page_content[0:200])
print(docs[0].metadata)