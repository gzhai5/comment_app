from fastapi import HTTPException
from loguru import logger
from app.comment.model.comment_model import CommentModel, UpdateCommentModel
from app.comment.database.comment_database import comment_database
from app.utils.model.model import ResponseModel, ErrorResponseModel


class CommentService:
    def __init__(self):
        self.db = comment_database

    def add_comment(self, comment: CommentModel):
        comment_data = comment.dict()
        comment_in_db = self.db.add_comment(comment_data)
        return ResponseModel(comment_in_db, "Comment added successfully.")
    
    def get_comment(self, comment_id: str):
        comment = self.db.retrieve_comment(comment_id)
        if not comment:
            logger.error(f"ERROR: Comment with id {comment_id} not found")
            return ErrorResponseModel(None, 404, f"Comment with id {comment_id} not found")
        return ResponseModel(comment, "Comment retrieved successfully.")
    
    def retrieve_comments(self):
        comments = self.db.retrieve_comments()
        return ResponseModel(comments, "Comments retrieved successfully.")
    
    def update_comment(self, comment_id: str, comment: UpdateCommentModel):
        comment_data = {k: v for k, v in comment.dict(exclude_unset=True).items()}
        updated = self.db.update_comment(comment_id, comment_data)
        if not updated:
            logger.error(f"ERROR: Comment with id {comment_id} not found for update")
            return ErrorResponseModel(None, 404, f"Comment with id {comment_id} not found for update")
        return ResponseModel(True, f"Comment with id {comment_id} updated successfully")
    
    def delete_comment(self, comment_id: str):
        deleted = self.db.delete_comment(comment_id)
        if not deleted:
            return ErrorResponseModel(None, 404, f"Comment with id {comment_id} not found for delete")
        return ResponseModel(True, f"Comment with id {comment_id} deleted successfully")

comment_service = CommentService()