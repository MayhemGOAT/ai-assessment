import useSWR from 'swr'
import axios from 'axios'
const fetcher = url => axios.get(url).then(r => r.data)
const BE = process.env.NEXT_PUBLIC_BACKEND_URL || process.env.BACKEND_URL || "";

export default function Home() {
  const { data } = useSWR(`${BE}/assessments/available`, fetcher)
  return (
    <div style={{ padding: 24 }}>
      <h1>AI Assessment - Student</h1>
      <ul>
        {(data || []).map(a => (
          <li key={a.id}>
            <strong>{a.title}</strong> – {a.duration} min – <a href={`/assessment/${a.id}`}>Start</a>
          </li>
        ))}
      </ul>
      <p><a href="/admin">Go to Admin</a></p>
    </div>
  )
}
