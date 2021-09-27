import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [myMessage, setMyMessage] = useState({})
  const [myMessageIds, setMyMessageIds] = useState('')
  const [myMessageName, setMyMessageName] = useState('')


  useEffect(()=>{
    axios.get('https://reactflask-smb.herokuapp.com/flask/hello').then(response => {
      console.log("SUCCESS", response);
      console.log(response);
      setMyMessage(response.data.message);
    }).catch(error => {
      console.log(error)
    });
  }, []);


  useEffect(()=>{
    const id = 100;
    axios.get(`https://reactflask-smb.herokuapp.com/flask/${id}`).then(response => {
      console.log("1.USE ID-SUCCESS: ", response);
      console.log(response);
      setMyMessageIds(response.data);
    }).catch(error => {
      console.log(error)
    });
  }, []);

  const handleClick = (e) => {
    e.preventDefault();
    console.log('The link was clicked.');
    const name = 'kylling';
    axios.get(`https://reactflask-smb.herokuapp.com/flask/kategori/${name}`).then(response => {
      console.log("2.SUCCESS: ", response);
      console.log(response);
      setMyMessageName(response.data);
    }).catch(error => {
      console.log(error)
    });
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>React + Flask Tutorial</p>
        <div>{myMessage.status === 200 ? 
          <h3> Henting av meldinger fra Flask Fungerer som det skal: {myMessage.data.message} Ids {myMessageIds} Name {myMessageName} </h3>
          :
          <h3>..LOADING..</h3>}</div>
      </header>
      <h3>
      <p> xsxsx Testing - Pyton Flask Test: 
      <a href="#" onClick={handleClick}>
        Click me
      </a>
     </p>
      </h3>
    </div>
  );
}

export default App;
