import { createContext, useContext, useEffect, useState } from "react";
import { supabase } from "../config/supabase";
import { apiFetch } from "../services/api";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [session, setSession] = useState(null);
  const [userProfile, setUserProfile] = useState(null);
  const [loading, setLoading] = useState(true);

  const loadProfile = async (session) => {
    try {
      const profile = await apiFetch(
        "/users/sync",
        "POST",
        session.access_token
      );
      setUserProfile(profile);
    } catch (err) {
      console.error("Profile sync failed:", err);
      setUserProfile(null); // IMPORTANT: don't block UI
    }
  };

  useEffect(() => {
    supabase.auth.getSession().then(async ({ data }) => {
      setSession(data.session);

      if (data.session) {
        await loadProfile(data.session);
      }

      setLoading(false); // 🔴 ALWAYS stop loading
    });

    const { data: listener } = supabase.auth.onAuthStateChange(
      async (_event, session) => {
        setSession(session);

        if (session) {
          await loadProfile(session);
        } else {
          setUserProfile(null);
        }

        setLoading(false); // 🔴 ALWAYS stop loading
      }
    );

    return () => listener.subscription.unsubscribe();
  }, []);

  return (
    <AuthContext.Provider value={{ session, userProfile, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
