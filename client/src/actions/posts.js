import * as api from "../api";
import { FETCH_ALL, FETCH_BY_USER } from "../constants/actionTypes";

// Action Creators
export const getPosts = () => async (dispatch) => {
  try {
    const { data } = await api.fetchPosts();
    dispatch({ type: FETCH_ALL, payload: data });
  } catch (error) {
    console.log(error.message);
  }
};

export const getPostsByUser = (user) => async (dispatch) => {
  try {
    const { data } = await api.getPostsByUser(user);
    dispatch({ type: FETCH_BY_USER, payload: data });
  } catch (error) {
    console.log(error.message);
  }
};

// export const updatePost = (id, post) => async (dispatch) => {
//   try {
//     const { data } = await api.updatePost(id, post);
//     dispatch({ type: UPDATE, payload: data });
//   } catch (err) {
//     console.log(err);
//   }
// };
