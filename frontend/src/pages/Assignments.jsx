import Layout from "../components/Layout";
import { useAuth } from "../context/AuthContext";
import { apiFetch } from "../services/api";

export default function Assignments() {
  const { session, userProfile } = useAuth();

  const createAssignment = async () => {
    await apiFetch(
      "/assignments",
      "POST",
      session.access_token,
      {
        title: "Algebra HW",
        subject: "Math",
        deadline: new Date().toISOString(),
      }
    );
    alert("Assignment created");
  };

  return (
    <Layout>
      <h2>Assignments</h2>

      {userProfile?.role === "teacher" && (
        <button className="btn" onClick={createAssignment}>
          ➕ Create Assignment
        </button>
      )}

      {userProfile?.role === "student" && (
        <p>You can view and complete assignments.</p>
      )}
    </Layout>
  );
}
