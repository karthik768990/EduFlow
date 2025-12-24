const API_URL = "http://127.0.0.1:8000";
//TODO replace it witth .env format

export async function apiFetch(path, method = "GET", token, body) {
  const res = await fetch(`${API_URL}${path}`, {
    method,
    headers: {
      "Content-Type": "application/json",
      ...(token && { Authorization: `Bearer ${token}` }),
    },
    body: body ? JSON.stringify(body) : undefined,
  });

  if (!res.ok) {
    throw new Error("API Error");
  }

  return res.json();
}
  