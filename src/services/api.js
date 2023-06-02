import axios from "axios";
const api = axios.create({
  baseURL: "http://localhost:3000/api/",
});

export const baseURL = "http://localhost:3000/api/";

export default {
  addNewUser: (user) => {
    return api.post("user", user);
  },
  getBooks: () => {
    return api.get("books");
  },
  getBookById: (id) => {
    return api.get(`books/${id}`);
  },
  getUserById: (id) => {
    return api.get(`user/${id}`);
  },
  getAllCategories: () => {
    return api.get("categories");
  },
  getCategoryById: (id) => {
    return api.get(`categories/${id}`);
  },
};
