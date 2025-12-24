import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import { useAuth } from "../context/AuthContext";
import { apiFetch } from "../services/api";

export default function TeacherDoubts() {
  const { session, userProfile } = useAuth();
  const [doubts, setDoubts] = useState([]);

  useEffect(() => {
    if (userProfile?.role === "teacher") {
      apiFetch("/doubts/teacher", "GET", session.access_token)
        .then(setDoubts)
        .catch(() => alert("Failed to load doubts"));
    }
  }, [session, userProfile]);

  return (
    <Layout>
      <h2>Student Doubts</h2>

      {doubts.length === 0 && <p>No doubts yet.</p>}

      {doubts.map((d) => (
        <div key={d.id} className="card" style={{ marginBottom: "10px" }}>
          <p><strong>Student:</strong> {d.student_id}</p>
          <p><strong>Question:</strong> {d.question}</p>
          <p style={{ fontSize: "12px", color: "#666" }}>
            {new Date(d.created_at).toLocaleString()}
          </p>
        </div>
      ))}
    </Layout>
  );
}
