from pymongo import MongoClient
from fastapi import HTTPException
from loguru import logger
from app.config import settings

def comment_helper(comment) -> dict:
    return {
        "id": comment["id"],
        "author": comment["author"],
        "text": comment["text"],
        "date": comment["date"],
        "likes": comment["likes"],
        "image": comment["image"],
    }

class CommentDatabase:

    def __init__(self):
        self.error_address = "Comment Database"
        self.client = MongoClient(settings.mongo_uri)
        self.db = self.client["Comment"]
        self.collection = self.db["comment"]

    # Add a new comment into to the database
    def add_comment(self, comment_data: dict) -> dict:
        comment = self.collection.insert_one(comment_data)
        new_comment = self.collection.find_one({"_id": comment.inserted_id})
        return comment_helper(new_comment)
    
    # Retrieve a comment with a matching ID
    def retrieve_comment(self, id: str) -> dict:
        try:
            comment = self.collection.find_one({"id": id})
            if comment:
                return comment_helper(comment)
        except Exception as e:
            logger.error(f"ERROR: An unexpected error occurred when retrieving comment: {str(e)}")
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred when retrieving comment: {str(e)}") from e

    # Retrieve all comments present in the database
    def retrieve_comments(self) -> list:
        comments = []
        for comment in self.collection.find():
            comments.append(comment_helper(comment))
        return comments

    # Update a comment with a matching ID
    def update_comment(self, id: str, data: dict):
        try:
            # Return false if an empty request body is sent.
            if len(data) < 1:
                return False
            comment = self.collection.find_one({"id": id})
            if comment:
                updated_comment = self.collection.update_one(
                    {"id": id}, {"$set": data}
                )
                if updated_comment:
                    return True
                return False
        except Exception as e:
            logger.error(f"ERROR: An unexpected error occurred when updating comment: {str(e)}")
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred when updating comment: {str(e)}") from e

    # Delete a comment from the database
    def delete_comment(self, id: str):
        try:
            comment = self.collection.find_one({"id": id})
            if comment:
                self.collection.delete_one({"id": id})
                return True
            return False
        except Exception as e:
            logger.error(f"ERROR: An unexpected error occurred when deleting comment: {str(e)}")
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred when deleting comment: {str(e)}") from e

comment_database = CommentDatabase()