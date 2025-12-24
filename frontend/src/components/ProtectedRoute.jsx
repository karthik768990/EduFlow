import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const ProtectedRoute = ({ children, role }) => {
  const { session, user, loading } = useAuth();

  if (loading) {
    return (
      <div style={{ padding: 40, fontSize: 18 }}>
        Initializing session…
      </div>
    );
  }

  if (!session) return <Navigate to="/login" />;

  if (role && user?.role !== role) {
    return <Navigate to="/unauthorized" />;
  }

  return children;
};

export default ProtectedRoute;
