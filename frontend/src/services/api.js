const BASE_URL = import.meta.env.VITE_BACKEND_URL;

export const apiFetch = async (endpoint, method, token, body) => {
  const res = await fetch(`${BASE_URL}${endpoint}`, {
    method,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: body ? JSON.stringify(body) : undefined,
  });

  if (!res.ok) throw new Error("API Error");
  return res.json();
};
