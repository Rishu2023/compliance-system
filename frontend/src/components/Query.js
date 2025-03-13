import React, { useState } from 'react';
import axios from 'axios';

function Query() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [entities, setEntities] = useState([]);

  const handleQuery = async () => {
    try {
      const res = await axios.post('http://localhost:8000/query', { question: query });
      setResponse(res.data.response);
      setEntities(res.data.entities);
    } catch (error) {
      console.error('Query failed:', error);
      setResponse('An error occurred.');
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto' }}>
      <h1>Regulatory Compliance Query</h1>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask about compliance..."
        style={{ width: '100%', padding: '10px', marginBottom: '10px' }}
      />
      <button onClick={handleQuery} style={{ padding: '10px 20px' }}>Submit</button>
      {response && (
        <div>
          <h3>Response:</h3>
          <p>{response}</p>
        </div>
      )}
      {entities.length > 0 && (
        <div>
          <h3>Detected Entities:</h3>
          <ul>
            {entities.map((ent, idx) => (
              <li key={idx}>{ent[0]} ({ent[1]})</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default Query;