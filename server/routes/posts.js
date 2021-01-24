import express from "express";

import { getPosts, createTrans, deleteAllPosts } from "../controllers/posts.js";

const router = express.Router();

router.get("/", getPosts);
router.post("/", createTrans);
router.delete("/all", deleteAllPosts);

export default router;
