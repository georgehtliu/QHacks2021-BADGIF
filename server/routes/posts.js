import express from "express";

import {
  getPosts,
  createTrans,
  deleteAllPosts,
  getUserPosts,
} from "../controllers/posts.js";

const router = express.Router();

router.get("/", getPosts);
router.get("/:id", getUserPosts);
router.post("/", createTrans);
router.delete("/all", deleteAllPosts);

export default router;
