import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:3000/api/",
});

axios.defaults.headers.common["Authorization"] =
  "Bearer " + localStorage.getItem("token");

export default {
  addNewUser: (user) => {
    return api.post("user", user);
  },
  loginUser: (user) => {
    api.post("login", user).then((resp) => {
      localStorage.setItem("token", resp.data.token);
    });
  },
};
