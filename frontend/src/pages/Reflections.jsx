import Layout from "../components/Layout";
import { useAuth } from "../context/AuthContext";
import { apiFetch } from "../services/api";

export default function Reflections() {
  const { session } = useAuth();

  return (
    <Layout>
      <h2 className="text-xl font-bold mb-4">Reflections</h2>
      <button
        onClick={() =>
          apiFetch("/reflections", "POST", session.access_token, {
            content: "Great session today",
          })
        }
        className="bg-purple-500 text-white px-4 py-2 rounded"
      >
        Submit Reflection
      </button>
    </Layout>
  );
}
