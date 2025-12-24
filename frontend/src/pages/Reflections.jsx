import { useAuth } from "../context/AuthContext";
import { apiFetch } from "../services/api";

export default function Reflections() {
  const { session } = useAuth();

  const submit = async () => {
    await apiFetch(
      "/reflections",
      "POST",
      session.access_token,
      { content: "Good study session today" }
    );
    alert("Reflection submitted");
  };

  return (
    <div>
      <h2>Reflections</h2>
      <button onClick={submit}>Submit Reflection</button>
    </div>
  );
}
