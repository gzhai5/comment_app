from fastapi import APIRouter, Body, HTTPException
from loguru import logger
from app.comment.comment_service import comment_service
from app.comment.model.comment_model import CommentModel, UpdateCommentModel
from app.utils.model.model import ErrorResponseModel


# define the router
router = APIRouter(prefix="/comment", tags=["Comment"])


@router.post("/", response_description="Add a new comment", status_code=201)
def add_comment(body: CommentModel):
    try:
        response = comment_service.add_comment(body)
        logger.info(f"INFO: Comment added successfully")
        return response
    except HTTPException as http_e:
        logger.error(f"ERROR: HTTPException occurred when adding comment: {http_e.detail}")
        return ErrorResponseModel(http_e.detail, http_e.status_code, "Failed to add comment.")
    except Exception as e:
        logger.error(f"ERROR: An unexpected error occurred when adding comment: {str(e)}")
        return ErrorResponseModel(str(e), 500, "Failed to add comment due to an unexpected error.")
    
@router.get("/{comment_id}", response_description="Get a single comment")
def get_comment(comment_id: str):
    try:
        response = comment_service.get_comment(comment_id)
        return response
    except HTTPException as http_e:
        logger.error(f"ERROR: HTTPException occurred when retrieving comment: {http_e.detail}")
        return ErrorResponseModel(http_e.detail, http_e.status_code, "Failed to retrieve comment.")
    except Exception as e:
        logger.error(f"ERROR: An unexpected error occurred when retrieving comment: {str(e)}")
        return ErrorResponseModel(str(e), 500, "Failed to retrieve comment due to an unexpected error.")
    
@router.get("/", response_description="Get all comments")
def get_comments():
    try:
        response = comment_service.retrieve_comments()
        return response
    except HTTPException as http_e:
        logger.error(f"ERROR: HTTPException occurred when retrieving all comments: {http_e.detail}")
        return ErrorResponseModel(http_e.detail, http_e.status_code, "Failed to retrieve comments.")
    except Exception as e:
        logger.error(f"ERROR: An unexpected error occurred when retrieving all comments: {str(e)}")
        return ErrorResponseModel(str(e), 500, "Failed to retrieve comments due to an unexpected error.")
    
@router.put("/{comment_id}", response_description="Update a comment")
def update_comment(comment_id: str, body: UpdateCommentModel = Body(...)):
    try:
        response = comment_service.update_comment(comment_id, body)
        return response
    except HTTPException as http_e:
        logger.error(f"ERROR: HTTPException occurred when updating comment: {http_e.detail}")
        return ErrorResponseModel(http_e.detail, http_e.status_code, "Failed to update comment.")
    except Exception as e:
        logger.error(f"ERROR: An unexpected error occurred when updating comment: {str(e)}")
        return ErrorResponseModel(str(e), 500, "Failed to update comment due to an unexpected error.")
    
@router.delete("/{comment_id}", response_description="Delete a comment")
def delete_comment(comment_id: str):
    try:
        response = comment_service.delete_comment(comment_id)
        return response
    except HTTPException as http_e:
        logger.error(f"ERROR: HTTPException occurred when deleting comment: {http_e.detail}")
        return ErrorResponseModel(http_e.detail, http_e.status_code, "Failed to delete comment.")
    except Exception as e:
        logger.error(f"ERROR: An unexpected error occurred when deleting comment: {str(e)}")
        return ErrorResponseModel(str(e), 500, "Failed to delete comment due to an unexpected error.")