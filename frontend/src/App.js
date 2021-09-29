import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [myMessage, setMyMessage] = useState({})
  const [state, setState] = useState({})
  const [myMessageIds, setMyMessageIds] = useState('')
  const [myMessageName, setMyMessageName] = useState('')
  const [fileData, setFileData] = useState('')

  const options = [
    { value: 'Blåskjellsalat.txt', label: 'Blåskjellsalat.txt' },
    { value: 'Andebryst med pastinakkrem og appelsinsaus.txt', label: 'Andebryst med pastinakkrem og appelsinsaus.txt' },
    { value: 'Gulasj.txt', label: 'Gulasj.txt' },
    { value: 'Burrito med stekt kyllingfilet, ris, avokadodressing, paprika-, chili- og mangosalsa.txt', label: 'Burrito med stekt kyllingfilet, ris, avokadodressing, paprika-, chili- og mangosalsa.txt' },
  ];

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


  const handleChange = (e) => {
    const {name, value} = e.target
    setState({ value });
    console.log(`handleChange Option selected:`, value);
    console.log('handleChange The link was clicked.');
    axios.get(`https://reactflask-smb.herokuapp.com/flask/oppskriftInfo/${value}`).then(response => {
      console.log("2.handleChange SUCCESS: ", response);
      console.log(response);
      setFileData(response.data);
    }).catch(error => {
      console.log(error)
    });
  };

  const handleClick = (e) => {
    e.preventDefault();
    console.log('The link was clicked.');
    const variable_name = 'Gulasj.txt';
    axios.get(`https://reactflask-smb.herokuapp.com/flask/oppskriftInfo/${variable_name}`).then(response => {
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
      <p>
      <select onChange={e => handleChange(e)} className="SelectFile" >
        {options.map((value, label) => <option value={value}>{label}</option>)}
      </select >
      
      Filer:
      {fileData && fileData}

      </p>
    </div>
  );
}

export default App;
