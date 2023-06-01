const baseURL = "http://localhost:3000/api";

function getHeaders() {
  const token = localStorage.getItem("token");
  return {
    "Content-Type": "application/json",
    ...(token && {
      Authorization: `Bearer ${token}`,
    }),
  };
}

async function request(method, url, body) {
  const options = {
    method,
    headers: getHeaders(),
    ...(method !== "GET" && {
      body: JSON.stringify(body),
    }),
  };
  const response = await fetch(baseURL + url, options);
  return await response.json();
}

export { request as default, request, getHeaders };
