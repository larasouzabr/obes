import decode from "jwt-decode";
import request from "./request";
import api from "./api";
export async function signIn(email, password) {
  const { token, user } = await request("POST", "/login", {
    email,
    password,
  });
  localStorage.setItem("token", token);
  localStorage.setItem("user", JSON.stringify(user));
}

export function signOut() {
  localStorage.removeItem("token");
  localStorage.removeItem("user");
}

export function getUserLoggedInfo() {
  const user = JSON.parse(localStorage.getItem("user"));
  api
    .getUserById(user.id)
    .then((response) => {
      console.log(response.data);
      return response.data;
    })
    .catch((error) => {
      console.error(error);
    });
}

export function isSignedIn() {
  const token = localStorage.getItem("token");

  if (!token) return false;

  try {
    const { exp: expiration } = decode(token);
    const isExpired = !!expiration && Date.now() > expiration * 1000;

    if (isExpired) return false;
    return true;
  } catch (_) {
    return false;
  }
}
