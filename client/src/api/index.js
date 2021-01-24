import axios from "axios";

const url = "http://localhost:5000/posts";

export const fetchPosts = () => axios.get(url);
export const getPostsByUser = (user) => axios.get(url + "/" + user);
