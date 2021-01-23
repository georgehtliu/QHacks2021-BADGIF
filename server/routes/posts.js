import express from "express";

import { getPosts, createTrans } from "../controllers/posts.js";

const router = express.Router();

router.get("/", getPosts);
router.post("/", createTrans);

export default router;
