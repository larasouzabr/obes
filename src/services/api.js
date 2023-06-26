import axios from "axios";
const api = axios.create({
  baseURL: "https://obes-backend.onrender.com/api/",
});

export const baseURL = "https://obes-backend.onrender.com/api/";

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
  getBooksDonatedOrSellingByUser: (id) => {
    return api.get(`${id}/books`);
  },
};
