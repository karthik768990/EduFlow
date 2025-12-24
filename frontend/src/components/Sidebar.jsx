import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <div className="w-60 bg-gray-900 text-white h-screen p-5 space-y-4">
      <Link to="/" className="block hover:text-blue-400">Dashboard</Link>
      <Link to="/assignments" className="block hover:text-blue-400">Assignments</Link>
      <Link to="/study" className="block hover:text-blue-400">Study</Link>
      <Link to="/reflections" className="block hover:text-blue-400">Reflections</Link>
    </div>
  );
}
    