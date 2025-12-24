import { supabase } from "../config/supabase";

export default function Login() {
  const login = async () => {
    await supabase.auth.signInWithOAuth({
      provider: "google",
    });
  };

  return (
    <div>
      <h2>EduFlow Login</h2>
      <button onClick={login}>Sign in with Google</button>
    </div>
  );
}
