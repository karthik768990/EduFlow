import { supabase } from "../config/supabase";

export default function Login() {
  return (
    <div className="login-container">
      <div className="login-box">
        <h2 style={{ marginBottom: "20px" }}>EduFlow Login</h2>
        <button
          className="btn"
          onClick={() => supabase.auth.signInWithOAuth({ provider: "google" })}
        >
          Sign in with Google
        </button>
      </div>
    </div>
  );
}
