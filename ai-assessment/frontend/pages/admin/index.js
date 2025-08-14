import axios from 'axios'
import { useState } from 'react'
const BE = process.env.BACKEND_URL || "http://localhost:8000"

export default function Admin() {
  const [src, setSrc] = useState('Paste some source text here to generate questions.')
  const [gen, setGen] = useState([])
  const [aid, setAid] = useState('')
  const [title, setTitle] = useState('Quick Assessment')
  const [duration, setDuration] = useState(20)

  const generate = async () => {
    const r = await axios.post(`${BE}/admin/questions/generate`, {
      source_text: src, num_mcq: 2, num_desc: 1, num_code: 1, topic: "Demo", difficulty: "medium"
    })
    setGen(r.data || [])
  }

  const createAssessment = async () => {
    const qids = gen.map(q => q.id)
    const r = await axios.post(`${BE}/admin/assessments/create`, {
      title, duration, question_ids: qids
    })
    setAid(r.data.id)
  }

  return (
    <div style={{ padding: 24 }}>
      <h1>Admin</h1>
      <h3>Generate Questions</h3>
      <textarea rows={4} style={{ width: '100%' }} value={src} onChange={e => setSrc(e.target.value)} />
      <div style={{ marginTop: 8 }}>
        <button onClick={generate}>Generate</button>
      </div>
      <pre>{JSON.stringify(gen, null, 2)}</pre>

      <h3>Create Assessment</h3>
      <input placeholder="Title" value={title} onChange={e => setTitle(e.target.value)} />
      <input type="number" value={duration} onChange={e => setDuration(parseInt(e.target.value||'0'))} style={{ marginLeft: 8 }} />
      <div><button onClick={createAssessment}>Create</button></div>
      {aid && <p>Created assessment ID: {aid}</p>}

      <p><a href="/">Go to Student</a></p>
    </div>
  )
}
