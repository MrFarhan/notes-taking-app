import React, { useEffect, useState } from 'react';
import axios from 'axios'; // For making HTTP requests to the backend
import "./App.css"
function App() {
  const [note, setNote] = useState('');
  const [stackNotes, setStackNotes] = useState([]);
  const [queueNotes, setQueueNotes] = useState([]);
  const [sortNotes, setSortNotes] = useState([]);

  let baseUrl = `http://127.0.0.1:5000`;

  const addNote = () => {
    axios.post(`${baseUrl}/add_note`, { note })
      .then(response => {
        console.log(response.data);
        setNote("")
        viewNotes();
      })
      .catch(error => {
        console.error('Error adding note:', error);
      });
  };

  const viewNotes = () => {
    axios.get(`${baseUrl}/view_notes`)
      .then(response => {
        console.log("response is ", response.data);
        const { queue_notes, stack_notes, sort_notes } = response.data;
        setStackNotes(stack_notes);
        setQueueNotes(queue_notes);
        setSortNotes(sort_notes);
      })
      .catch(error => {
        console.error('Error viewing notes:', error);
      });
  };

  const deleteNote = (endpoint) => {
    axios.delete(`${baseUrl}/delete_note/${endpoint}`)
      .then(response => {
        console.log(response.data);
        viewNotes();
      })
      .catch(error => {
        console.error('Error deleting note:', error);
      });
  };


  useEffect(() => {
    viewNotes();
  }, []);

  return (
    <div className="App">
      <h1>Note Management</h1>
      <div className="input-container">
        <input
          type="text"
          value={note}
          onChange={(e) => setNote(e.target.value)}
          placeholder="Enter your note"
        />
        <button onClick={addNote}>Add Note</button>
      </div>

      <div className="notes-container">
        <div className="stack-notes">
          <h2>Stack Notes:</h2>
            <button onClick={() => deleteNote("stack")}>Delete</button>
          <ul>
            {stackNotes.map((note, index) => (
              <li key={`stack-${index}`}>
                <span>{note}</span>
              </li>
            ))}
          </ul>
        </div>
        <div className="queue-notes">
          <h2>Queue Notes:</h2>
            <button onClick={() => deleteNote("queue")}>Delete</button>
          <ul>
            {queueNotes.map((note, index) => (
              <li key={`queue-${index}`}>
                <span>{note}</span>
              </li>
            ))}
          </ul>
        </div>

        <div className="sort-notes">
          <h2>Sort Notes:</h2>
            <button onClick={() => deleteNote("sort")}>Delete</button>
          <ul>
            {sortNotes.map((note, index) => (
              <li key={`sort-${index}`}>
                <span>{note}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default App;
