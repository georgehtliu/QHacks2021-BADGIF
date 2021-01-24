import mongoose from "mongoose";

const qhackSchema = mongoose.Schema({
  username: String,
  message: String,
  mood: Number,
  timestamp: Number,
  server: Number,
  channel: Number,
});

const qhack = mongoose.model("qhack", qhackSchema);

export default qhack;
