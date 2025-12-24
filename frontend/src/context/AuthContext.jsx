import { createContext, useContext, useEffect, useState } from "react";
import { supabase } from "../config/supabase";
import { apiFetch } from "../services/api";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [session, setSession] = useState(null);
  const [userProfile, setUserProfile] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    supabase.auth.getSession().then(async ({ data }) => {
      setSession(data.session);
      if (data.session) {
        const profile = await apiFetch(
          "/users/sync",
          "POST",
          data.session.access_token
        );
        setUserProfile(profile);
      }
      setLoading(false);
    });

    supabase.auth.onAuthStateChange(async (_, session) => {
      setSession(session);
      if (session) {
        const profile = await apiFetch(
          "/users/sync",
          "POST",
          session.access_token
        );
        setUserProfile(profile);
      } else {
        setUserProfile(null);
      }
    });
  }, []);

  return (
    <AuthContext.Provider value={{ session, userProfile, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
