import { useAuth } from "../context/AuthContext";
import { apiFetch } from "../services/api";

export default function Dashboard() {
  const { session } = useAuth();

  const testBackend = async () => {
    const res = await apiFetch("/auth/me", "GET", session.access_token);
    alert(JSON.stringify(res, null, 2));
  };

  return (
    <div>
      <h1>Dashboard</h1>
      <button onClick={testBackend}>Test Backend Auth</button>
    </div>
  );
}
