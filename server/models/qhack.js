import mongoose from "mongoose";

const qhackSchema = mongoose.Schema({
  author: Number,
  mood: Number,
  timestamp: Date,
  server: Number,
  channel: Number,
});

const qhack = mongoose.model("qhack", qhackSchema);

export default qhack;
