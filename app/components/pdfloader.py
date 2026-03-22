import os
from langchain_community.document_loaders import DirectoryLoader,PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DATA_PATH,CHUNK_OVERLAP,CHUNK_SIZE

