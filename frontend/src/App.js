import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('http://127.0.0.1:5000/upload', {
      method: 'POST',
      body: formData,
    });
  };

  const handleQuestionSubmit = async () => {
    const response = await fetch('http://127.0.0.1:5000/ask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question }),
    });

    const data = await response.json();
    setAnswer(data.answer);

  };

  return (
    <div className="App">
      <header className="App-header">
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload}>Upload PDF</button>
        <div>
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask a question"
          />
          <button onClick={handleQuestionSubmit}>Ask</button>
        </div>
        {answer && <p>Answer: {answer}</p>}
      </header>
    </div>
  );
}

export default App;
