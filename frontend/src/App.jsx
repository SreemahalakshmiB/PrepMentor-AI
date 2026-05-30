import { useState } from "react";
import axios from "axios";

function App() {
  const [formData, setFormData] = useState({
    name: "",
    goal: "",
    hours: "",
    weakSubjects: "",
    mood: "",
  });

  const [studyPlan, setStudyPlan] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const generatePlan = async () => {
    try {
      setLoading(true);

      const response = await axios.post(
        "https://prepmentor-backend.onrender.com/generate-plan",
        formData
      );

      setStudyPlan(response.data.studyPlan);
    } catch (error) {
      alert("Something went wrong!");
      console.log(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 flex justify-center items-center p-8">
      <div className="bg-slate-800 p-8 rounded-2xl shadow-xl w-full max-w-2xl">
        <h1 className="text-4xl font-bold text-white text-center mb-2">
          🚀 PrepMentor AI
        </h1>

        <p className="text-gray-400 text-center mb-8">
          Smart Adaptive Study Planner
        </p>

        <div className="space-y-4">
          <input
            type="text"
            name="name"
            placeholder="Enter Your Name"
            className="w-full p-3 rounded-lg bg-slate-700 text-white"
            onChange={handleChange}
          />

          <select
            name="goal"
            className="w-full p-3 rounded-lg bg-slate-700 text-white"
            onChange={handleChange}
          >
            <option value="">Select Goal</option>
            <option value="GATE">GATE</option>
            <option value="Placements">Placements</option>
            <option value="Both">GATE + Placements</option>
          </select>

          <input
            type="number"
            name="hours"
            placeholder="Study Hours Per Day"
            className="w-full p-3 rounded-lg bg-slate-700 text-white"
            onChange={handleChange}
          />

          <input
            type="text"
            name="weakSubjects"
            placeholder="Weak Subject"
            className="w-full p-3 rounded-lg bg-slate-700 text-white"
            onChange={handleChange}
          />

          {/* Mood Dropdown */}
          <select
            name="mood"
            className="w-full p-3 rounded-lg bg-slate-700 text-white"
            onChange={handleChange}
          >
            <option value="">Select Mood</option>
            <option value="Motivated">😊 Motivated</option>
            <option value="Normal">😐 Normal</option>
            <option value="Tired">😞 Tired</option>
            <option value="Stressed">😫 Stressed</option>
            <option value="Focused">🔥 Highly Focused</option>
          </select>

          <button
            onClick={generatePlan}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-lg font-bold"
          >
            {loading ? "Generating..." : "Generate Plan"}
          </button>
        </div>

        {studyPlan && (
          <div className="mt-8 bg-slate-700 p-5 rounded-xl text-white whitespace-pre-wrap">
            {studyPlan}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;