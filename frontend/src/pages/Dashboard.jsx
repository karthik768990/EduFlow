import { useEffect, useRef } from "react";
import Layout from "../components/Layout";
import Chart from "chart.js/auto";

export default function Dashboard() {
  const chartRef = useRef();

  useEffect(() => {
    new Chart(chartRef.current, {
      type: "bar",
      data: {
        labels: ["Assignments", "Study Sessions", "Reflections"],
        datasets: [
          {
            label: "Activity",
            data: [5, 8, 3],
            backgroundColor: ["#2563eb", "#16a34a", "#7c3aed"],
          },
        ],
      },
    });
  }, []);

  return (
    <Layout>
      <h2>Dashboard</h2>
      <canvas ref={chartRef} height="100"></canvas>
    </Layout>
  );
}
