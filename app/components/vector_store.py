from langchain_community.vectorstores import FAISS
from app.components.embedding import get_embedding_model
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import os
from app.config.config import DB_FAISS_PATH
logger=get_logger(__name__)

def load_vector_store():
    try:
        embedding_model=get_embedding_model()
        if os.path.exists(DB_FAISS_PATH):
            logger.info("Loading existing vectorstore...")
            return FAISS.load_local(DB_FAISS_PATH,embedding_model,allow_dangerous_deserialization=True)
        else:
            logger.warning("No vector store found")
    except Exception as e:
        error_msg=CustomException("Failed to load vector store",e)
        logger.error(str(error_msg))
        
def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("No chunks were found ...")
        embedding_model=get_embedding_model()
        db=FAISS.from_documents(text_chunks,embedding_model)
        logger.info("Saving Vector store")
        db.save_local(DB_FAISS_PATH)
        logger.info("Vector store saved successfully...")
        return db
    except Exception as e:
        error_msg=CustomException("Failed to create new vector store",e)
        logger.error(str(error_msg))
