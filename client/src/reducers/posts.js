export default (posts = [], action) => {
  switch (action.type) {
    case "FETCH_ALL":
      return action.payload;
    case "FETCH_BY_USER":
      return action.payload;
    default:
      return posts;
  }
};
