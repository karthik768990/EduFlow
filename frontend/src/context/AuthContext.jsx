import { createContext, useContext, useEffect, useState } from "react";
import { supabase } from "../config/supabase";
import { apiFetch } from "../services/api";

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [session, setSession] = useState(null);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const loadProfile = async (accessToken) => {
    try {
      const profile = await apiFetch(
        "/users/sync",
        "POST",
        accessToken
      );
      setUser(profile);
    } catch (err) {
      console.error("Profile sync failed:", err);
      setUser(null);
    }
  };

  useEffect(() => {
    supabase.auth.getSession().then(({ data }) => {
      setSession(data.session);
      if (data.session?.access_token) {
        loadProfile(data.session.access_token);
      }
      setLoading(false);
    });

    const { data: listener } = supabase.auth.onAuthStateChange(
      async (_event, session) => {
        setSession(session);
        if (session?.access_token) {
          await loadProfile(session.access_token);
        } else {
          setUser(null);
        }
        setLoading(false);
      }
    );

    return () => listener.subscription.unsubscribe();
  }, []);

  return (
    <AuthContext.Provider value={{ session, user, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

/* ✅ THIS WAS MISSING */
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used inside AuthProvider");
  }
  return context;
};
