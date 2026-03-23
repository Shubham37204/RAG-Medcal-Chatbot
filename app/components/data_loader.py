import os
from app.components.pdfloader import load_pdf_files,create_text_chunks
from app.config.config import DB_FAISS_PATH
from app.components.vector_store import save_vector_store
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger=get_logger(__name__)

def process_store_pdfs():
    try:
        logger.info("Making the vector store")
        documents=load_pdf_files()
        text_chunks=create_text_chunks(documents)
        save_vector_store(text_chunks)
        logger.info("Vectorization created successfully..")
    except Exception as e:
        error_msg=CustomException("Failed to create vectorstore",e)
        logger.error(str(error_msg))
        raise e
        
if __name__=="__main__":
    process_store_pdfs()