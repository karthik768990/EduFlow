import { useAuth } from "../context/AuthContext";
import { apiFetch } from "../services/api";

export default function Study() {
  const { session } = useAuth();

  return (
    <div>
      <h2>Study Session</h2>
      <button
        onClick={() =>
          apiFetch("/study-sessions/start", "POST", session.access_token, {
            subject: "Physics",
          })
        }
      >
        Start
      </button>

      <button
        onClick={() =>
          apiFetch("/study-sessions/stop", "POST", session.access_token)
        }
      >
        Stop
      </button>
    </div>
  );
}
