import { useState } from "react";
import axios from "axios";

export default function App() {
  const [q, setQ] = useState("");
  const [a, setA] = useState("");
  const [loading, setLoading] = useState(false);

  const ask = async (e) => {
    e.preventDefault();
    if (!q.trim()) return;
    setLoading(true);
    const { data } = await axios.post("http://localhost:8000/api/ask", { question: q });
    setA(data.answer);
    setLoading(false);
  };

  return (
    <main className="p-6 max-w-xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">AI Q&A</h1>
      <form onSubmit={ask} className="flex gap-2">
        <input className="flex-1 border p-2 rounded"
               value={q} onChange={e=>setQ(e.target.value)} placeholder="Ask…" />
        <button className="border px-4 rounded">Ask</button>
      </form>

      {loading && <p className="mt-4">Thinking…</p>}
      {a && <p className="mt-4 whitespace-pre-wrap">{a}</p>}
    </main>
  );
}
