import { useAuth } from "../context/AuthContext";
import { apiFetch } from "../services/api";

export default function Assignments() {
  const { session } = useAuth();

  const createAssignment = async () => {
    await apiFetch(
      "/assignments",
      "POST",
      session.access_token,
      {
        title: "Demo Assignment",
        subject: "Math",
        deadline: new Date().toISOString(),
      }
    );
    alert("Assignment created");
  };

  return (
    <div>
      <h2>Assignments</h2>
      <button onClick={createAssignment}>Create Assignment</button>
    </div>
  );
}
