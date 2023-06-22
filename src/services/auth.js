import decode from "jwt-decode";
import request from "./request";
import api from "./api";
export async function signIn(email, password) {
  const { token, user } = await request(
    "POST",
    "/login",
    JSON.stringify({
      email,
      password,
    })
  );
  localStorage.setItem("token", token);
  localStorage.setItem("user", JSON.stringify(user));
}

export function signOut() {
  localStorage.removeItem("token");
  localStorage.removeItem("user");
}

export function getUserTypeLogged() {
  const user = JSON.parse(localStorage.getItem("user"));
  return user.user_type;
}

export async function hasInfoCompleted() {
  const user = JSON.parse(localStorage.getItem("user"));
  let sit;

  const situation = await api.getUserById(user.id);

  situation.data.address == null ? (sit = false) : (sit = true);
  return sit;
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
