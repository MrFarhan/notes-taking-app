import React, { useEffect, useState } from 'react';
import axios from 'axios'; // For making HTTP requests to the backend
import "./App.css"
function App() {
  const [note, setNote] = useState('');
  const [stackNotes, setStackNotes] = useState([]);
  const [queueNotes, setQueueNotes] = useState([]);

  let baseUrl = `http://127.0.0.1:5000`;

  const addNote = () => {
    axios.post(`${baseUrl}/add_note`, { note })
      .then(response => {
        console.log(response.data);
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
        const { queue_notes, stack_notes } = response.data;
        setStackNotes(stack_notes);
        setQueueNotes(queue_notes);
      })
      .catch(error => {
        console.error('Error viewing notes:', error);
      });
  };

  const deleteNote = (noteIndex, isStack) => {
    const endpoint = isStack ? 'stack' : 'queue';
    axios.delete(`${baseUrl}/delete_note/${endpoint}/${noteIndex}`)
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
          <ul>
            {stackNotes.map((note, index) => (
              <li key={`stack-${index}`}>
                <span>{note}</span>
                <button onClick={() => deleteNote(index, true)}>Delete</button>
              </li>
            ))}
          </ul>
        </div>
        <div className="queue-notes">
          <h2>Queue Notes:</h2>
          <ul>
            {queueNotes.map((note, index) => (
              <li key={`queue-${index}`}>
                <span>{note}</span>
                <button onClick={() => deleteNote(index, false)}>Delete</button>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default App;
