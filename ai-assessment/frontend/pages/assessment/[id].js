import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'
import axios from 'axios'
const BE = process.env.BACKEND_URL || "http://localhost:8000"

export default function TakeAssessment() {
  const router = useRouter()
  const { id } = router.query
  const [assessment, setAssessment] = useState(null)
  const [questions, setQuestions] = useState([])
  const [answers, setAnswers] = useState({})
  const [result, setResult] = useState(null)

  useEffect(() => {
    if (!id) return
    axios.get(`${BE}/assessments/available`).then(r => {
      const a = (r.data || []).find(x => x.id === id)
      setAssessment(a || null)
      if (a && a.question_ids && a.question_ids.length) {
        axios.get(`${BE}/admin/questions/review`).then(rr => {
          const sample = rr.data.sample || []
          const picked = sample.filter(q => a.question_ids.includes(q.id))
          setQuestions(picked)
        })
      }
    })
  }, [id])

  const submit = async () => {
    const payload = {
      user_id: null,
      answers: Object.keys(answers).map(qid => ({ question_id: qid, answer: answers[qid] }))
    }
    const r = await axios.post(`${BE}/assessments/${id}/submit`, payload)
    setResult(r.data)
  }

  if (!assessment) return <div style={{ padding: 24 }}>Loading...</div>

  return (
    <div style={{ padding: 24 }}>
      <h2>{assessment.title}</h2>
      <ol>
        {questions.map(q => (
          <li key={q.id} style={{ marginBottom: 16 }}>
            <div><strong>{q.type.toUpperCase()}</strong>: {q.question}</div>
            {q.type === 'mcq' && (
              <div>
                {(q.options || []).map(op => (
                  <label key={op} style={{ display: 'block' }}>
                    <input type="radio" name={q.id} onChange={() => setAnswers(prev => ({ ...prev, [q.id]: op }))} />
                    {op}
                  </label>
                ))}
              </div>
            )}
            {q.type === 'descriptive' && (
              <textarea rows={3} style={{ width: '100%' }} onChange={e => setAnswers(prev => ({ ...prev, [q.id]: e.target.value }))} />
            )}
            {q.type === 'coding' && (
              <textarea rows={6} placeholder="Paste your code here" style={{ width: '100%' }} onChange={e => setAnswers(prev => ({ ...prev, [q.id]: e.target.value }))} />
            )}
          </li>
        ))}
      </ol>
      <button onClick={submit}>Submit</button>

      {result && (
        <div style={{ marginTop: 24 }}>
          <h3>Result</h3>
          <p>Score: {result.score}%</p>
          <pre style={{ whiteSpace: 'pre-wrap' }}>{result.feedback}</pre>
        </div>
      )}
    </div>
  )
}
