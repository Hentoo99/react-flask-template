import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}`)
      .then(res => setMessage(res.data.message))
      .catch(err => console.error(err));
  }, []);
  console.log(process.env.REACT_APP_API_URL)
  return (
    <div>
      <h1>Messaggio dal backend:</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;