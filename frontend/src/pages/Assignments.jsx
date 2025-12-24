import { useState } from "react";
import Layout from "../components/Layout";
import { useAuth } from "../context/AuthContext";
import { apiFetch } from "../services/api";

export default function Assignments() {
  const { session, userProfile } = useAuth();

  const [doubt, setDoubt] = useState("");

  // TEMP demo assignment (replace with real list later)
  const assignmentId = 1;

  const postDoubt = async () => {
    if (!doubt.trim()) return alert("Enter a doubt");

    await apiFetch(
      "/doubts",
      "POST",
      session.access_token,
      {
        assignment_id: assignmentId,
        question: doubt,
      }
    );

    setDoubt("");
    alert("Doubt sent to teacher");
  };

  const createAssignment = async () => {
    await apiFetch(
      "/assignments",
      "POST",
      session.access_token,
      {
        title: "Algebra Homework",
        subject: "Math",
        deadline: new Date().toISOString(),
      }
    );
    alert("Assignment created");
  };

  return (
    <Layout>
      <h2>Assignments</h2>

      {/* Teacher-only */}
      {userProfile?.role === "teacher" && (
        <button className="btn" onClick={createAssignment}>
          ➕ Create Assignment
        </button>
      )}

      {/* Student-only Doubt Section */}
      {userProfile?.role === "student" && (
        <div style={{ marginTop: "30px" }}>
          <h3>Ask a Doubt</h3>

          <textarea
            rows="4"
            placeholder="Type your doubt here..."
            value={doubt}
            onChange={(e) => setDoubt(e.target.value)}
            style={{ width: "100%", marginBottom: "10px" }}
          />

          <button className="btn" onClick={postDoubt}>
            Send Doubt
          </button>
        </div>
      )}
    </Layout>
  );
}
