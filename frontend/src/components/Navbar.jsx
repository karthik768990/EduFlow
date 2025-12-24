import { supabase } from "../config/supabase";

export default function Navbar() {
  return (
    <div className="flex justify-between items-center px-6 py-4 bg-white shadow">
      <h1 className="text-xl font-bold">EduFlow</h1>
      <button
        onClick={() => supabase.auth.signOut()}
        className="text-sm bg-red-500 text-white px-4 py-2 rounded"
      >
        Logout
      </button>
    </div>
  );
}
