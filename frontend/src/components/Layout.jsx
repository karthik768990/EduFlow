import { supabase } from "../config/supabase";
import { useAuth } from "../context/AuthContext";
import { Link } from "react-router-dom";

export default function Layout({ children }) {
  const { userProfile } = useAuth();

  return (
    <div className="app-layout">
      <div className="sidebar">
        {userProfile?.role === "teacher" && (
        <Link to="/teacher/doubts">Student Doubts</Link>
        )}

        <h2>EduFlow</h2>
        <Link to="/">Dashboard</Link>
        <Link to="/assignments">Assignments</Link>
        <Link to="/study">Study</Link>
        <Link to="/reflections">Reflections</Link>
      </div>

      <div className="main">
        <div className="navbar">
          <div>
            <strong>{userProfile?.email}</strong>
          </div>
          <button
            className="logout-btn"
            onClick={() => supabase.auth.signOut()}
          >
            Logout
          </button>
        </div>

        <div className="content">{children}</div>
      </div>
    </div>
  );
}
