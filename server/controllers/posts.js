import mongoose from "mongoose";
import Post from "../models/qhack.js";

export const getPosts = async (req, res) => {
  try {
    const posts = await Post.find({});
    console.log(posts);
    res.status(200).json(posts);
  } catch (error) {
    res.status(404).json({ message: error.message });
  }
};

export const createTrans = async (req, res) => {
  const post = {
    author: 6969696969696969696969,
    mood: 0.2,
    timestamp: "2021-01-23T17:58:11.410+00:00",
  };

  const newPost = new Post(post);

  try {
    await newPost.save();

    res.status(201).json(newPost);
  } catch (error) {
    res.status(409).json({ message: error.message });
  }
};

export const deleteAllPosts = async (req, res) => {
  await Post.remove({});
  res.json({ message: "deleted all posts" });
};
