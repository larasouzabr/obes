import axios from "axios";

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
      body,
    }),
  };
  const response = await fetch(baseURL + url, options);
  return await response.json();
}

async function requestFormData(url, body) {
  await axios.post(baseURL + url, body, {
    headers: {
      ...getHeaders(),
      "Content-Type":
        "multipart/form-data; boundary=----WebKitFormBoundarydMIgtiA2YeB1Z0kl",
    },
  });
  /* .then((response) => {
      return response;
    }); */
}

export { request as default, request, getHeaders, requestFormData };
