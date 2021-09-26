import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.get('https://reactflask-smb.herokuapp.com/flask/hello').then(response => {
      console.log("SUCCESS", response);
      console.log(response);
      setGetMessage(response);
    }).catch(error => {
      console.log(error)
    });
  }, []);


  const handleClick = (e) => {
    e.preventDefault();
    console.log('The link was clicked.');
    const variable_name = 'Samuel';
    axios.get(`https://reactflask-smb.herokuapp.com/flask/${variable_name}`).then(response => {
      console.log("SUCCESS", response);
      console.log(response);
    }).catch(error => {
      console.log(error)
    });

  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>React + Flask Tutorial</p>
        <div>{getMessage.status === 200 ? 
          <h3> YES!!! {getMessage.data.message}</h3>
          :
          <h3>LOADING</h3>}</div>
      </header>
      <h3>
      Simon!!!
      <a href="#" onClick={handleClick}>
        Click me
      </a>
      Mukunga!!!!
      </h3>
    </div>
  );
}

export default App;
