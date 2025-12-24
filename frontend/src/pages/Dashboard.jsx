import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import { useAuth } from "../context/AuthContext";
import { apiFetch } from "../services/api";

export default function Dashboard() {
  const { session } = useAuth();
  const [leaders, setLeaders] = useState([]);

  useEffect(() => {
    apiFetch("/analytics/leaderboard", "GET", session.access_token)
      .then(setLeaders)
      .catch(() => console.log("Leaderboard unavailable"));
  }, [session]);

  return (
    <Layout>
      <h2>Leaderboard</h2>

      {leaders.length === 0 && <p>No ranking data yet.</p>}

      <table width="100%" style={{ marginTop: "20px" }}>
        <thead>
          <tr>
            <th align="left">Rank</th>
            <th align="left">User</th>
            <th align="left">Score</th>
          </tr>
        </thead>
        <tbody>
          {leaders.map((u, index) => (
            <tr key={index}>
              <td>#{index + 1}</td>
              <td>{u.user_id}</td>
              <td>{u.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </Layout>
  );
}
