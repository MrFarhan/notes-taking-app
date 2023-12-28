import React, { useEffect, useState } from 'react';
import './App.css'; // You can create this file for styling
import Loader from './components/Loader';

function App() {

  const [count, setCount] = useState(0)
  const [loading, setLoading] = useState(true)
  
  useEffect(() => {
    setTimeout(() => setLoading(false), 3000)
  }, [])

  
  if (loading) {
    return <Loader />
  }
  // const [count1, setCount1] = useState(0)

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to My Basic Page</h1>
        <p>This is a simple but good-looking React page.</p>
      </header>
      <main className="App-main">
        <p>Start building your content here!</p>
        <button onClick={() => setCount((prev) => ++prev)}>{count} Update me</button>

      </main>

      <footer className="App-footer">
        <p>&copy; 2023 Your Name</p>
      </footer>
    </div>
  );
}

export default App;
