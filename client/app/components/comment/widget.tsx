/* eslint-disable @next/next/no-img-element */
"use client";
import { useState, useEffect } from "react";
import { Comment } from "@/app/apis/comment/interfaces";
import { getAllComments, deleteComment, updateComment, addComment } from "@/app/apis/comment/apis";
import { EllipsisVertical, ThumbsUp } from 'lucide-react';
import { generateUUID } from "@/app/utils";

type NewCommentPayload = {
  author: string;
  text: string;
  image: string;
};
const emptyNewComment: NewCommentPayload = {
  author: "",
  text: "",
  image: ""
};

export default function CommentWidget() {
    const [comments, setComments] = useState<Comment[]>([]);
    const [editCommentId, setEditCommentId] = useState<string | null>(null);
    const [newComment, setNewComment] = useState<NewCommentPayload>(emptyNewComment);
    const [isAddModalOpen, setIsAddModalOpen] = useState<boolean>(false);
    const [loading, setLoading] = useState<boolean>(false);

    // Fetch comments when component mounts
    useEffect(() => {
        const fetchComments = async () => {
            const data = await getAllComments();
            setComments(data);
        };
        fetchComments();
    }, []);

    const handleAddNewComment = () => {
        setLoading(true);
        const commentData: Comment = {
            id: generateUUID(),
            author: newComment.author,
            text: newComment.text,
            image: newComment.image,
            date: new Date().toISOString(),
            likes: 0,
        };
        addComment(commentData)
            .then((addedComment) => {
                setComments([...comments, addedComment]);
                setNewComment(emptyNewComment);
                setIsAddModalOpen(false);
                setLoading(false);
            });
    };

    const handleEditThisComment = (id: string) => {
        setLoading(true);
        const commentToUpdate = comments.find((comment) => comment.id === id);
        if (commentToUpdate) {
            updateComment(id, { text: commentToUpdate.text })
                .then(() => {
                    setEditCommentId(null);
                    setLoading(false);
                });
        }
    };

    const handleDeleteThisComment = (id: string) => {
        setLoading(true);
        deleteComment(id)
            .then(() => {
                setComments(comments.filter((comment) => comment.id !== id));
                setLoading(false);
            });
    };

    return (
        <div className="w-full">

            {/* if no comments */}
            {comments.length === 0 && (
                <div className="flex flex-col gap-4 items-center justify-center py-10">
                    <p className="text-center text-gray-500">No comments yet.</p>
                    <button
                        className="mt-4 px-4 py-2 bg-blue-500 text-white rounded w-64"
                        onClick={() => setIsAddModalOpen(true)}
                    >
                        Add a comment
                    </button>
                </div>
            )}

            {comments.map((comment) => (
                <div key={comment.id} className="flex flex-row w-full gap-5 relative px-4 py-3 bg-white rounded-lg shadow-md mb-4">
                    
                    {/* avatar */}
                    <img 
                        src={comment.image || "/default-avatar.png"} 
                        alt={comment.author} 
                        className="w-12 h-12 rounded-full"
                        onError={(e) => e.currentTarget.src="/default-avatar.png"}
                    />

                    {/* content */}
                    <div className="flex flex-col gap-3 w-full">
                        
                        {/* author and time */}
                        <div className="flex items-center space-x-2">
                            <span className="font-bold">{'@ ' + comment.author}</span>
                            <span className="text-sm text-gray-500">{new Date(comment.date).toLocaleString()}</span>
                        </div>

                        {/* text */}
                        {editCommentId === comment.id ? (
                            <div className="flex flex-col w-full">
                                <textarea
                                    className="mt-2 p-2 border rounded w-full h-32"
                                    value={comment.text}
                                    onChange={(e) => {
                                        const updatedComments = comments.map((c) =>
                                            c.id === comment.id ? { ...c, text: e.target.value } : c
                                        );
                                        setComments(updatedComments);
                                    }}
                                />
                                <button
                                    className="mt-2 px-4 py-2 bg-blue-500 text-white rounded"
                                    onClick={() => handleEditThisComment(comment.id)}
                                >
                                    Save
                                </button>
                            </div>
                        ) : (
                            <p className="mt-2">{comment.text}</p>
                        )}

                        {/* likes */}
                        <div className="mt-2 text-sm text-gray-500 flex flex-row gap-2 items-center">
                            <ThumbsUp size={16}/>
                            {comment.likes}
                        </div>
                    </div>

                    {/* edit icon */}
                    <div className="dropdown dropdown-end absolute top-0 right-0 cursor-pointer">
                        <div tabIndex={0} role="button" className="btn m-1">
                            <EllipsisVertical size={20}/>
                        </div>
                        <ul tabIndex={-1} className="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
                            <li>
                                <button onClick={() => setIsAddModalOpen(true)}>Add New</button>
                            </li>
                            <li>
                                {editCommentId === comment.id ? (
                                    <button onClick={() => setEditCommentId('')}>Cancel Edit</button>
                                ) : (
                                    <button onClick={() => setEditCommentId(comment.id)}>Edit</button>
                                )}
                            </li>
                            <li>
                                <button onClick={() => handleDeleteThisComment(comment.id)}>Delete</button>
                            </li>
                        </ul>
                    </div>
                </div>
            ))}

            {/* ADD NEW COMMENT MODAL */}
            {isAddModalOpen && (
                <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
                    <div className="w-full max-w-md rounded-lg bg-white p-6 shadow-lg">
                        <h2 className="text-lg font-semibold mb-4">Add New Comment</h2>

                        <label className="block mb-2 text-sm font-medium">
                            Author
                        <input
                            type="text"
                            className="mt-1 w-full rounded border px-2 py-1"
                            value={newComment.author}
                            onChange={(e) =>
                                setNewComment((prev => ({
                                    ...prev,
                                    author: e.target.value,
                                })))
                            }
                        />
                        </label>

                        <label className="block mb-2 text-sm font-medium">
                            Comment
                        <textarea
                            className="mt-1 w-full rounded border px-2 py-1 h-24"
                            value={newComment.text}
                            onChange={(e) =>
                            setNewComment((prev) => ({
                                    ...prev,
                                    text: e.target.value,
                                }))
                            }
                        />
                        </label>

                        <label className="block mb-4 text-sm font-medium">
                        Avatar URL (optional)
                        <input
                            type="text"
                            className="mt-1 w-full rounded border px-2 py-1"
                            value={newComment.image}
                            onChange={(e) =>
                            setNewComment((prev) => ({
                                    ...prev,
                                    image: e.target.value,
                                }))
                            }
                        />
                        </label>

                        <div className="flex justify-end gap-2">
                        <button
                            className="px-4 py-2 rounded border"
                            onClick={() => setIsAddModalOpen(false)}
                            disabled={loading}
                        >
                            Cancel
                        </button>
                        <button
                            className="px-4 py-2 rounded bg-blue-500 text-white"
                            onClick={handleAddNewComment}
                            disabled={loading}
                        >
                            {loading ? "Creating..." : "Create"}
                        </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}