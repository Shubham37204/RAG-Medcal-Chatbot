import os
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DATA_PATH,CHUNK_OVERLAP,CHUNK_SIZE

logger = get_logger(__name__)

#loading and checking the existing of the data root and having pdf in it or not
def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException("Data path does not exist")
        logger.info(f"loading files from {DATA_PATH}")
        loader = DirectoryLoader(DATA_PATH,glob="*.pdf",loader_cls=PyPDFLoader)
        documents=loader.load()
        if not documents:
            logger.warning("No Pdf were found")
        else:
            logger.info(f"Successfully fetched {len(documents)} documents")
        return documents
    except Exception as e:
        error_msg = CustomException("Failed to load pdf",e)
        logger.error(str(error_msg))
        return []
    
#loading the content of the pdf
def load_pdf_files(documents):
    try:
        if not documents:
            raise CustomException("No Document were found")
        logger.info(f"spliting {len(documents)} documents into chunks")
        text_spillter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)
        text_chunk=text_spillter.split_documents(documents=documents)
        logger.info(f"Generated {len(text_chunk)} text chunks")
        return text_chunk
    except Exception as e:
        error_msg = CustomException("Failed to load chunk",e)
        logger.error(str(error_msg))
        return []
