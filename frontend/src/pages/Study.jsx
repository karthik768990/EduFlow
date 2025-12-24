import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import { useAuth } from "../context/AuthContext";
import { apiFetch } from "../services/api";

export default function Study() {
  const { session } = useAuth();
  const [seconds, setSeconds] = useState(0);
  const [running, setRunning] = useState(false);

  useEffect(() => {
    let interval;
    if (running) {
      interval = setInterval(() => {
        setSeconds((s) => s + 1);
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [running]);

  const start = async () => {
    await apiFetch("/study-sessions/start", "POST", session.access_token, {
      subject: "Physics",
    });
    setSeconds(0);
    setRunning(true);
  };

  const stop = async () => {
    await apiFetch("/study-sessions/stop", "POST", session.access_token);
    setRunning(false);
    alert("Study session saved!");
  };

  return (
    <Layout>
      <h2>Study Timer</h2>
      <h1>{Math.floor(seconds / 60)}:{seconds % 60}</h1>

      {!running ? (
        <button className="btn secondary" onClick={start}>
          ▶ Start
        </button>
      ) : (
        <button className="btn danger" onClick={stop}>
          ⏹ Stop
        </button>
      )}
    </Layout>
  );
}
