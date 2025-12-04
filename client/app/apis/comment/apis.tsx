import { instance } from "../base/instance";
import { Comment } from "./interfaces";


export const addComment = async (data: Comment): Promise<Comment> => {
    const response = await instance.post("/comment/", data);
    return response.data.data;
}

export const getAllComments = async (): Promise<Comment[]> => {
    const response = await instance.get("/comment/");
    return response.data.data;
}

export const getCommentById = async (id: string): Promise<Comment> => {
    const response = await instance.get(`/comment/${id}`);
    return response.data.data;
}

export const deleteComment = async (id: string): Promise<void> => {
    await instance.delete(`/comment/${id}`);
}

export const updateComment = async (id: string, data: Partial<Comment>): Promise<void> => {
    await instance.put(`/comment/${id}`, data);
}